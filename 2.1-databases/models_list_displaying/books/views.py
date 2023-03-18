from django.shortcuts import render
from django.core.paginator import Paginator
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {'books': books}
    return render(request, template, context)


def book_date(request, pub_date):
    template = 'books/books_by_date.html'
    books_date = Book.objects.filter(pub_date = pub_date)
    all_dates = Book.objects.values_list('pub_dates', flat=True)
    sorted_dates_list = sorted([date for date in all_dates])
    page_number = None
    prev_date = None
    next_date = None
    i = 0
    paginator = Paginator(sorted_dates_list, 1)
    for date in paginator.object_list:
        if str(date) == pub_date:
            page_number = i+1

    context = {'books': books}
    return render(request, template, context)
