from django.contrib import admin
from . models import *


admin.site.register(ChemicalReport)
admin.site.register(IncidentType)
admin.site.register(PhysicalDescription)
admin.site.register(MedicalReport)
admin.site.register(FireReport)