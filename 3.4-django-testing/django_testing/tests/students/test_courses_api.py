from django.urls import reverse
import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.filters import CourseFilter
from students.models import Student, Course


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.fixture
def course_factory(student_factory):
    def factory(*args, **kwargs):
        students_set = student_factory(_quantity=3)
        return baker.make(Course, students=students_set, *args, **kwargs, make_m2m=True)
    return factory


# получение первого курса
@pytest.mark.django_db
def test_retrieve_course(client, course_factory):
    course = course_factory()
    response = client.get(reverse('courses-detail', kwargs={'pk': course.pk}))
    data = response.json()
    assert response.status_code == 200
    assert data['id'] == course.pk


# получение списка курсов
@pytest.mark.django_db
def test_courses_list(client, course_factory):
    course = course_factory(_quantity=5)
    url = reverse('courses-list')
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 5
    assert len(response.data) == len(course)


# проверка фильтрации списка курсов по id:
@pytest.mark.django_db
def test_course_id(client, course_factory):
    courses = course_factory(_quantity=3)
    filtered_ids = [courses[0].pk, courses[2].pk]
    url = reverse('courses-list')
    data = {'id': filtered_ids}
    response = client.get(url, data)
    assert response.status_code == 200
    assert len(response.json()) == len(filtered_ids)
    assert all(course['id'] in filtered_ids for course in response.json())


# проверка фильтрации списка курсов по name
@pytest.mark.django_db
def test_course_name(client, course_factory):
    courses = course_factory(_quantity=3)
    some_course = course_factory(name='Math')
    courses.append(some_course)
    url = reverse('courses-list')
    my_filter = CourseFilter(data={'name': 'Math'}, queryset=Course.objects.all())
    response = client.get(url, {'name': 'Math'})
    data = response.json()
    assert response.status_code == 200
    assert len(courses) == 4
    assert courses[3].name == some_course.name
    assert courses[3].name == data[0]['name']
    assert courses[3].id == data[0]['id']
    assert all(course.id == some_course.pk for course in my_filter.qs)


# тест успешного создания курса:
@pytest.mark.django_db
def test_create_course(client):
    data = {
        'name': 'Python'
    }
    url = reverse('courses-list')
    response = client.post(url, data)
    assert response.status_code == 201
    assert Course.objects.count() == 1
    assert response.data['name'] == data['name']


# тест успешного обновления курса:
@pytest.mark.django_db
def test_patch_course(client, course_factory):
    course = course_factory()
    new_data = {
        'name': 'New course'
    }
    url = reverse('courses-detail', kwargs={'pk': course.pk})
    response = client.patch(url, new_data)
    assert response.status_code == 200
    assert response.data['name'] == new_data['name']


# тест успешного удаления курса.
@pytest.mark.django_db
def test_delete_course(client, course_factory):
    course = course_factory()
    count = Course.objects.count()
    url = reverse('courses-detail', kwargs={'pk': course.pk})
    response = client.delete(url)
    assert Course.objects.count() == count-1
    assert response.status_code == 204
    assert not Course.objects.filter(id=course.pk).exists()