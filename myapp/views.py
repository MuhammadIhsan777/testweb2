from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from myapp.models import Mahasiswa

def index(request):
    return render(request, 'myapp/index.html')

def mahasiswa_list(request):
    mahasiswa = Mahasiswa.objects.all()
    return render(request, 'myapp/mahasiswa_list.html', {'mahasiswa': mahasiswa})

from django.shortcuts import render
from myapp.models import Mahasiswa

def mahasiswa_list(request):
      mahasiswa = Mahasiswa.objects.all()
      return render(request, 'myapp/mahasiswa_list.html', {'mahasiswa': mahasiswa})

from myapp.models import Jurusan

def jurusan_list(request):
     jurusan = Jurusan.objects.all()
     return render(request, 'myapp/jurusan_list.html', {'jurusan': jurusan})