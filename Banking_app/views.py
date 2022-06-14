from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Customer
# Create your views here.
def index(request):
    return render(request, 'index.html')

def view_cust(request):
    custs = Customer.objects.all()
    context = {
        'custs': custs
    }

    return render(request,'view_cust.html', context)


def add_customer(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        current_balance = request.POST['current_balance']
        new_cust = Customer(first_name = first_name ,last_name =last_name ,
         email =email,current_balance= current_balance )
        new_cust.save()
        custs = Customer.objects.all()
        context = {
        'custs': custs
         }
        return render(request, 'view_cust.html', context)
   # return render(request,'add_customer.html', {})

    elif request.method == 'GET':
        return render(request,'add_customer.html')

    else:
         return HttpResponse('An error occur')

    return render(request,"view_cust.html")




def remove_cust(request, cust_id = 0):
    if cust_id:
        try:
            cust_to_be_removed = Customer.objects.all()
            cust_to_be_removed.delete()
            return HttpResponse("Customer Removed Successfully")
        except:
            return HttpResponse("Please Enter A Valid CUST ID")

    custs = Customer.objects.all()
    context = {'custs': custs}
    return render(request,'remove_cust.html',context)