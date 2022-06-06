from django.shortcuts import render

from main.models import Person


def view_home(request):
    home = Person.objects.all()
    return render(request, 'home.html', {'home': home})
