from django.shortcuts import render,HttpResponse,redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.urls import reverse_lazy,reverse
from django.http import HttpResponse
from . import models #aynı klasörün altında olduğu için . import models dedik.
from basic_app.forms import AppointmentForm,VisitorForm
from django.views.generic import (View,TemplateView,
                                 CreateView,UpdateView,
                                 ListView,DeleteView,
                                 DetailView )
# Create your views here.
class IndexView(TemplateView):#IndexView classını TemplateView classı ile genişlettik
    template_name = 'index.html'

def VisitorListView(request): #okul modelinde yer alan tüm okulları listeler
    context_object_name = 'visitor_details' # orijinal parametre adını (object_list) "context_object_name" ile başka bir şekilde adlandırabiliriz.
    model = models.Visitor
    visit_list = model.objects.all()
    paginator = Paginator(visit_list, 4) # Show 5 contacts per page
    page = request.GET.get('page')
    visitor_details = paginator.get_page(page)
    return render(request, 'basic_app/visitor_list.html', {'visitor_details': visitor_details})


class VisitorDetailView(DetailView): #okul veritabanında bulunan bir girdinin tüm detaylarını listelemesi için
    context_object_name = 'visitor_details'   #html sayfasında bu isimle çağıracağız.
    model = models.Visitor
    template_name = 'basic_app/visitor_detail.html'

class VisitorCreateView(CreateView):
    form_class = VisitorForm
    model = models.Visitor

class VisitorUpdateView(UpdateView):
    form_class = VisitorForm
    model = models.Visitor

def  VisitorDeleteView(request, pk):
    model = models.Visitor
    visitor_details = model.objects.get(pk=pk)
    visitor_details.delete()
    return redirect('/basic_app/')



def  AppointmentListView(request):
    context_object_name = 'appointments'
    model = models.Appointment
    app_list = model.objects.all()
    paginator = Paginator(app_list, 4) # Show 5 contacts per page
    page = request.GET.get('page')
    appointments = paginator.get_page(page)
    return render(request, 'basic_app/appo_list.html', {'appointments': appointments})


class AppointmentDetailView(DetailView):
    context_object_name = 'appo_details'
    model = models.Appointment
    template_name = 'basic_app/appo_detail.html'

class AppointmentCreateView(CreateView):

    form_class = AppointmentForm
    model = models.Appointment

class AppointmentUpdateView(UpdateView):

    form_class = AppointmentForm
    model = models.Appointment

def AppointmentDeleteView(request, pk):
   model = models.Appointment
   appo_details = model.objects.get(pk=pk)
   appo_details.delete()
   return redirect('/basic_app/appo_list')
