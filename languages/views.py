from django.views.generic import ListView, DetailView
from django.shortcuts import render
from . import models


class LanguagesView(ListView):

    """HomeView"""

    model = models.Language


def Language_noteView(request, pk):
    return render(request, "languages/language.html")
