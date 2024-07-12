from django.shortcuts import render, redirect
from .models import todoItem

# Function names are matched with the path provided in the urls.py
def index(request):
    todos = todoItem.objects.all()
    return render(request, 'index.html', {'todos' : todos} )

def add_todo(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        todoItem.objects.create(title=title, description=description)
        return redirect('index')
    return render(request, 'add_todo.html')

def update_todo(request, todo_id):
    todo = todoItem.objects.get(id=todo_id)
    if request.method == 'POST':
        todo.title = request.POST['title']
        todo.description = request.POST['description']
        todo.completed = 'completed' in request.POST
        todo.save()
        return redirect('index')
    return render(request, 'update_todo.html', {'todo': todo})

def delete_todo(request, todo_id):
    todo = todoItem.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')

