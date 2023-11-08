from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import *
from django.views.generic import CreateView,UpdateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm



def admin_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None and user.is_superuser:
                login(request, user)
                return redirect('admin_page')
            else:
                return render(request, 'admin_login.html', {'form': form, 'error_message': 'Invalid credentials'})
    else:
        form = AuthenticationForm()

    return render(request, 'admin_login.html', {'form': form})
# Create your views here.
def index(request):
    products=Product.objects.all()
    print(products)
    return render(request,'index.html',{'products':products})

#admin view
def admin_page(request):
    products=Product.objects.all()
    print(products)
    return render(request,'admin_page.html',{'products':products})

#product update
class update_product(UpdateView):
    model=Product
    fields="__all__"
    template_name='update_product.html'
    success_url=reverse_lazy('admin_page')

#product delete
def delete_product(request,pk):
    ud=Product.objects.filter(id=pk)
    ud.delete()
    return redirect('admin_page')


#product insert
class add_product(CreateView):
    model=Product
    fields="__all__"
    template_name='add_product.html'
    success_url=reverse_lazy('admin_page')