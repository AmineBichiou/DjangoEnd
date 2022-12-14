from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from config.forms import FormConnexion
from django.contrib.auth import authenticate, login, logout

from config.forms import FormConnexion
def test(request):
 template = loader.get_template('test.html')
 return HttpResponse(template.render())
def connect (request):
 connect_form = FormConnexion()
 return render(request, 'connexion.html', {'connect_form' :connect_form,'error':False}) 
def signIn(request):
 username = request.POST['login']
 password = request.POST['mot2pass']
 user = authenticate(request, username=username,password=password)
 if user is not None:
    login(request, user)
    request.session['username'] = username
    return HttpResponseRedirect(reverse('change'))
 else:
    connect_form = FormConnexion()
    print("Login et/ou mot de passe incorrect")
    return render(request,'connexion.html',{'connect_form' :connect_form,'error':True})
 #return HttpResponseRedirect(reverse('connect')) 
def signOut(request):
 logout(request)
 return HttpResponseRedirect(reverse('connect'))
