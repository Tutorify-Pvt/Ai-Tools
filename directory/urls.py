from django.urls import path
from .views import *
urlpatterns = [
    path("", list_directory, name='directory_view'),
    path("directory/get/<str:id>", get_directory, name='get_directory'),
    path("reviewing/", review_directory, name='review_directory'),
    path("create_directory/", create_directory, name='create_directory'),
    path("edit_directory/<str:id>/", edit_directory, name='edit_directory')
]