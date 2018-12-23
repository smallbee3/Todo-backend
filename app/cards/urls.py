from django.urls import path

from .apis import CardListCreateAPIView, CardRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', CardListCreateAPIView.as_view()),
    path('<int:pk>/', CardRetrieveUpdateDestroyAPIView.as_view()),
]
