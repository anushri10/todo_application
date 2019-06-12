from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from assignment.forms import *
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core import mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

#user functionalities

def main_page(request):
    if 'user_id' in request.session:
        user_obj=User.objects.filter(id=request.session['user_id'])
        todo_obj=Todo.objects.filter(user_id=request.session['user_id'])
        data={'fname':request.session['fname'],'user':user_obj,'todo':todo_obj,'a':0}
        return render(request,'home.html',data)
        #return render_to_response('home.html',data)
    else:
        form = SignupForm()
        variables = {'form': form}
        #return render_to_response('index.html', {'form': form},context_instance = RequestContext(request))
        return render(request,'index.html',variables)

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            obj=form.save()
            id=obj.id
            request.session['user_id']=id
            request.session['fname']=form.cleaned_data['fname']
    return HttpResponseRedirect('/')

def login(request):
    user_obj=User.objects.filter(email=request.POST.get('email'),password=request.POST.get('password'))
    if user_obj.count():
        print (user_obj)
        request.session['user_id']=user_obj[0].id
        request.session['fname']=user_obj[0].fname
    return HttpResponseRedirect('/')

def logout(request):
    del request.session['user_id']
    del request.session['fname']
    request.session.modified=True
    return HttpResponseRedirect('/')

#operations on todo list

def add_todo(request):
    if request.method=='POST':
       todo_obj=Todo(todo_job=request.POST.get('job'),priority=request.POST.get('level'),completed=request.POST.get('status'),user_id=request.session['user_id'])
       todo_obj.save()
       return HttpResponseRedirect('/')
    else:
       data={'fname':request.session['fname']}
       return render(request,'add_todo.html',data)
       #return render_to_response('add_todo.html',data)

def edit_todo(request,todo_id):
    if request.method=='POST':
        todo_obj=Todo.objects.filter(id=request.POST.get('id')).update(todo_job=request.POST.get('job'),priority=request.POST.get('level'),completed=request.POST.get('status'))
        return HttpResponseRedirect('/')
    else:
        todo_obj=Todo.objects.filter(id=todo_id)
        data={'fname':request.session['fname'],'todo':todo_obj[0]}
        return render(request,'edit_todo.html',data)

def delete_todo(request,todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')

def email_todo(request):
    #if 'user_id' in request.session:
    user_obj=User.objects.filter(id=request.session['user_id'])
    todo_obj=Todo.objects.filter(user_id=request.session['user_id'])
    data={'fname':request.session['fname'],'user':user_obj,'todo':todo_obj,'a':0}
    u_name = request.session['fname']
    if request.method=='POST':
        todo_data=[]
        for row in todo_obj:
            todo_data.append(str(row.created_date))
            todo_data.append(str(row.todo_job))
            todo_data.append(str(row.priority))
            todo_data.append(str(row.completed))
            print("\n",todo_data,"\n")

        to=request.POST.get('email')
        subject = str(u_name)+"'s Todo List:"
        html_message = render_to_string('extra_todo_table.html', data)
        plain_message = strip_tags(html_message)
        from_email = 'xxxx@gmail.com'

    #to = 'to@example.com'
        #msg = EmailMultiAlternatives(subject, plain_message, from_email, [to])
        #msg.attach_alternative(html_message, "text/html")
        #msg.send()

        mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
        return render(request,'email_todo.html',data)
    else:
        return render(request,'email_todo.html',data)




