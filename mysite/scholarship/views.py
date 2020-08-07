from django.shortcuts import render
from .forms import BioDataForm, SchoolForm, ReasonForm


# Create your views here.
def biodata(request):
    context = {
        'form': BioDataForm(),
    }
    return render(request, 'biodata.html', context=context)


def schoolinfo(request):
    context = {
        'form': SchoolForm(),
    }
    return render(request, 'school.html', context=context)


def reason(request):
    context = {
        'form': ReasonForm(),
    }
    return render(request, 'reason.html', context=context)
