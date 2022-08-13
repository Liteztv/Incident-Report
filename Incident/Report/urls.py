from django.urls import path
from . import views
from .views import (FireDetailView, FireListView,ChemicalListView,
                    MedicalListView,SecureListView,ChemicalDetailView)

urlpatterns = [
    path('',views.home_view),
    path('Fire',views.report_create_fire, name='Fire'),
    path('Medical',views.report_create_medical, name='Medical'),
    path('Chemical',views.report_create_chemical, name='Chemical'),
    path('Secure',views.report_create_secure, name='Secure'),
    path('fire_list',FireListView.as_view(),name='fire_list'),
    path('chemical_list',ChemicalListView.as_view(),name='chemical_list'),
    path('medical_list',MedicalListView.as_view(),name='medical_list'),
    path('Lists',views.list_view, name='Lists'),
    path('secure_list',SecureListView.as_view(),name='secure_list'),
    path('firereport_detail/<int:pk>',FireDetailView.as_view(),name='firereport_detail'),
    path('chemicalreport_detail/<int:pk>',ChemicalDetailView.as_view(),name='chemicalreport_detail')
]