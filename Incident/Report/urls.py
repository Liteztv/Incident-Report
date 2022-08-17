from django.urls import path
from . import views
from .views import (FireDetailView, FireListView,ChemicalListView,
                    MedicalListView,ChemicalDetailView,ScListView,
                    MedicalDetailView)

urlpatterns = [
    path('',views.home_view),
    path('Fire',views.report_create_fire, name='Fire'),
    path('Medical',views.report_create_medical, name='Medical'),
    path('Chemical',views.report_create_chemical, name='Chemical'),
    path('Sc',views.report_create_sc, name='Sc'),
    path('fire_list',FireListView.as_view(),name='fire_list'),
    path('chemical_list',ChemicalListView.as_view(),name='chemical_list'),
    path('sc_list',ScListView.as_view(),name='sc_list'),
    path('medical_list',MedicalListView.as_view(),name='medical_list'),
    path('Lists',views.list_view, name='Lists'),
    path('firereport_detail/<int:pk>',FireDetailView.as_view(),name='firereport_detail'),
    path('chemicalreport_detail/<int:pk>',ChemicalDetailView.as_view(),name='chemicalreport_detail'),
    path('medicalreport_detail/<int:pk>',MedicalDetailView.as_view(),name='medicalreport_detail')
]