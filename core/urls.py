from django.urls import path, include
from categorys import views as category_views
from languages import views as language_views
from portfolios import views as portfolio_views
from self_introductions import views as self_introduction_views


app_name = "core"

urlpatterns = [
    path("", category_views.CategoryView.as_view(), name="categorys"),
    path("Code/", include("languages.urls", namespace="language")),
    # path("Portfolios/", portfolio_views.HomeView.as_view(), name="portfolio"),
    # path(
    #    "Introduction/",
    #    self_introduction_views.HomeView.as_view(),
    #    name="self_introduction",
    # ),
]
