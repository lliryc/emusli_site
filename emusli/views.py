from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
# import pdb; pdb.set_trace()

# Create your views here.
def index(request):
    context_dict = {}
    return render(request, 'emusli/index.html', context = context_dict)

def cashbox(request):
    context_dict = {}
    return render(request, 'emusli/cashbox.html', context = context_dict)

def mix(request):
    context_dict = {}
    return render(request, 'emusli/mix.html', context = context_dict)

def order(request):
    context_dict = {}
    return render(request, 'emusli/order.html', context = context_dict)
