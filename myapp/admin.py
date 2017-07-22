from django.contrib import admin

# Register your models here.


from .models import Student,Proffesor,Others


admin.site.register(Student)
admin.site.register(Proffesor)
admin.site.register(Others)