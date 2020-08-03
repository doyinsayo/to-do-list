from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def todoappView(request):
    return render(request, 'todolist.html')

from .models import TodoListItem 

def addTodoView(request):
    x = request.POST['content']
    new_item = TodoListItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/todoapp/') 

def deleteTodoView(request, i):
    y = TodoListItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/todoapp/')     