from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
# Including format_suffix_patterns is an optional choice that 
# provides a simple, DRY way to refer to a specific file format for 
# a URL endpoint. It means our API will be able to handle 
# URls such as http://example.com/api/items/4.json rather than 
# just http://example.com/api/items/4.