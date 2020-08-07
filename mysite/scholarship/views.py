from django.shortcuts import render
from .forms import BioDataForm, SchoolForm, ReasonForm
from .models import Scholarship


# Create your views here.
def biodata(request):
    form = BioDataForm()
    context = {
        'form': form,
    }
    if request.method == "POST":
        form = BioDataForm(request.POST, request.FILES)
        if form.is_valid():
            your_name = form.cleaned_data['your_name']
            your_address = form.cleaned_data['your_address']
            your_mobile = form.cleaned_data['your_mobile']
            your_email = form.cleaned_data['your_email']
            your_birth = form.cleaned_data['your_birth']
            your_naid = form.cleaned_data['your_naid']
            print(request.user)
            # Scholarship.object.create(
            #     user=request.user
            # )


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
