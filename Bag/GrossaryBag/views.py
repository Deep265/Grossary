from django.shortcuts import render,get_object_or_404,redirect,reverse
import datetime
# Models import
from django.contrib.auth.models import User
from .models import GroceryList

#login imports
from django.contrib.auth.decorators import login_required
# Https Imports
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
@login_required(login_url='/authenticate/login/')
def home(request):

    user = get_object_or_404(User,pk=request.user.pk)
    grossary = GroceryList.objects.filter(user=user,date=str(datetime.date.today()))

    if request.method == "POST":
        filter_date = request.POST.get("date")
        print(datetime.date.today(),filter_date)
        grossary = GroceryList.objects.filter(user=user,date=str(filter_date))
        return render(request,"index.html",context={"grossary":grossary})
    return render(request,"index.html",context={"grossary":grossary})


@login_required(login_url='/authenticate/login/')
def add_item(request,pk):
    user = get_object_or_404(User,pk=pk)
    if request.method == "POST":
        item_name = request.POST.get("item_name")
        item_quantity = request.POST.get("item_quantity")
        item_status = request.POST.get("item_status")
        date = request.POST.get("date")

        add = GroceryList(user=user,item_name=item_name,item_quantity=item_quantity,item_status=item_status,date=date)
        add.save()

        return HttpResponseRedirect(reverse('bag:Home'))
    return render(request,"GrossaryBag/add_item.html")

@login_required(login_url='/authenticate/login/')
def update_item(request,pk):
    grossary = get_object_or_404(GroceryList,pk=pk)
    if request.method == "POST":
        item_name = request.POST.get("item_name")
        item_quantity = request.POST.get("item_quantity")
        item_status = request.POST.get("item_status")
        date = request.POST.get("date")

        # Update
        grossary.item_name = item_name
        grossary.item_quantity = item_quantity
        grossary.item_status = item_status
        grossary.date = date

        grossary.save()

        return HttpResponseRedirect(reverse('bag:Home'))
    return render(request,"GrossaryBag/update_item.html",context={"grossary":grossary})

@login_required(login_url='/authenticate/login/')
def delete_item(request,pk):
    grossary = get_object_or_404(GroceryList,pk=pk)
    grossary.delete()
    return HttpResponseRedirect(reverse('bag:Home'))

@login_required(login_url='/authenticate/login/')
def check(request,pk):
    grossary = get_object_or_404(GroceryList,pk=pk)
    grossary.item_status = "Purchased"
    grossary.save()
    return HttpResponseRedirect(reverse('bag:Home'))

