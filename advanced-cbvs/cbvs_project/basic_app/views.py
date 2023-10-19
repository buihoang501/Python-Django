from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView, UpdateView, DeleteView
from . import models




class IndexView(TemplateView):
    template_name ='index.html'

    #get context data func
     
    #. The super() function is used to give access to methods and properties of a parent or sibling class
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hello_str'] ='Hello Developers XD~'
        return context

class SchoolListView(ListView):
    #return a school_list
    context_object_name = 'schools' # instead of school_list => schools is the name of list
    model = models.School
    template_name = 'basic_app/school_list.html'

class SchoolDetailView(DetailView):
    #return a school_detail
    #edit name
    context_object_name ='school_detail' 
    model = models.School
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields =('name','principal','location')
    model = models.School
    template_name = 'basic_app/school_form.html'
class SchoolUpdateView(UpdateView):
    #only update name and principal
    fields = ('name','principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    #
    success_url = reverse_lazy("basic_app:list")
    template_name ='basic_app/school_conform_delete.html'