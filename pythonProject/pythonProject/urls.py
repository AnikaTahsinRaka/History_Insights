"""pythonProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import to include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
# from .views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import path, reverse_lazy

from django.conf import settings
from django.conf.urls.static import static


from .views import password_change

urlpatterns = [
<<<<<<< HEAD
    path('', views.home, name='home'),
     path('review/', views.review, name='review'),
    path('review', views.handleReview, name='handleReview'),
    path('signup', views.handleSignup, name='handleSignup'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('signin', views.handleSignin, name='handleSignin'),
=======

    
    
   
    
>>>>>>> eafb169c58c80899aead9d37808153ef969eb0da
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('make_plan/', views.make_plan, name='make_plan'),
    path('contact_us', views.handleContact_us, name='handleContact_us'),
    path('reset_with_mail/', views.reset_with_mail, name='reset_with_mail'),
    path('profile_page/', views.profile_page, name='profile_page'),
    path('logout', views.handleLogout, name='handleLogout'),
    # path('new_pass/', views.new_pass, name='new_pass'),
    path('password_change', views.PasswordChangeView.as_view(template_name="registration/password_change_form.html"),
         name='password_change'),
    # path('password_change_done', views.PasswordChangeDoneView.as_view(template_name="registration/password_change_done.html"), name='password_change_done'),
    path('password_change_done', PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
         name='password_change_done'),
    path('tasks/', views.handleTasks, name='handleTasks'),
    path('heritage/', views.heritage, name='heritage'),
    path('list_of_sights/', views.list_of_sights, name='list_of_sights'),
    path('ahsan_manjil/', views.ahsan_manjil, name='ahsan_manjil'),
    path('lalbagh_fort/', views.lalbagh_fort, name='lalbagh_fort'),
    path('star_mosque/', views.star_mosque, name='star_mosque'),
    path('ramakrishna_mission_temple/', views.ramakrishna_mission_temple, name='ramakrishna_mission_temple'),
    path('searchbar/', views.searchbarr, name='searchbar'),
    path('places/', views.places, name='places'),
    path('information', views.handleInformation, name='handleInformation'),
    path('heritageNew/', views.heritageNew, name='heritageNew'),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
