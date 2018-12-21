from django.urls import path

from .apis import CardListCreateView

urlpatterns = [
    path('', CardListCreateView.as_view()),
]
