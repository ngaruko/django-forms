from django.shortcuts import render
from .forms import CoffeeForm 

def home (request):
    return render(request, 'coffee/home.html')

def order (request):
    if request.method == 'POST':
        form_data = CoffeeForm(request.POST)
        if form_data.is_valid():
            reply = 'Thanks %s for ordering coffee. Your %s %s is coming your way!' %(form_data.cleaned_data['name'], form_data.cleaned_data['size'], form_data.cleaned_data['flavour'])
            form = CoffeeForm() 
            return render(request, 'coffee/order.html', {'coffee_form': form, 'reply': reply})         
    

    else:
        return render(request, 'coffee/order.html', {'coffee_form': CoffeeForm()  })
