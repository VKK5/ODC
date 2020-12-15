from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.Location_list_view,name="Location_list_view"),
    path('Location/<slug:slug>',views.Location_detail_view, name="Location_detail_view"),
   
]