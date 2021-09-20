from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PatientRegisterForm


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
