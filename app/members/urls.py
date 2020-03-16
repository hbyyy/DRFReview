from django.urls import path
from rest_framework.authtoken import views
from .apis import UserList, UserDetail, CustomAuthToken

urlpatterns = [
    path('', UserList.as_view()),
    path('<int:pk>/', UserDetail.as_view()),
    path('api-token-auth/', CustomAuthToken.as_view()),
]