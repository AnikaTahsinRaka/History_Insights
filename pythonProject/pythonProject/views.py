# import signin as signin
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from . import models
from django.contrib.auth import update_session_auth_hash
from .forms import PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.urls import path, include, re_path
from django.urls import re_path as sign_in
# from django.contrib.auth import signin
from django.contrib.auth.models import User
from .models import Task, Review

from .models import Contact, HeritageDetails

import os
from django.conf import settings
from django.shortcuts import render
from django.templatetags.static import static




def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def make_plan(request):
    # task = Task.objects.all()
    # task = Task.objects.filter(user=request.user.id)
    # print(task)
    return render(request, 'make_plan.html')


0
def profile_page(request):
    return render(request, 'profile_page.html')



def reset_with_mail(request):
    return render(request, 'reset_with_mail.html')


def new_pass(request):
    return render(request, 'new_pass.html')




def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('/')
    return HttpResponse('handleLogout')


def handleContact_us(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        user_email = request.POST['user_email']
        user_message = request.POST['user_message']

        if len(fname) > 50:
            messages.error(request, "Name must be under 50 characters.")
            return redirect('/contact/')

        myuser = models.Contact(UserName=fname, Email=user_email, Message=user_message)
        myuser.save()
        messages.success(request, "Message successfully sent.")
        # return HttpResponse(request, "Your account has been successfully created")
        return redirect('/contact/')
    else:
        return HttpResponse('404 Not Found')





def handleTasks(request):

    if request.method == 'POST':
        title = request.POST['title']
        u = User.objects.filter(username=request.user)
        # print(request.user)
        myuser = models.Task(Title=title, user=u[0])
        myuser.save()
        return redirect('/')

        # if myuser is not None:
        #     messages.success(request, "Tasks successfully save.")
        #     return redirect('/')
        # else:
        #     messages.error(request, "Something not matching.")
        #     return redirect('/')




def password_success(request):
    return render(request, "home.html")


def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
    else:
        return HttpResponse('404 Not Found')


def password_change_done(request):
    return redirect('/')


def handleProfile(request):
    if request.method == 'POST':
        # username = user.username
        full_name = request.POST['full_name']
        date_of_birth = request.POST['date_of_birth']
        gender = request.POST['gender']

        if len(full_name) > 50:
            messages.error(request, "Name must be under 50 characters.")
            return redirect('/profile_page/')

        my_user = models.Contact(full_name=full_name, birth_date=date_of_birth, GENRE_CHOICES=gender)
        my_user.save()
        messages.success(request, "Message successfully sent.")
        # return HttpResponse(request, "Your account has been successfully created")
        return redirect('/profile_page/')
    else:
        return HttpResponse('404 Not Found')





     




