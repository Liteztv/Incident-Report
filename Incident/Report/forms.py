from django import forms
from matplotlib import widgets
from . models import ChemicalReport, FireReport, MedicalReport

class DateInput(forms.DateTimeInput):
    input_type = 'datetime-local'



class ChemicalForm(forms.ModelForm):
    class Meta:
        model = ChemicalReport
        exclude = [
            'user', 'created', 'updated'         
            ]
        widgets = {'date_and_time_of_incident_start': DateInput(),
                    'date_and_time_of_incident_end': DateInput(),
                    'debrief_date_time': DateInput()
        }


class FireForm(forms.ModelForm):
    class Meta:
        model = FireReport
        exclude = [
            'user', 'created', 'updated'         
            ]
        widgets = {'date_and_time_of_incident_start': DateInput(),
                    'date_and_time_of_incident_end': DateInput(),
                    'debrief_date_time': DateInput()
        }


class MedicalForm(forms.ModelForm):
    class Meta:
        model = MedicalReport
        exclude = [
            'user', 'created', 'updated'         
            ]
        widgets = {'date_and_time_of_incident_start': DateInput(),
                    'date_and_time_of_incident_end': DateInput(),
                    'debrief_date_time': DateInput()
        }


class SecureForm(forms.ModelForm):
    class Meta:
        model = MedicalReport
        exclude = [
            'user', 'created', 'updated'         
            ]
        widgets = {'date_and_time_of_incident_start': DateInput(),
                    'date_and_time_of_incident_end': DateInput(),
                    'debrief_date_time': DateInput()
        }