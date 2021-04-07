from chinnu_reddy.models import UsrRg,NewData
from django import forms

class UsregForm(forms.ModelForm):
	class Meta:
		model=UsrRg
		fields=['username','email','password']
		widgets={
		"username":forms.TextInput(attrs= {"class":"form-control","placeholder":"Enter Username","required":True,}),
		"password":forms.PasswordInput(attrs= {"class":"form-control","placeholder":"Enter Password","required":True,}),
		
		"email":forms.EmailInput(attrs= {"class":"form-control","placeholder":"Enter Email","required":True,}),
		}
class Userupdate(forms.ModelForm):
	class Meta:
		model=UsrRg
		fields=['username','email','age']
		widgets={
		"username":forms.TextInput(attrs= {"class":"form-control","placeholder":"Enter Username","required":True,}),
		"email":forms.EmailInput(attrs= {"class":"form-control","placeholder":"Enter email","required":True,}), 
		"age":forms.NumberInput(attrs= {"class":"form-control","placeholder":"Enter age","required":True,}),
		}


class NewUsrForms(forms.ModelForm):
	class Meta:
		model=NewData
		fields=['mobile','gender']
		widgets={
		"mobile":forms.TextInput(attrs= {"class":"form-control","placeholder":"update mobile number","required":True,}),
		"gender":forms.Select(attrs= {"class":"form-control","placeholder":"Enter Username","required":True,}),
		}
	