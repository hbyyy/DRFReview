from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from snippets.apis import cbv_mixins

urlpatterns = [
    path('snippets/', cbv_mixins.SnippetList.as_view()),
    path('snippets/<int:pk>/', cbv_mixins.SnippetDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
