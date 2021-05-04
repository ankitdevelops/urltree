from django.shortcuts import redirect, render
from django.core.exceptions import ValidationError
from . forms import *
from django.contrib.auth import logout
# Create your views here.


def register(request):
    if request.method == 'POST':
        forms = UserRegisterForm(request.POST)
        
        if forms.is_valid():
            username = forms.cleaned_data.get('username')
            first_name = forms.cleaned_data.get('first_name')
            last_name = forms.cleaned_data.get('last_name')
            email = forms.cleaned_data.get('email')
            password = forms.cleaned_data.get('forms')
            if User.objects.filter(email=email).exists():
                raise ValidationError("Email exists")
            else:
                forms.save()
            return redirect('login')
    else:
        forms = UserRegisterForm()
    return render(request, 'accounts/register.html', {'forms':forms})
            

def login(request):
    pass


def profile(request):
    current_user = request.user
    if request.method == 'POST':
        profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        user_form = UserUpdateForm(request.POST,instance=request.user)
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            return redirect('profile')
    else:
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        user_form = UserUpdateForm(instance=request.user)

    data = {
        'profile_form':profile_form,
        'user_form':user_form,
    }

    return render(request, 'accounts/profile.html', data)

def logout_user(request):
    logout(request) 
    return redirect('login')