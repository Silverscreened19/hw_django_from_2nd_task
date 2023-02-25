from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlete': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'butter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def recipies(request, recipy):
    recipies = {}
    servings = int(request.GET.get('servings', 1))
    dish = DATA.get(recipy)
    for key, value in dish.items():
        value_new = round(value * servings, 2)
        recipies.setdefault(key, value_new)
    context = {'recipy': recipies}
    return render(request, 'calculator/index.html', context)


def home(msg):
    msg = 'Введите название рецепта в адресной строке'
    return HttpResponse(msg)
# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
