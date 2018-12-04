from django import forms
from .models import Visitor, Appointment


class VisitorForm(forms.ModelForm):

    class Meta:
        model = Visitor
        fields = ('name','email', 'company')

class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ('start_date','end_date', 'subject','name')
