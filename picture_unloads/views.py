from django.shortcuts import render
from django.views.generic import DetailView,ListView
from django.views.generic.edit import CreateView
from .models import IMG

class Showall(ListView):
    queryset = IMG.objects.all().order_by('-date_added')
    # ListView 默认 context_object_name = 'object_list'
    context_object_name = 'latest_picture_list'
    # 默认的 template_name = 'pic_upload/picture_list.html'
    template_name = 'img_tem/picture_list.html'
    
class Show(DetailView):
    model = IMG
    template_name = 'img_tem/picture_detail.html'
    
class Upload(CreateView):
    model = IMG
    fields = ['name', 'img']
    template_name = 'img_tem/picture_form.html'
