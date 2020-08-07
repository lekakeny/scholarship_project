from django.shortcuts import render, redirect, reverse
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
            Scholarship.objects.create(
                contact1=your_email,
                contact2=your_mobile,
                birth=your_birth,
                naid=your_naid,
                address=your_address,
                names=your_name,
            )
        return redirect(reverse("schoolinfo"))

    return render(request, 'biodata.html', context=context)


def schoolinfo(request):
    form = SchoolForm()
    context = {
        'form': form,
    }
    if request.method == "POST":
        form = SchoolForm(request.POST, request.FILES)
        if form.is_valid():
            school_name = form.cleaned_data['school_name']
            school_address = form.cleaned_data['school_address']
            academic_level = form.cleaned_data['academic_level']
            completion_year = form.cleaned_data['completion_year']

            Scholarship.objects.create(
                school=school_name,
                address=school_address,
                level=academic_level,
                year=completion_year,
            )
            return redirect(reverse("reason"))
    return render(request, 'school.html', context=context)


def reason(request):
    form = ReasonForm()
    context = {
        'form': ReasonForm(),
    }
    if request.method == "POST":
        form = SchoolForm(request.POST, request.FILES)
        if form.is_valid():
            sponsorship_reasons = form.cleaned_data['sponsorship_reasons']
            recommendation_letter = form.cleaned_data['recommendation_letter']
            academic_level = form.cleaned_data['academic_level']
            completion_year = form.cleaned_data['completion_year']

            Scholarship.objects.create(
                reason=sponsorship_reasons,
                letter=recommendation_letter,
            )
            # return redirect(reverse("reason"))
    return render(request, 'reason.html', context=context)
