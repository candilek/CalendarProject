from django.db import models
from django.urls import reverse

# Create your models here.
class  Visitor(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=254,unique=True)
    company = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self): # Güncelleme formunu gönderdikten sonra sayfa tekrar list sayfasına yönlendirilecek
        return reverse('basic_app:visitor_update',kwargs={'pk':self.pk}) #----basic_app:visitor_list yazınca hata alıyorum


class Appointment(models.Model): #randevu modeli
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()     #örnek 2006-10-25 14:30 şeklinnde olucak
    subject = models.TextField()
    name = models.ForeignKey('basic_app.Visitor',on_delete= models.CASCADE) #Visitor modeline bağladım.

    def __str__(self):
        return self.name

    def get_absolute_url(self): # Güncelleme formunu gönderdikten sonra sayfa tekrar detail sayfasına yönlendirilecek
        return reverse("basic_app:appo_detail",kwargs={'pk':self.pk})
