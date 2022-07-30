from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view),
    path('Fire',views.report_create_fire, name='Fire'),
    path('Medical',views.report_create_medical, name='Medical'),
    path('Chemical',views.report_create_chemical, name='Chemical')
]