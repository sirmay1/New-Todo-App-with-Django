from django.shortcuts import render, redirect
from .models import List #(12:09)
from .forms import ListForm #(12:45)
from django.contrib import messages

# Create your views here.
# adding logic 'conditionals to our home function (13:00).


def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        
        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, ('Congratulations! You added a new item to the list!'))
            context = {'all_items': all_items}
            return render(request, 'home.html', context)
        
    else: #(13:40)
        all_items = List.objects.all
        context = {'all_items': all_items}
        return render(request, 'home.html', context)
    
    
def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item has been eradicated! Thank-You!'))
    return redirect('home')

def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')

def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')

def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)
        
        form = ListForm(request.POST or None, instance=item)
        
        if form.is_valid():
            form.save()
            messages.success(request, ('The item has been successfully Edited!'))
            return redirect('home')
    
    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})
    
    