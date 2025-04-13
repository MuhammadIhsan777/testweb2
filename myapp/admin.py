from django.contrib import admin

# Register your models here.
from django.contrib import admin
from myapp.models import Mahasiswa, Jurusan

admin.site.register(Mahasiswa)
admin.site.register(Jurusan)