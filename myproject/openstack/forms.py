from django import forms
#from bigdata.views import get_my_choices
#from .views import page1
#from bigdata.functions import get_my_choices
#import .views
#from .models import Join


	


def get_my_choices():
	import subprocess
	ee=[]
	s=subprocess.Popen(["nova --os-username admin --os-password prax --os-tenant-name admin --os-auth-url http://192.168.43.154:35357/v2.0/ image-list"],stdout=subprocess.PIPE, shell=True)
	temp=s.communicate()[0]
	print temp,'dsfsdf'
	temp=temp.split('\n')
	temp1=temp[3:]
	temp2=temp1[:len(temp1)-2]
	count=1
	for i in temp2:
		ee.append((count,i.split('|')[2].strip()))
	
		count=count+1
	return ee

class DropDlist(forms.Form):
	choice=[(1,'m1.tiny'),(2,'m1.small'),(3,'m1.medium'),(4,'m1.large'),(5,'m1.xlarge')]
	OS_Name=forms.CharField(required=True)
	#progname=forms.CharField(required=True)
	#outputfold=forms.CharField(required=True)
	Flavor_List=forms.ChoiceField(widget=forms.RadioSelect,choices=choice)
	Image_To_Boot = forms.ChoiceField(choices=get_my_choices())
	'''def __init__(self, *args, **kwargs):
        	super(DropDlist, self).__init__(*args, **kwargs)
        	self.fields['Image_to_Boot'] = forms.ChoiceField(
           	   choices=get_my_choices() )
	'''
