from django.shortcuts import render

from .forms import Leitor
from django.http import HttpResponse
import datetime
from teste import linux
import os
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.



def home(request):
    return render(request, 'mooc.html',{'usuario': 'Fulano de Tal'})

