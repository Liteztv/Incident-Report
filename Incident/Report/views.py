from django.shortcuts import render
from Report.models import ChemicalReport, MedicalReport, FireReport
from . forms import ChemicalForm, FireForm, MedicalForm, SecureForm 
from django.views.generic.edit import FormView


def home_view(request):
    return render(request,'/Report/home.html')

# # def fires_view(request):
# #     return render(request,'Report/fire.html')

# def medical_view(request):
#     return render(request,'Report/medical.html')    

# # def chemical_view(request):
# #     return render(request,'Report/chemical.html')        

# def success_view(request):
#     return render(request,'Report/chemical_success.html')

# class ChemicalFormView(FormView):
#     template_name = 'Report/chemical.html'
#     form_class = ChemicalForm
#     success_url = 'chemical_success' 
    
#     def form_valid(self, form):
#         user= request.user
#         form.save()
#         return super(ChemicalFormView, self).form_valid(form)


def report_create_chemical(request):
    if request.method == 'POST':
        form = ChemicalForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            report = form.save()
            
            return render(request,
                          'Report/chemical_success.html',
                          {'report': report,
                           })
    else:
        form = ChemicalForm()
    return render(request,
                  'Report/chemical.html',
                  {'form': form})

def report_create_fire(request):
    if request.method == 'POST':
        form = FireForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            report = form.save()
            
            return render(request,
                          'Report/fire_success.html',
                          {'report': report,
                           })
    else:
        form = FireForm()
    return render(request,
                  'Report/fire.html',
                  {'form': form})        


def report_create_medical(request):
    if request.method == 'POST':
        form = MedicalForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            report = form.save()
            
            return render(request,
                          'Report/medical_success.html',
                          {'report': report,
                           })
    else:
        form = MedicalForm()
    return render(request,
                  'Report/medical.html',
                  {'form': form})  




def report_create_secure(request):
    if request.method == 'POST':
        form = SecureForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            report = form.save()
            
            return render(request,
                          'Report/secure_success.html',
                          {'report': report,
                           })
    else:
        form = SecureForm()
    return render(request,
                  'Report/secure.html',
                  {'form': form})