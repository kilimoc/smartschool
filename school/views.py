from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import SchoolForm


class HomePage(TemplateView):
    template_name = 'school/home.html'
def registerSchool(request):
    if request.method=='POST':
        form=SchoolForm(request.POST)
        if form.is_valid():
            school_name = form.cleaned_data['school_name']
            reg_number = form.cleaned_data['reg_number']
            teacher_no = form.cleaned_data['teacher_no']

    else:
        form=SchoolForm()
    return render(request,'school/register_school.html',{'form':form})





