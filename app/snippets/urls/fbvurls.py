from django.urls import path

from ..apis import fbv

urlpatterns = [
    path('snippets/', fbv.snippet_list),
    path('snippets/<int:pk>/', fbv.snippet_detail)
]
