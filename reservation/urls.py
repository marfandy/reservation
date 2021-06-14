from django.contrib import admin
from django.urls import path,include

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',include(('home.urls', 'home'), namespace='home')),
    path('',views.index, name="index"),
    path('logout',views.getlogout, name="logout"),

]
