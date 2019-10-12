from django.urls import path
from Seryigram import views
from posts import views as ex

urlpatterns = [
    path('hello/', views.hello),
    path('hi/', views.hi),
    path('hi2/<str:name>/<int:age>', views.hi2),
    path('posts/', ex.list_posts)
]
