from django.shortcuts import render,HttpResponseRedirect,reverse
from bug_tracker.models import Tracker, Ticket
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from bug_tracker.form import signinform, createticketform

# Create your views here.
def loginuser(request):
    if request.method == "POST":
        Form = signinform(request.POST)
        if Form.is_valid():
            data = Form.cleaned_data
            user = authenticate(request, username=data['username'],password=data['password'])
            if user:
                login(request,user)
                return HttpResponseRedirect(request.GET.get('next',reverse('homepage')))
    Form = signinform()
    return render(request,'form.html',{'Form': Form})

def logoutuser(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))

@login_required
def index(request):
    data = Ticket.objects.all().order_by('-time')
    return render(request,'index.html',{'data':data})

@login_required
def createticket(request,userid):
    if request.method == "POST":
        Form = createticketform(request.POST)
        if Form.is_valid():
            data = Form.cleaned_data
            user = Tracker.objects.get(id=userid)
            Ticket.objects.create(
                title=data['title'],
                description=data['description'],
                usersubmited=user
            )
            return HttpResponseRedirect(reverse('homepage'))
    Form = createticketform()
    return render(request,'form.html', {"Form": Form})

@login_required
def ticketdetail(request,ticketid):
    data = Ticket.objects.get(id=ticketid)
    return render(request,'ticket.html', {'data':data})

@login_required
def doticket(request,ticketid,userid):
    data= Ticket.objects.get(id=ticketid)
    user = Tracker.objects.get(id=userid)
    data.userassigned = user
    data.status = "P"
    data.save()
    return HttpResponseRedirect(reverse('detailpage',args=(ticketid,)))

@login_required
def ticketdone(request,ticketid,userid):
    data= Ticket.objects.get(id=ticketid)
    user = Tracker.objects.get(id=userid)
    data.status = "D"
    data.usercompleted = user
    data.save()
    return HttpResponseRedirect(reverse('detailpage',args=(ticketid,)))

@login_required
def invalidticket(request,ticketid,userid):
    data = Ticket.objects.get(id=ticketid)
    user = Tracker.objects.get(id=userid)
    data.status = "I"
    data.usercompleted = user
    data.save()
    return HttpResponseRedirect(reverse('detailpage', args=(ticketid,)))

@login_required
def editticket(request,ticketid):
    ticket = Ticket.objects.get(id=ticketid)
    if request.method == "POST":
        form = createticketform(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ticket.title = data['title']
            ticket.description = data['description']
            ticket.save()
        return HttpResponseRedirect(reverse('detailpage', args=(ticketid,)))
    Form = createticketform(initial={
        'title': ticket.title,
        'description': ticket.description
    })
    return render(request,'form.html',{"Form":Form})

def viewuser(request,userid):
    assigned = Ticket.objects.filter(userassigned_id=userid)
    completed = Ticket.objects.filter(usercompleted_id=userid)
    submited = Ticket.objects.filter(usersubmited_id=userid)
    return render(request,'userpage.html',{'assigned': assigned,'completed':completed,'submited':submited})