from django.urls import path,include
from . import views

urlpatterns = [
    
    path('medicines/',views.medicines,name='medicines'),
    path('medicinedetails/<int:prodid>',views.medicinedetails, name='medicinedetails'),

]