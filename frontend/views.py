from django.http.request import HttpRequest
from django.shortcuts import render, redirect
from frontend.models import User, Complaint

def landing(request: HttpRequest):
    return render(request, 'landing.html')

def login(request: HttpRequest):
    ''' Uses user account if it exists. Else, creates a new one.'''
    if request.method == 'POST':
        user_data = request.POST.dict()
        if not User.objects.filter(username=user_data['username']).exists():
            obj = User(username=user_data['username'], password=user_data['password'])
            obj.save()
        return redirect('complaints', user_data['username'])
    else:
        return render(request, 'landing.html')

def complaints(request: HttpRequest, username: str):
    user_complaints = Complaint.objects.filter(username=username)
    context = {}
    context['username'] = username
    context['complaints'] = []
    for complaint in user_complaints:
        context['complaints'].append({'title': complaint.title, 'content': complaint.content})
    context['count'] = len(context['complaints'])
    return render(request, 'complaints.html', context)

def register(request: HttpRequest, username: str):
    content = request.POST.dict()
    user = User.objects.get(username=username)
    obj = Complaint(username=user, title=content['title'], content=content['content'])
    obj.save()
    return redirect('complaints', username)
