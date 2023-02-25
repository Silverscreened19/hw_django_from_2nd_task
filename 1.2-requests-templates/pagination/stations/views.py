from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    bus_stops_list = []
    with open('data-398-2018-08-30.csv', encoding='UTF-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            bus_stops_list.append(row)

    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(bus_stops_list, 10)
    page = paginator.get_page(page_number)
    objects_on_page = page.object_list
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    context = {
    'bus_stations': objects_on_page,
    'page': page,
    }
    return render(request, 'stations/index.html', context)
