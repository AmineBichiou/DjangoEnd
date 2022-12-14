from django.shortcuts import HttpResponseRedirect, render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from cv.models import Internships, Language, Skills,diploma

def index(request):
    template = loader.get_template('Info.html')
    context = {
    'Name': 'Amine Bichiou',
    'work': 'Apps Developer, Front end Developer',
    'Birthday': '15 July 2002',
    'email': 'aminebichiou2@gmail.com',
    'Phone': 20319318,
    'adresse': 'Hammamet',
    'freelance':'Available',
    'Experience': 'none',
    'Degree':'licence',
    'Hobbies':['Handball','Watching Movies','Playing video games','Programming'],
    'Description':'I am a student in the second year of the license in computer science at the University of Nabeul, I am 20 years old, I am a hard worker and I am looking for an internship in the field of Web development.',
    }
    return HttpResponse(template.render(context, request))
def skills(request):
    l = Language.objects.all().values()
    s = Skills.objects.all().values()
    template = loader.get_template('Skills.html')
    context = {
    's': s,
    'l':l,
    }
    return HttpResponse(template.render(context, request))
def iploma(request):
    d = diploma.objects.all().values()
    template = loader.get_template('Diploma.html')
    context = {
    'd': d,
    }
    return HttpResponse(template.render(context, request))
def internship(request):
    i = Internships.objects.all().values()
    template = loader.get_template('Internships.html')
    context = {
    'i': i,
    }
    return HttpResponse(template.render(context, request))
def change(request):
    l = Language.objects.all().values()
    s = Skills.objects.all().values()
    template = loader.get_template('Change.html')
    context = {   
    's': s,
    'l':l,
    }
    return HttpResponse(template.render(context, request))
def quali(request):
    i = Internships.objects.all().values()
    d = diploma.objects.all().values()
    template = loader.get_template('quali.html')
    context = {
    'd': d,   
    'i': i,
    }
    return HttpResponse(template.render(context, request))
def del_s(request, id):
    s = Skills.objects.get(id=id)
    s.delete()
    return HttpResponseRedirect(reverse('change'))
def del_i(request, id):
    i = Internships.objects.get(id=id)
    i.delete()
    return HttpResponseRedirect(reverse('quali'))
def del_d(request, id):
    d = diploma.objects.get(id=id)
    d.delete()
    return HttpResponseRedirect(reverse('quali'))
def update_s(request, id):
    s = Skills.objects.get(id=id)
    l = Language.objects.all().values()
    template = loader.get_template('updateSkills.html')
    context = {
    's': s,
    'l':l, 
    }
    return HttpResponse(template.render(context, request))
def update_s_action(request, id):
    n = request.POST['nom']
    ni = request.POST['niveau']
    f = request.POST['formation']
    l = request.POST['language']
    s = Skills.objects.get(id=id)
    l = Language.objects.get(id=l)
    s.nom = n
    s.niveau = ni
    s.formation = f
    s.language = l
    s.save()
    return HttpResponseRedirect(reverse('change'))
def update_i(request, id):
    i = Internships.objects.get(id=id)
    template = loader.get_template('updateInt.html')
    context = {
    'i': i,
    }
    return HttpResponse(template.render(context, request))
def update_i_action(request, id):
    n = request.POST['namesociete']
    p = request.POST['projet']
    i= Internships.objects.get(id=id)
    i.namesociete = n
    i.projet = p
    i.save()
    return HttpResponseRedirect(reverse('quali'))
def update_d(request, id):
    d = diploma.objects.get(id=id)
    template = loader.get_template('updateDi.html')
    context = {
    'd': d,
    }
    return HttpResponse(template.render(context, request))
def update_d_action(request, id):
    me1 = request.POST['me1']
    me2 = request.POST['me2']
    d= diploma.objects.get(id=id)
    d.MyEducation = me1
    d.MyExperience = me2
    d.save()
    return HttpResponseRedirect(reverse('quali'))
def adds(request):
    l = Language.objects.all().values()
    template = loader.get_template('addS.html')
    context = {
    'l': l,
    }
    return HttpResponse(template.render(context, request))
def add_s(request):
    n = request.POST['nom']
    ni = request.POST['niveau']
    f = request.POST['formation']
    l = request.POST['language']
    d = request.POST['dateS']
    l = Language.objects.get(id=l)
    s = Skills(nom=n, niveau=ni, formation=f,language=l,dateS=d)
    s.save()
    return HttpResponseRedirect(reverse('change'))
def addi(request):
    i = Internships.objects.all().values()
    template = loader.get_template('addI.html')
    context = {
    'i': i,
    }
    return HttpResponse(template.render(context, request))
def add_i(request):
    n = request.POST['namesociete']
    p = request.POST['projet']
    d = request.POST['dateI']
    i= Internships(namesociete=n, projet=p, dateI=d)
    i.save()
    return HttpResponseRedirect(reverse('quali'))
def addd(request):
    d = diploma.objects.all().values()
    template = loader.get_template('addD.html')
    context = {
    'd': d,
    }
    return HttpResponse(template.render(context, request))
def add_d(request):
    me1 = request.POST['me1']
    me2 = request.POST['me2']
    d = request.POST['dateD']
    d= diploma(MyEducation=me1, MyExperience=me2, dateD=d)
    d.save()
    return HttpResponseRedirect(reverse('quali'))


