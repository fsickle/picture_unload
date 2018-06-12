'''定义 picture_unloads 的 urls'''
from django.urls import path, re_path
from . import views

app_name='picture_unloads'
urlpatterns = [
    # 显示所有图片
    path('',views.Showall.as_view(),name='showall'),
    re_path(r'^picture/unload/$', views.Upload.as_view(), name='upload'),
    re_path(r'^picture/(?P<pk>\d+)$',views.Show.as_view(), name='show'),
]    

