from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PatientRegisterForm, PatientUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = PatientRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. You can now login.')
            return redirect('login')
    else:
        form = PatientRegisterForm()
    return render(request, 'patient/register.html', {'form': form})


@login_required
def patient(request):
    return render(request, 'patient/patientportal.html')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = PatientUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('profile')

    else:
        u_form = PatientUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'patient/profile.html', context)
