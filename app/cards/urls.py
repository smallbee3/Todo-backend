from django.urls import path

from .apis import CardListCreateView, CardRetrieveUpdateDestroyView

urlpatterns = [
    path('', CardListCreateView.as_view()),
    path('<int:pk>/', CardRetrieveUpdateDestroyView.as_view()),
]
