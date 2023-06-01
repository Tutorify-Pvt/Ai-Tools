from django.urls import path, include

urlpatterns = [
    path("user/", include('users.urls'), name='api_users'),
    path("directory/", include('directory.urls'), name='api_directory'),
    path("blog/", include('blogs.urls'), name='api_blogs')
]