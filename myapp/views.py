from django.shortcuts import render
from myapp.models import *
from django.http import HttpResponseRedirect

# Create your views here.
def homepage(request):
	if request.session.has_key('user'):
		un=request.session['user']
		cr=customerreg.objects.get(mobile=un)
		return render(request,'home.html',{'cr':cr})
	else:
		return render(request,'home.html',{})
def aboutpage(request):
	if request.session.has_key('user'):
		un=request.session['user']
		cr=customerreg.objects.get(mobile=un)
		return render(request,'about.html',{'cr':cr})
	else:
		return render(request,'about.html',{})
def cabspage(request):
	if request.session.has_key('user'):
		un=request.session['user']
		cr=customerreg.objects.get(mobile=un)
		resulteddisplay=addk.objects.all()
		return render (request,'cabs.html',{'res':resulteddisplay,'cr':cr})
	else:
		resulteddisplay=addk.objects.all()
		return render(request,'cabs.html',{'res':resulteddisplay})

def caboffer(request):
	if request.session.has_key('user'):
		un=request.session['user']
		cr=offer.objects.all()
		return render(request,'caboffer.html',{'cr':cr,'un':un})
	else:
		return render(request,'customerlogin.html',{})

def admin(request):
	if request.session.has_key('user'):
		un=request.session['user']
		return render(request,'admin.html',{})
	else:
		res="you must login"
		return render(request,'adminlogin.html',{'res':res})
	
def adminlogin(request):
	return render(request,'adminlogin.html',{})

def add(request):
	if request.session.has_key('user'):
		un=request.session['user']
		return render(request,'addcars.html',{'un':un})
	else:
		res="you must login"
		return render(request,'adminlogin.html',{'res':res})
	
def car(request):
	if request.session.has_key('user'):
		un=request.session['user']
		resulteddisplay=addk.objects.all()
		return render (request,'cars.html',{'result':resulteddisplay})

def adminpage(request):
	un=request.POST['name']
	print(un)
	pwd=request.POST['pass']
	print(pwd)	
	if adminlog.objects.filter(Username=un,Password=pwd).exists():
		request.session['user']=un
		return render(request,'admin.html')
	else:
		m="Invalid Login"
		return render(request,'adminlogin.html',{"msg":m})
	
def insertrecord(request):
	if request.session.has_key('user'):
		un=request.session['user']
		if request.method == 'POST':
			pic=request.FILES['photo']
			details = request.POST['txtdetails']
			model = request.POST['txtmodel']
			color = request.POST['txtcolor']
			carnumber = request.POST['txtcarnumber']
			seats = request.POST['txtseats']
			drivercharge = request.POST['txtdrivercharge']
			roadcharge = request.POST['txtonroadcharge']
			accharge = request.POST['txtaccharge']	

			cab=addk()
			cab.Photo=pic
			cab.Details=details
			cab.Model=model
			cab.Color=color
			cab.CarNumber=carnumber
			cab.Seats=seats
			cab.DriverCharge=drivercharge
			cab.OnroadCharge=roadcharge
			cab.ACCharge=accharge
			cab.save()
			msg="Registered Successfully"
			return render(request,'addcars.html',{"msg":msg,'un':un})
		
def viewdetails(request):
	if request.session.has_key('user'):
		un=request.session['user']
		resulteddisplay=addk.objects.all()
		return render (request,'viewdetails.html',{'result':resulteddisplay})
def viewcars(request):
	if request.session.has_key('user'):
		un=request.session['user']
		resulteddisplay=addk.objects.all()
		return render(request,'viewcars.html',{'result':resulteddisplay})
	else:
		res="you must login"
		return render(request,'adminlogin.html',{'res':res})
	
def logincheck(request):
	nam=request.POST['una']
	passwo=request.POST['paa']
	if customerreg.objects.filter(mobile=nam,password=passwo).exists():
		request.session['user']=nam
		return HttpResponseRedirect('/')
	else:
		m="Invalid Login"
		return render(request,'customerlogin.html',{"msg":m})


def login(request):
	return render(request,'customerlogin.html')

def details(request):
	if request.session.has_key('user'):
		un=request.session['user']
		resulteddisplay=bkdetail.objects.all()
		return render(request,'details.html',{'getdata1':resulteddisplay})
	else:
		res="you must login"
		return render(request,'adminlogin.html',{'res':res})
	
def bookdetails(request):
	if request.session.has_key('user'):
		un=request.session['user']
		if request.method == 'POST':
			firstname=request.POST['fname']
			email = request.POST['email']
			mobnum = request.POST['number']
			picup = request.POST['picloc']
			drop = request.POST['droploc']
			pickdate = request.POST['picdate']
			pictime = request.POST['pictime']
			numperson = request.POST['numperson']
			ac = request.POST['ac']
			special = request.POST['req']
			payoption = request.POST['pa']
			c = request.POST['cno']
			of = request.POST['off']
			

			det=bkdetail()

			det.Firstname=firstname
			det.Email=email
			det.Mobnum=mobnum
			det.Pickuploc=picup
			det.Droploc=drop
			det.Pickdate=pickdate
			det.Picktime=pictime
			det.NumofPersons=numperson
			det.Ac=ac
			det.Request=special
			det.Payment=payoption
			det.carno=c
			det.offer=of
			det.save()
			msg="booked Successfully"
			return render(request,'details2.html',{"msg":msg})

def details2(request):
		return render(request,'details2.html',{})

def loginsucess(request,id):
	if request.session.has_key('user'):
		un=request.session['user']
		resulteddisplay=feed.objects.get(id=id)
		return render(request,'feedbackmessage.html',{'getdata':resulteddisplay})

def login2(request):
	if request.session.has_key('user'):
		un=request.session['user']
		return render(request,'feedbackmessage.html',{})

def feedba(request):
	if request.session.has_key('user'):
		resulteddisplay=feed.objects.all()
		return render(request,'viewfeedback.html',{'getdata5':resulteddisplay})
	else:
		res="you must login"
		return render(request,'adminlogin.html',{'res':res})

def select(request,id):
	if request.session.has_key('user'):
		un=request.session['user']
		resulteddisplay=bkdetail.objects.get(id=id)
		return render(request,'viewbookdet1.html',{'selrec':resulteddisplay})

def edit(request,id):
	if request.session.has_key('user'):
		un=request.session['user']
		res=bkdetail.objects.get(id=id)
		return render(request,'edit.html',{'user':res})

def delete(request,id):
	if request.session.has_key('user'):
		un=request.session['user']
		stud=bkdetail.objects.get(id=id)
		stud.delete()
		return HttpResponseRedirect('/details')

def logout(request):
	del request.session['user']
	return HttpResponseRedirect('/login')

def update(request,id):
	if request.session.has_key('user'):
		un=request.session['user']
		if request.method == 'POST':
			firstname=request.POST['fname']
			lastname = request.POST['lname']
			email = request.POST['email']
			mobnum = request.POST['number']
			picup = request.POST['picloc']
			drop = request.POST['droploc']
			pickdate = request.POST['picdate']
			pictime = request.POST['pictime']
			numperson = request.POST['numperson']
			ac = request.POST['ac']
			special = request.POST['req']

			det=bkdetail.objects.get(id=id)
			det.Firstname=firstname
			det.Lastname=lastname
			det.Email=email
			det.Mobnum=mobnum
			det.Pickuploc=picup
			det.Droploc=drop
			det.Pickdate=pickdate
			det.Picktime=pictime
			det.NumofPersons=numperson
			det.Ac=ac
			det.Request=special
			det.save()

			return HttpResponseRedirect('/details')

def select1(request,id):
	if request.session.has_key('user'):
		un=request.session['user']
		resulteddisplay=addk.objects.get(id=id)
		return render(request,'viewcars2.html',{'selrec1':resulteddisplay})

def update1(request,id):
	if request.session.has_key('user'):
		un=request.session['user']
		if request.method == 'POST':
			pic=request.FILES['dp']
			details = request.POST['txtdetails']
			model = request.POST['txtmodel']
			color = request.POST['txtcolor']
			carnumber = request.POST['txtcarnumber']
			seats = request.POST['txtseats']
			drivercharge = request.POST['txtdrivercharge']
			roadcharge = request.POST['txtonroadcharge']
			accharge = request.POST['txtaccharge']
			off = request.POST['txtoffer']

			cab=addk()
			cab.Photo=pic
			cab.Details=details
			cab.Model=model
			cab.Color=color
			cab.CarNumber=carnumber
			cab.Seats=seats
			cab.DriverCharge=drivercharge
			cab.OnroadCharge=roadcharge
			cab.ACCharge=accharge
			cab.offer=off
			cab.save()

			return HttpResponseRedirect('/viewdetails')

def edit1(request,id):
	if request.session.has_key('user'):
		un=request.session['user']
		res=addk.objects.get(id=id)
		return render(request,'edit2.html',{'user':res})

def loginsuccess3(request):
	if request.session.has_key('user'):
		un=request.session['user']
		return render(request,'admin.html',{})
	else:
		return render(request,'adminlogin.html')
		
def logout2(request):
	del request.session['user']
	return render(request,'adminlogin.html')

def delete1(request,id):
	if request.session.has_key('user'):
		un=request.session['user']
		stud1=addk.objects.get(id=id)
		stud1.delete()
		return HttpResponseRedirect('/viewdetails')

def delete2(request,id):
	if request.session.has_key('user'):
		un=request.session['user']
		stud2=feed.objects.get(id=id)
		stud2.delete()
		return HttpResponseRedirect('/feedba')

def logout3(request):
	return render(request,'home.html')

def update3(request,id):
	if request.session.has_key('user'):
		un=request.session['user']
		if request.method == 'POST':
			n = request.POST['ne']
			cu = request.POST['cus'] 
			ans = request.POST['txtanswer']

			an=feed.objects.get(id=id)
			
			an.Name=n
			an.Cusfeedback=cu
			an.Answer=ans
			an.save()
			return HttpResponseRedirect('/feedba')
	
def replay(request,id):
	if request.session.has_key('user'):
		un=request.session['user']
		res=feed.objects.get(id=id)
		return render(request,'replay.html',{'user':res})

def area(request):
	if request.session.has_key('user'):
		un=request.session['user']
		a=triparea.objects.all()
		return render(request,"a_view_area.html",{'a':a})

def addarea(request):
	if request.session.has_key('user'):
		un=request.session['user']
		return render(request,"a_add_area.html",{})

def addarea1(request):
	if request.session.has_key('user'):
		un=request.session['user']
		if request.method == 'POST':
			n=request.POST['area']
			ar=triparea()
			ar.area=n
			ar.save()
			return render(request,"a_add_area.html",{})

def areaselect(request,id):
	if request.session.has_key('user'):
		un=request.session['user']
		ar=triparea.objects.get(id=id)
		return HttpResponseRedirect('/area',{'ar':ar})

def areaedit(request,id):
	if request.session.has_key('user'):
		un=request.session['user']
		ar=triparea.objects.get(id=id)
		return render(request,'a_edit_area.html',{'ar':ar})

def areaeditsave(request,id):
	if request.session.has_key('user'):
		un=request.session['user']
		if request.method == 'POST':
			a=request.POST['are']
			ar=triparea.objects.get(id=id)
			ar.area=a
			ar.save()
			return HttpResponseRedirect('/area')
	
def areadelete(request,id):
	if request.session.has_key('user'):
		un=request.session['user']
		ar=triparea.objects.filter(id=id)
		ar.delete()
		return HttpResponseRedirect('/area')

def aoffer(request):
	if request.session.has_key('user'):
		un=request.session['user']
		o=offer.objects.all()
		cr=addk.objects.all()
		return render(request,'a_offer_view.html',{'cr':cr,'o':o})

def offeradd(request):
	if request.session.has_key('user'):
		un=request.session['user']
		if request.method == 'POST':
			c=request.POST['ocar']
			of=request.POST['off']

			k=offer()

			k.carid=i
			k.carnumber=c
			k.offer=of
			k.save()
			return HttpResponseRedirect('/aoffer')

def offerdelete(request,id):	
	if request.session.has_key('user'):
		un=request.session['user']
		o=offer.objects.filter(id=id)
		o.delete()
		return HttpResponseRedirect('/aoffer')
	
def carviewoffer(request,id):
	if request.session.has_key('user'):
		un=request.session['user']
		o=addk.objects.get(id=id)
		return render(request,'a_offer_view1.html',{'o':o})
	

#customer


def cusreg(request):
	return render(request,'customer_reg.html',{})

def regcus(request):
	if request.session.has_key('user'):
		un=request.session['user']
		if request.method == 'POST':
			n=request.POST['na']
			m=request.POST['mo']
			e=request.POST['em']
			p=request.POST['ps']
			a=request.POST['ad']

			r=customerreg()

			r.name=n
			r.mobile=m
			r.email=e
			r.password=p
			r.address=a
			r.save()
			cr=customerreg.objects.get(mobile=un)
			res="Register Successfully"
			return HttpResponseRedirect('/login',{'result':res,'cr':cr})
		
def bookingpage(request):
	if request.session.has_key('user'):
		un=request.session['user']
		cr=customerreg.objects.get(mobile=un)
	return render(request,'booking.html',{'cr':cr})

def bookpage(request):
	if request.session.has_key('user'):
		un=request.session['user']
		cr=customerreg.objects.get(mobile=un)
		resulteddisplay=addk.objects.all()
		a=triparea.objects.all()
	return render (request,'book.html',{'result':resulteddisplay,'cr':cr,'a':a})

def book1(request,id):
	if request.session.has_key('user'):
		un=request.session['user']
		resulteddisplay=addk.objects.get(id=id)
		o=offer.objects.get(carid=id)
		cr=customerreg.objects.get(mobile=un)
		a=triparea.objects.all()
		return render(request,'book.html',{'getdata':resulteddisplay,'cr':cr,'a':a,'o':o})
	else:
		return render(request,'customerlogin.html',{})
	

def viewreplay(request):
	if request.session.has_key('user'):
		un=request.session['user']
		cr=customerreg.objects.get(mobile=un)
		res=feed.objects.get(mobile=un)
		return render (request,'viewreplay.html',{'res':res,'cr':cr})
	else:
		return render(request,'viewreplay.html',{})

def clientbooking(request):
	if request.session.has_key('user'):
		un=request.session['user']
		cr=customerreg.objects.get(mobile=un)
		f=bkdetail.objects.filter(Mobnum=un)
		return render (request,'c_view_booking.html',{'f':f,'cr':cr})
	else:
		return render(request,'customerlogin.html',{})

def addfeed(request):
	if request.method == 'POST':
		nam=request.POST['cn']
		mob=request.POST['cm']
		feedbac=request.POST['feedb']

		fe=feed()
		fe.Name=nam
		fe.mobile=mob
		fe.Cusfeedback=feedbac
		fe.save()
		return HttpResponseRedirect('/clientbooking')
	
def viewfeedback(request,id):
	if request.session.has_key('user'):
		un=request.session['user']
		cr=bkdetail.objects.get(id=id)
		return render(request,'feedback.html',{'cr':cr,'un':un})
	else:
		return render(request,'customerlogin.html',{})
