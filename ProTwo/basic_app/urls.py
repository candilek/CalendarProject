from django.urls import path
from . import views

app_name = 'basic_app'

urlpatterns = [
    path('',views.VisitorListView,name='visitor_list'),
    #path('<int:pk>/',views.VisitorDetailView.as_view(),name='visitor_detail'),
    path('visitor_create/',views.VisitorCreateView.as_view(),name='visitor_create'),
    path('visitor_update/<int:pk>/',views.VisitorUpdateView.as_view(),name='visitor_update'),
    path('<int:pk>/',views.VisitorDeleteView,name='visitor_delete'),

    path('appo_list/',views.AppointmentListView,name='appo_list'),
    path('appo_list/<int:pk>/',views.AppointmentDetailView.as_view(),name='appo_detail'),
    path('appo_create/',views.AppointmentCreateView.as_view(),name='appo_create'),
    path('appo_update/<int:pk>/',views.AppointmentUpdateView.as_view(),name='appo_update'),
    path('appo_delete/<int:pk>/',views.AppointmentDeleteView,name='appo_delete'),



]
