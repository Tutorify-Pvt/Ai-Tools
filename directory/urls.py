from django.urls import path
from .views import *
urlpatterns = [
    path("", list_directory, name='directory_view'),
    path("directory/get/<str:id>", get_directory, name='get_directory'),
    path("tag/get/<str:tag_id>", get_tags, name='get_tag'),
    path("type/get/<str:type_id>", get_type, name='get_type'),

    path("reviewing/", review_directory, name='review_directory'),
    path("create_directory/", create_directory, name='create_directory'),
    path("edit_directory/<str:id>/", edit_directory, name='edit_directory')
]