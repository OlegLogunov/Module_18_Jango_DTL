from django.shortcuts import render
from django.views.generic import TemplateView


def menu_page(request):
    return render(request, 'menu.html')


def shop_page(request):
    santech = ['Смесители', 'Фаянс', 'Ванны', 'Полотенцесушители']
    context = {
        'santech': santech
    }
    return render(request, 'shop_page.html', context)


def bin_page(request):
    cont = 'Продолжить покупки'
    done = 'Оформить заказ'
    context = {
        'cont': cont,
        'done': done,

    }
    return render(request, 'bin_page.html', context)
