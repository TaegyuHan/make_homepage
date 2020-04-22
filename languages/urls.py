from django.urls import path
from languages import views as language_views
from . import models

app_name = "language"


urlpatterns = [
    path("", language_views.LanguagesView.as_view(), name="code_categorys"),
    path("<int:pk>", language_views.Language_noteView, name="detail"),
]
