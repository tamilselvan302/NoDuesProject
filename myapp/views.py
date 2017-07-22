from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout
from django.views.generic import View
from .forms import UserForm
from .models import Student,Proffesor,Others

def index(request):
	if request.user.is_authenticated() and request.user.username != "shivram":
		if request.method == "GET":
			profCheck = Proffesor.objects.filter(webmail=request.user.username)

			if profCheck[0].hod:
				studList = Student.objects.filter(cc=False,sa=False,workshop=False,cselib=False)
				for x in xrange(2,6):
					qry = "prof" + str(x)
					my_filter = {}
					my_filter[qry] = False
					studList = studList.filter(**my_filter)
				profCol = profCheck[0].colName
				return render(request, 'myapp/index.html',{'studList': studList, 'user': profCol, 'hostel': profCheck[0].hostel , 'nameDisplay':profCheck[0].name})

			studList = Student.objects.all()
			profCol = profCheck[0].colName
			return render(request, 'myapp/index.html',{'studList':studList,'user':profCol,'hostel':profCheck[0].hostel, 'nameDisplay':profCheck[0].name})

		else:
			selectStud = request.POST.getlist('selectList')
			for mail in selectStud:
				student = Student.objects.get(webmail=mail)
				userVar = request.user.username
				profCheck = Proffesor.objects.filter(webmail=userVar)
				profCol = profCheck[0].colName

				setattr(student,profCol,False)
				student.save()

			return redirect('myapp:index')

	else:
		return redirect('myapp:Login')

def hostel(request):
	if request.user.is_authenticated() and request.user.username != "shivram":
		if request.method == "GET":

			profCheck = Proffesor.objects.filter(webmail=request.user.username)
			studList = Student.objects.filter(hostel=profCheck[0].hostel)

			return render(request, 'myapp/hostel.html',{'studList':studList,'user':"hostelVal",'hostel':profCheck[0].hostel, 'nameDisplay':profCheck[0].name})

		else:
			selectStud = request.POST.getlist('selectList')
			for mail in selectStud:
				student = Student.objects.get(webmail=mail)
				setattr(student,"hostelVal",False)
				student.save()

			return redirect('myapp:hostel')

	else:
		return redirect('myapp:Login')

def comment(request):
	if request.user.is_authenticated() and request.user.username != "shivram":
		if request.method == "GET":
			profCheck = Proffesor.objects.filter(webmail=request.user.username)
			return render(request,'myapp/choice.html',{'hostel':profCheck[0].hostel})
		else:
			if request.POST['action'] == "ch":
				if request.POST['choose'] == "dept":
					studList = Student.objects.all()
					profCheck = Proffesor.objects.filter(webmail=request.user.username)
					profCol = profCheck[0].colName
					return render(request, 'myapp/comment.html', {'studList': studList,'user':profCol,'hostel':profCheck[0].hostel})
				else:
					profCheck = Proffesor.objects.filter(webmail=request.user.username)
					studList = Student.objects.filter(hostel=profCheck[0].hostel)
					profCol = "hostelVal"
					return render(request, 'myapp/comment.html',{'studList': studList, 'user': profCol, 'hostel': profCheck[0].hostel})

			else:
				pkFind = request.POST['studentComment']
				student = Student.objects.get(pk=pkFind)
				profCheck = Proffesor.objects.filter(webmail=request.user.username)
				profCol = request.POST['column']
				return render(request, 'myapp/edit.html', {'student': student, 'user': profCol,'hostel':profCheck[0].hostel})
	else:
		return redirect('myapp:Login')

def successEdit(request):
	if request.method == "GET":
		return redirect('myapp:index')
	else:
		textEntered=request.POST['newComment']
		pkFind = request.POST['pkStud']
		student = Student.objects.get(pk=pkFind)

		profCol = request.POST['column']
		profCol = profCol + "C"

		setattr(student,profCol,textEntered)
		student.save()

		if profCol == "hostelValC":
			return redirect('myapp:hostel')

		return redirect('myapp:index')


class Login(View):
	form_class = UserForm
	template_name = 'myapp/login.html'

	def  get(self,request):
		form = self.form_class(None)
		return render(request,self.template_name,{'form':form})

	def  post(self,request):
		form = self.form_class(request.POST)

		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			checkUser = authenticate(username=username,password=password)

			if checkUser is not None:
				if checkUser.is_active:
					login(request,checkUser)
					if checkUser.username == "shivram":
						return redirect('/admin')
					else:
						profCheck = Proffesor.objects.filter(webmail=username)
						if profCheck.count():
							return redirect('myapp:index')
						else:
							otherCheck = Others.objects.filter(webmail=username)
							if otherCheck.count():
								return redirect('myapp:others')
							else:
								return redirect('myapp:stud1')
			else:
				return render(request, self.template_name, {'form': form})
		else:
			return render(request, self.template_name, {'form': form})



def Logout(request):
	if request.user.is_authenticated():
		logout(request)
	return redirect('myapp:Login')


def others(request):
	if request.user.is_authenticated() and request.user.username != "shivram": #CHANGE
		#return HttpResponse('<p>u r logged in</p>')
		if request.method == "GET":

			otherCheck = Others.objects.filter(webmail=request.user.username)

			if otherCheck[0].webmail == "fa":
				studList = Student.objects.filter(prof1=False)
				otherCol = otherCheck[0].colName
				return render(request, 'myapp/others.html', {'studList': studList, 'user': otherCol, 'nameDisplay':otherCheck[0].name})

			studList = Student.objects.all()
			otherCol = otherCheck[0].colName
			return render(request, 'myapp/others.html',{'studList':studList,'user':otherCol, 'nameDisplay':otherCheck[0].name})

		else:
			selectStud = request.POST.getlist('selectList')
			for mail in selectStud:
				student = Student.objects.get(webmail=mail)
				userVar = request.user.username
				otherCheck = Others.objects.filter(webmail=userVar)
				otherCol = otherCheck[0].colName

				setattr(student,otherCol,False)
				student.save()

			return redirect('myapp:others')

	else:
		return redirect('myapp:Login')



def otherscomment(request):
	if request.user.is_authenticated() and request.user.username != "shivram": #CHANGE
		if request.method == "GET":
			studList = Student.objects.all()
			otherCheck = Others.objects.filter(webmail=request.user.username)
			otherCol = otherCheck[0].colName
			return render(request, 'myapp/otherscomment.html',{'studList': studList, 'user': otherCol})
		else:
			pkFind = request.POST['studentComment']
			student = Student.objects.get(pk=pkFind)
			otherCheck = Others.objects.filter(webmail=request.user.username)
			otherCol = otherCheck[0].colName
			return render(request, 'myapp/othersedit.html', {'student': student, 'user': otherCol})
	else:
		return redirect('myapp:Login')

def successEditothers(request):
	if request.method == "GET":
		return redirect('myapp:others')
	else:
		textEntered=request.POST['newComment']
		pkFind = request.POST['pkStud']
		student = Student.objects.get(pk=pkFind)

		otherCol = request.POST['column']
		otherCol = otherCol + "C"

		setattr(student,otherCol,textEntered)
		student.save()

		return redirect('myapp:others')





def stud1(request):
	if request.user.is_authenticated():
		all_albums=Student.objects.all()
		context1={'all_albums':all_albums,'webmail':request.user.username}
		return render(request,"myapp/inde.html",context1)
	else:
		return redirect('myapp:Login')


def stud2(request):
	if request.user.is_authenticated():
		all_albums=Student.objects.all()
		context1={'all_albums':all_albums,'webmail':request.user.username}
		return render(request,"myapp/inde1.html",context1)
	else:
		return redirect('myapp:Login')









