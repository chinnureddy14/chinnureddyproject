from django.shortcuts import render,redirect
from django.http import  HttpResponse
from chinnu_reddy.models import UsrRg,NewData
from chinnu_reddy.forms import UsregForm,Userupdate,NewUsrForms

def home(request):
	return HttpResponse("<h1 style='background-color:powderblue;'>welcome to aits</h1>")

def chk(request):
	return HttpResponse("<script>alert('hi good afternoon')</script><h2>welcome</h2>")


def homepage(request):
	return render(request,'ht/homepage.html')


def lgn(re):
	return render(re,'ht/login.html')


def reg(rt):
	return render(rt,'ht/register.html') 


def bthm(qw):
	return render(qw,'ht/bthome.html')

def about(req):
	return render(req,'ht/about.html')

		
def contact(req):
	return render(req,'ht/contact.html')


def registration(req):
	if req.method=="POST":
		fn=req.POST['fname'];
		ln=req.POST['lname'];
		age=req.POST['age'];
		mail=req.POST['email'];
		pas=req.POST['pwd'];
		pas1=req.POST['pwd1'];
		d={'info':fn,'info1':ln,'info2':age,'info3':mail,'info4':pas,'info5':pas1}
		return render(req,'ht/details.html',{'d':d})
	return render(req,'ht/registration.html')



def crud(rq):
	if rq.method == "POST":
		un=rq.POST['username']
		p=rq.POST['password']
		e=rq.POST['email']
		ph=rq.POST['age']
		data2=UsrRg.objects.all()
		if len(un)!=0:
			data=UsrRg.objects.create(username=un,password=p,email=e,age=ph)
			return render(rq,'ht/actions.html',{'info':data2})
   
	data2=UsrRg.objects.all()
	return render(rq,'ht/actions.html',{'info':data2})
def deletedata(request,st):
	data=UsrRg.objects.get(id=st)
	data.delete()
	return redirect("/cr")
	



def dform(request):
	if request.method == "POST":
		e=UsregForm(request.POST)
		if e.is_valid():
			q=e.save()
			y=NewData.objects.create(pid_id=q.id)
			return redirect("/showdata")
			return render(request,'ht/dyform.html',{'tu':y})
	
	e=UsregForm()
	return render(request,'ht/dyform.html',{'tu':e})
                                                                                                                  


def showinfo(req):
	data=UsrRg.objects.all()
	return render(req,'ht/showdata.html',{'info':data})

def infodelete(req,et):
	data=UsrRg.objects.get(id=et)
	if req.method=="POST":
		data.delete()
		return redirect('/showdata')
	return render(req,'ht/userdelete.html',{'sd':data})




def userupdate(up,si):
	t=UsrRg.objects.get(id=si)
	y=NewData.objects.get(pid=si)
	if up.method=="POST":
		d=Userupdate(up.POST,instance=t)
		k=NewUsrForms(up.POST,instance=y)
		if d.is_valid() and k.is_valid():
			d.save()
			k.save()
			return redirect('/showdata')
	d=Userupdate(instance=t)
	k=NewUsrForms(instance=y)
	return render(up,'ht/updateuser.html',{'us':d,'nt':k})



def userinfo(rq,username):
	p=UsrRg.objects.get(username=username)
	h=NewData.objects.get(pid=p.id)
	return render(rq,'ht/uinfo.html',{'y':p,'yu':h})
	


	









































































































































