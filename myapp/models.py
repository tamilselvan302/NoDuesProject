from __future__ import unicode_literals
from django.db import models

class Student(models.Model):

    rollno = models.CharField(max_length=9,default="15010106")
    name = models.CharField(max_length=70,default="student")
    webmail = models.CharField(max_length=30,default="mail")

    hostel = models.CharField(max_length=50,default="barak")
    hostelVal = models.BooleanField(default=1)
    hostelValC = models.CharField(max_length=700, default="No remarks")

    prof1 = models.BooleanField(default=1)
    prof1C = models.CharField(max_length=700,default="No remarks")

    prof2 = models.BooleanField(default=1)
    prof2C = models.CharField(max_length=700,default="No remarks")

    prof3 = models.BooleanField(default=1)
    prof3C = models.CharField(max_length=700,default="No remarks")

    prof4 = models.BooleanField(default=1)
    prof4C = models.CharField(max_length=700, default="No remarks")

    prof5 = models.BooleanField(default=1)
    prof5C = models.CharField(max_length=700, default="No remarks")

    lab1 = models.BooleanField(default=1)
    lab1C = models.CharField(max_length=700, default="No remarks")

    lab2 = models.BooleanField(default=1)
    lab2C = models.CharField(max_length=700, default="No remarks")

    lab3 = models.BooleanField(default=1)
    lab3C = models.CharField(max_length=700, default="No remarks")

    cc = models.BooleanField(default=1)
    ccC = models.CharField(max_length=700, default="No remarks")

    sa = models.BooleanField(default=1)
    saC = models.CharField(max_length=700, default="No remarks")

    fa = models.BooleanField(default=1)
    faC = models.CharField(max_length=700, default="No remarks")

    workshop = models.BooleanField(default=1)
    workshopC = models.CharField(max_length=700, default="No remarks")

    cenlib = models.BooleanField(default=1)
    cenlibC = models.CharField(max_length=700, default="No remarks")

    cselib = models.BooleanField(default=1)
    cselibC = models.CharField(max_length=700, default="No remarks")


	#string defenition -- used in showAll()
    def __str__(self):
        return self.name

class Proffesor(models.Model):

    name = models.CharField(max_length=70,default="proffesor")
    webmail = models.CharField(max_length=30,default="mailprof")


    hostel = models.CharField(max_length=700,default="NIL")
    hod = models.BooleanField(default=0)

    colName = models.CharField(max_length=700, default="prof")

	#string defenition -- used in showAll()
    def __str__(self):
        return self.name


class Others(models.Model):

    name = models.CharField(max_length=70,default="other")
    webmail = models.CharField(max_length=30,default="mailother")


    colName = models.CharField(max_length=700, default="lab")

	#string defenition -- used in showAll()
    def __str__(self):
        return self.name


