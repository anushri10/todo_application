"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
#from django.contrib.auth import views as auth_views
from assignment import views
from django.contrib import admin
import os.path

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.main_page),
    url(r'^signup$', views.signup),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^add-todo$', views.add_todo),
    url(r'^edit-todo/(?P<todo_id>\d+)$', views.edit_todo),
    url(r'^delete-todo/(?P<todo_id>\d+)$', views.delete_todo),
    url('^', include('django.contrib.auth.urls')),
    url(r'^accounts/login/$',views.login),
    url(r'^email-todo$',views.email_todo),
]

