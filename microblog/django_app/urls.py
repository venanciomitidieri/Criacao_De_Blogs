from django.conf.urls import include, url
from django.contrib import admin
from django_app import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^django_app/', include('django_app.urls')),
    url(r'^django_app/view/(?P<slug>[^\.]+).html', views.ver_post, name='ver_post_blog'),
    url(r'^django_app/categoria/(?P<slug>[^\.]+).html', views.ver_categoria, name='ver_categoria_blog'),
]