from django.urls import path

from ..apis import fbv_v1

urlpatterns = [
    path('snippets/', fbv_v1.snippet_list),
    path('snippets/<int:pk>/', fbv_v1.snippet_detail)
]
