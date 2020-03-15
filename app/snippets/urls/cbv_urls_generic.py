from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from snippets.apis import cbv_generic

urlpatterns = [
    path('snippets/', cbv_generic.SnippetList.as_view()),
    path('snippets/<int:pk>/', cbv_generic.SnippetDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
