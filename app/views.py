from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import View 
from django.http import HttpResponse
from app.forms import *
# Create your views here.

#html page renderind using both fbv and cbv
def fbv_html(request):
    return render(request,'fbv_html.html')


class cbv_html(View):
    def get(self,request):
        return render(request,'cbv_html.html')
    
# http respose using both fbv adnd cbv
def fbv_response(request):
    return HttpResponse('this is the function base httpresponse')

class cbv_Response(View):
    def get(self,request):
        return HttpResponse('this is the class base httpresponse')
    

def fbv_form(request):
    TO=Topicform()
    d={'TO':TO}
    if request.method=='POST':
        TOD=Topicform(request.POST)
        if TOD.is_valid():
            TOD.save()
            return HttpResponse('data inserted ')
    return render(request,'fbv_form.html',d)


class cbv_form (View):
    def get(self,request):
        CT=Topicform()
        d1={'CT':CT}
        return render(request,'cbv_form.html',d1)
    def post(self,request):
        CTD=Topicform(request.POST)
        if CTD.is_valid():
            CTD.save()
            return HttpResponse('data is inserted is done...')
        



from django.views.generic import TemplateView
from app.forms import *

class cbv_template_view(TemplateView):
    template_name='cbv_template_view.html'
    def get_context_data(self, **kwargs: Any):
        co=super().get_context_data(**kwargs)
        co['name']='basha'
        co['age']='22'
        return co
    



class CBV_form_view(TemplateView):
    template_name='CBV_form_view.html'
    def get_context_data(self, **kwargs: Any):
         edfo=super().get_context_data(**kwargs)
         to=Topicform()
         edfo['to']=to
         return edfo
    def post(self,request):
        td=Topicform(request.POST)
        if td.is_valid():
            td.save() 
        return HttpResponse ('data is inserted')
    
    