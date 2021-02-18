from django.shortcuts import render
import random


def home(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        upper = 'checked'
    else:
        upper = ''
    if request.GET.get('special'):
        characters.extend('!@#$%^&*?()-+=|~')
        special = 'checked'
    else:
        special = ''
    if request.GET.get('numbers'):
        characters.extend('0123456789')
        numbers = 'checked'
    else:
        numbers = ''

    length = int(request.GET.get('length', 12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/home.html', {
        'password': thepassword,
        'length': length,
        'upper': upper,
        'special': special,
        'numbers': numbers,
    })


def about(request):
    return render(request, 'generator/about.html')
