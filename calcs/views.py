from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Calc

def calc(request):
  if request.method == 'POST':

    listing = request.POST['listing']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']



    calc = Calc(listing=listing,  name=name, email=email, phone=phone, message=message )

    calc.save()

    messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
    return redirect('/listings/')


