from django.db import models
from django.contrib.auth.models import User
from sympy import ordered

class YesNo(models.Model):
    bool = models.CharField(max_length=10,blank=True, null=True)

    def __str__(self):
        return self.bool

class IncidentType(models.Model):
    type = models.CharField(max_length=100)
    description = models.CharField(max_length=140,blank=True, null=True)

    def __str__(self):
        return self.type
class PhysicalDescription(models.Model):
    state = models.CharField(max_length=100)    
    other = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.state

class FireReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='FireCreator')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    date_and_time_of_incident_start = models.DateTimeField()
    date_and_time_of_incident_end = models.DateTimeField()
    incident_commander = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='FireCommander')
    incident_type = models.ForeignKey(IncidentType, on_delete=models.SET_NULL, null=True)
    cause_of_incident = models.CharField(max_length=140)
    actions_taken = models.TextField()
    Test = models.BooleanField(null=True, blank=True)
    equipment_used = models.TextField()
    debrief_attendance = models.TextField()
    positive_notes = models.TextField()
    areas_of_improvement = models.TextField()
    debrief_commander = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,related_name='FireDebriefCommander')
    debrief_date_time = models.DateTimeField()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.user} reported {self.incident_type} on {self.created} .'


class MedicalReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='MedicalCreator')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    date_and_time_of_incident_start = models.DateTimeField()
    date_and_time_of_incident_end = models.DateTimeField()
    incident_commander = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='MedicalCommander')
    incident_type = models.ForeignKey(IncidentType, on_delete=models.SET_NULL, null=True)
    cause_of_incident = models.TextField()
    actions_taken = models.TextField()
    equipment_used = models.TextField()
    patient_name = models.CharField(max_length=300)
    patient_age = models.CharField(max_length=3)
    legal_gender = models.CharField(max_length=10)
    patient_address = models.CharField(max_length=300) 
    patient_phone_number = models.CharField(max_length=15)
    emergency_contact = models.CharField(max_length=100)
    level_of_conciousness = models.CharField(max_length=2)
    loss_of_consciousness = models.ForeignKey(YesNo, on_delete=models.SET_NULL, null=True, related_name='LossOfConsciousness')
    symptoms = models.TextField()
    chief_complaint = models.CharField(max_length=100)
    what_happened = models.TextField()
    prexisting_condition = models.ForeignKey(YesNo, on_delete=models.SET_NULL, null=True, related_name='PrexistingCondition')
    last_time_patient_ate = models.CharField(max_length=30)
    drug_allergies = models.TextField()
    skin_color_and_temp = models.TextField()
    eyes_perl = models.CharField(max_length=20)
    respirations = models.CharField(max_length=50)
    ambulance_called = models.ForeignKey(YesNo, on_delete=models.SET_NULL, null=True, related_name='AmbulanceCalled')
    hospital = models.CharField(max_length=50)
    employee_refused_treatment = models.ForeignKey(YesNo, on_delete=models.SET_NULL, null=True, related_name='EmployeeRefusedTreatment')
    first_aid_providers_name = models.CharField(max_length=50)
    debrief_attendance = models.TextField()
    positive_notes = models.TextField()
    areas_of_improvement = models.TextField()
    debrief_commander = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,related_name='MedicalDebriefCommander')
    debrief_date_time = models.DateTimeField()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.user} on {self.created} . {self.incident_type}.'

class ChemicalReport(models.Model):
    

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='ChemicalCreator')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    date_and_time_of_incident_start = models.DateTimeField()
    date_and_time_of_incident_end = models.DateTimeField()
    incident_commander = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='ChemicalCommander')
    incident_type = models.ForeignKey(IncidentType, on_delete=models.SET_NULL, null=True)
    cause_of_incident = models.TextField()
    actions_taken = models.TextField()
    equipment_used = models.TextField()
    identify_substance = models.TextField()
    physical_description = models.ForeignKey(PhysicalDescription, on_delete=models.SET_NULL, null=True )
    material_run_off_property = models.ForeignKey(YesNo, on_delete=models.SET_NULL, null=True, related_name='RunOff')
    agencies_notified = models.ForeignKey(YesNo, on_delete=models.SET_NULL, null=True, related_name='AgenciesNotified')
    Environment_affected = models.ForeignKey(YesNo, on_delete=models.SET_NULL, null=True, related_name='EnvironmentAffected')
    employee_chemical_exposure = models.ForeignKey(YesNo, on_delete=models.SET_NULL, null=True, related_name='EmployeeChemicalExposure')
    employee_injured = models.ForeignKey(YesNo, on_delete=models.SET_NULL, null=True, related_name='EmployeeInjured')
    employee_phone_number = models.CharField(max_length=15)
    public_chemical_exposure = models.ForeignKey(YesNo, on_delete=models.SET_NULL, null=True, related_name='PublicChemicalExposure')
    public_injured = models.ForeignKey(YesNo, on_delete=models.SET_NULL, null=True, related_name='PublicInjured')
    debrief_attendance = models.TextField()
    positive_notes = models.TextField()
    areas_of_improvement = models.TextField()
    debrief_commander = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,related_name='ChemicalDebriefCommander')
    debrief_date_time = models.DateTimeField()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.user} on {self.created} . {self.incident_type}.'

class ScReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='SecurityCreator')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    date_and_time_of_incident_start = models.DateTimeField()
    date_and_time_of_incident_end = models.DateTimeField()
    incident_commander = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='SecurityCommander')
    incident_type = models.ForeignKey(IncidentType, on_delete=models.SET_NULL, null=True)
    cause_of_incident = models.TextField()
    actions_taken = models.TextField()
    equipment_used = models.TextField()
    debrief_attendance = models.TextField()
    positive_notes = models.TextField()
    areas_of_improvement = models.TextField()
    debrief_commander = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,related_name='SecurityDebriefCommander')
    debrief_date_time = models.DateTimeField()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.user} on {self.created} . {self.incident_type}.'
    

# class GeneralReport(models.Model):

#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='Creator')
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     date_of_incident = models.DateTimeField()
#     incident_commander = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='Commander')
#     incident_type = models.ForeignKey(IncidentType, on_delete=models.SET_NULL, null=True, help_text='IF OTHER PROVIDE DESCRIPTION')
#     cause_of_incident = models.TextField()
#     actions_taken = models.TextField()
#     equipment_used = models.TextField()
#     debrief_attendance = models.TextField()
#     positive_notes = models.TextField()
#     areas_of_improvement = models.TextField()
#     debrief_commander = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,related_name='Debrief Commander')
#     debrief_date_time = models.DateTimeField()