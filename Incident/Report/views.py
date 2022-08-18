from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Report.models import ChemicalReport, MedicalReport, FireReport,ScReport
from . forms import ChemicalForm, FireForm, MedicalForm,ScForm 
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic import DetailView


def home_view(request):
    return render(request,'Report/home.html')

@login_required
def list_view(request):
    return render(request,'Report/incidentslist.html')

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

@login_required
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

@login_required
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

@login_required
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

@login_required
def report_create_sc(request):
    if request.method == 'POST':
        form = ScForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            report = form.save()
            
            return render(request,
                          'Report/sc_success.html',
                          {'report': report,
                           })
    else:
        form = ScForm()
    return render(request,
                  'Report/sc.html',
                  {'form': form})

class FireListView(ListView):
    model = FireReport

class ChemicalListView(ListView):
    model = ChemicalReport

class MedicalListView(ListView):
    model = MedicalReport

class ScListView(ListView):
    model = ScReport

class FireDetailView(DetailView):
    model = FireReport

class ChemicalDetailView(DetailView):
    model = ChemicalReport

class MedicalDetailView(DetailView):
    model = MedicalReport

class ScDetailView(DetailView):
    model = ScReport