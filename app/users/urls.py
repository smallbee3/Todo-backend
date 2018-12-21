from django.urls import path

from .apis import UserListCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [
    path('', UserListCreateView.as_view()),
    path('<int:pk>/', UserRetrieveUpdateDestroyView.as_view()),
]
