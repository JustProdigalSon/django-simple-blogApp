from django.contrib import admin
from django.urls import path
from blog.views import frontpage, post_detail,temp
urlpatterns = [
    path('admin', admin.site.urls),
    path('', frontpage, name='frontpage'),
    path('temp', temp, name='temp'),
    path('<slug:slug>', post_detail, name='post_detail'),
]