from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from snippets.apis import cbv_apiview

urlpatterns = [
    path('snippets/', cbv_apiview.SnippetList.as_view()),
    path('snippets/<int:pk>/', cbv_apiview.SnippetDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
