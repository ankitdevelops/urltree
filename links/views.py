from django.http import request
from django.shortcuts import redirect, render
from . forms import *
from . models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    all_links = Link.objects.filter(user = request.user)
    links = Link(user = request.user)
    link_form = LinkForm()
    if request.method == 'POST':
        link_form = LinkForm(request.POST, instance=links)
        if link_form.is_valid():
            link_form.save()
            return redirect('dashboard')
    else:
        link_form = LinkForm()
    data = {
        'link_form':link_form,
        'all_links':all_links,
    }
    return render(request, 'dashboard.html', data)


@login_required(login_url='login')
def link_edit(request,id):
    links = Link.objects.get(id = id)
    edit_form = LinkForm(instance=links)
    if request.method == 'POST':
        edit_form = LinkForm(request.POST, instance=links)
        if edit_form.is_valid():
            edit_form.save()
        return redirect('dashboard')

    data = {
        'edit_form':edit_form,
    }
    return render(request, 'link_edit.html', data)

@login_required(login_url='login')
def delete_link(request, id):
    links = Link.objects.get(id = id)
    if request.method == 'POST':
        links.delete()
        return redirect('dashboard')
    data = {
        'links':links,
    }
    return render(request, 'delete_link.html', data)


def user_link(request,username):
   user = User.objects.get(username= username)
   user_link = Link.objects.filter(user = user)
  
   data = {
       'user_link':user_link,
       'user':user,
   }
   return render(request, 'base.html', data)

