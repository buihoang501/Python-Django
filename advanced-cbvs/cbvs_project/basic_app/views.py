from django.shortcuts import render

from django.views.generic import View,TemplateView

class IndexView(TemplateView):
    template_name ='index.html'

    #get context data func
     
    #. The super() function is used to give access to methods and properties of a parent or sibling class
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hello_str'] ='Hello Developers XD~'
        return context

