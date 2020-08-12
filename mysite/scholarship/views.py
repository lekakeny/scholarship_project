from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseNotFound
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .forms import BioDataForm, SchoolForm, ReasonForm
from .models import Scholarship, Sponsor


# Create your views here.
def biodata(request):
    form = BioDataForm()
    context = {
        'form': form,
    }
    if request.method == "POST":
        User = get_user_model()
        form = BioDataForm(request.POST, request.FILES)
        if form.is_valid():
            # get the username fieild
            your_username = form.cleaned_data['your_username']
            your_firstname = form.cleaned_data['your_firstname']
            your_lastname = form.cleaned_data['your_lastname']
            password = form.cleaned_data['password']
            your_address = form.cleaned_data['your_address']
            your_mobile = form.cleaned_data['your_mobile']
            your_email = form.cleaned_data['your_email']
            your_birth = form.cleaned_data['your_birth']
            your_naid = form.cleaned_data['your_naid']
            s = User.objects.create_user(
                username=your_username,
                email=your_email,
                password=password
            )
            s.first_name = your_firstname
            s.last_name = your_lastname
            s.save()
            Scholarship.objects.create(
                user=s,
                contact1=your_email,
                contact2=your_mobile,
                birth=your_birth,
                naid=your_naid,
                address=your_address,
            )
            return redirect(reverse("schoolinfo"))
        return render(request, 'biodata.html', context={"form":form})

    return render(request, 'biodata.html', context=context)


@login_required
def schoolinfo(request):
    form = SchoolForm()
    context = {
        'form': form,
    }
    if request.method == "POST":
        form = SchoolForm(request.POST)
        if form.is_valid():
            school_name = form.cleaned_data['school_name']
            school_address = form.cleaned_data['school_address']
            academic_level = form.cleaned_data['academic_level']
            completion_year = form.cleaned_data['completion_year']
            # save the details to the instance object
            instance_object = Scholarship.objects.filter(
                user=request.user
            ).first()
            instance_object.school = school_name
            instance_object.school_address = school_address
            instance_object.level = academic_level
            instance_object.completion_year = completion_year
            instance_object.save()

            return redirect(reverse("submit"))
        return render(request, 'school.html', context={"form": form})
    return render(request, 'school.html', context=context)


@login_required
def reason(request):
    form = ReasonForm()
    context = {
        'form': form,
    }
    if request.method == "POST":
        form = ReasonForm(request.POST, request.FILES)
        if form.is_valid():
            sponsorship_reasons = form.cleaned_data['sponsorship_reasons']
            recommendation_letter = form.cleaned_data['recommendation_letter']
            # save the details to the instance object
            instance_object = Scholarship.objects.filter(
                user=request.user
            ).first()
            instance_object.reason = sponsorship_reasons
            instance_object.letter = recommendation_letter
            instance_object.save()
            return redirect(reverse("thank_you"))
        return render(request, 'reason.html', context={"form": form})
    return render(request, 'reason.html', context=context)


@login_required
def thank_you(request):
    return render(request, 'thank_you.html', context={})


@login_required
def list_scholarship(request):
    # Make sure that its a staff accessing this view
    if not request.user.is_staff:
        return redirect(reverse('login')+'?next='+request.path)
    qs = Scholarship.objects.filter(approved=False).all()
    return render(request, 'list.html', context={'qs': qs})


@login_required
def detail_scholarship(request, pk):
    # Make sure that its a staff accessing this view
    if not request.user.is_staff:
        return redirect(reverse('login') + '?next=' + request.path)
    object = get_object_or_404(Scholarship, pk=pk)
    return render(request, 'detail.html', context={'object': object})


@login_required
def approve(request, pk):
    if not request.user.is_staff:
        HttpResponseNotFound('<h1>Not Authorized</h1>')
    object = get_object_or_404(Scholarship, pk=pk)
    object.approved = True
    object.save()
    send_mail(
        'Approval for the scholarship',
        'You have been successfully approved',
        'from@example.com',
        [str(object.user.email)],
        fail_silently=True,
    )
    return redirect(reverse_lazy('successfully'))


def successfully(request):
    return render(request, 'success.html')


@login_required
def list_scholarship_for_sponsors(request):
    # Make sure that its a sponsor accessing this view
    s = Sponsor.objects.filter(user=request.user).first()
    # get_object_or_404(Sponsor, user=request.user)
    if s is None:
        return redirect(reverse('login') + '?next=' + request.path)
    qs = Scholarship.objects.filter(approved=True).filter(sponsored=False).all()
    return render(request, 'listsp.html', context={'qs': qs})


@login_required
def detail_scholarship_for_sponsors(request, pk):
    # Make sure that its a sponsor accessing this view
    s = Sponsor.objects.filter(user=request.user).first()
    # get_object_or_404(Sponsor, user=request.user)
    if s is None:
        return redirect(reverse('login') + '?next=' + request.path)
    object = get_object_or_404(Scholarship, pk=pk)
    return render(request, 'detailsp.html', context={'object': object})


@login_required
def approvesp(request, pk):
    s = Sponsor.objects.filter(user=request.user).first()
    if s is None:
        HttpResponseNotFound('<h1>Not Authorized</h1>')
    object = get_object_or_404(Scholarship, pk=pk)
    object.sponsored = True
    object.save()
    message = ('You have been successfully sponsored. Name of Sponsor: {name}, email address: {email}'.format(
        name=s.user.username, email=s.user.email))
    send_mail(
        'Sponsorship',
        message,
        'from@example.com',
        [str(object.user.email)],
        fail_silently=True,
    )
    return redirect(reverse_lazy('successfully'))
