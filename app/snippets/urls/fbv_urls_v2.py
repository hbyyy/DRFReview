from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from ..apis import fbv_v2

urlpatterns = [
    path('snippets/', fbv_v2.snippet_list),
    path('snippets/<int:pk>/', fbv_v2.snippet_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)
