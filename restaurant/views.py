from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Customer
from .forms import CustomerForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'restaurant/home.html')

@login_required
def add_customer(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        phone_number = request.POST.get('phone_number', '').strip()

        # Validate input

        if not name or not phone_number:
            return render(request, 'restaurant/add_customer.html', {'error': 'Name and phone number are required.'})

        # Check if a customer with the phone number already exists
        created = Customer.objects.get_or_create(phone_number=phone_number, defaults={'name': name})
        
        if not created:
            # Customer already exists
            return render(request, 'restaurant/add_customer.html', {'error': 'Customer with this phone number already exists.'})
        # not working
        return render(request, 'restaurant/add_customer.html', {'success': 'Customer added successfully!'})

    return render(request, 'restaurant/add_customer.html')

@login_required
def customer_lookup(request):
    customers =[]

    if request.method == 'POST':
        search_term = request.POST.get('search_term')
        if search_term:
            customers = Customer.objects.filter(Q(name__icontains=search_term)| Q(phone_number__icontains=search_term))


    return render(request, 'restaurant/customer_lookup.html', {'customers': customers})

@login_required
def customer_detail(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)

    if request.method == 'POST':
        if 'delete' in request.POST:
            customer.delete()
            return redirect('customer_lookup')
        else:
            form = CustomerForm(request.POST, instance=customer)
            if form.is_valid():
                form.save()

    else:
        form = CustomerForm(instance=customer)

    return render(request, 'restaurant/customer_detail.html', {'customer': customer, 'form': form})










