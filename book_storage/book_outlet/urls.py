from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>', views.detail, name='book-page'),
    path('<slug:book_slug>', views.detail_slug, name='book-page-slug'),
]