from django.shortcuts import render
from account.models import rtlrmodel ,usermodel
from aio.models import all
def home(request):
    if request.method=='POST':
        return render(request,'mainframe/mnframe.html')
    else:
        rmach=rtlrmodel.objects
        suser=usermodel.objects
        return render(request,'mainframe/home.html',{'suser':suser,'rmach':rmach})

def homee(request):
    return render(request,'mainframe/homee.html')

def mnframe(request):
    if request.method=='POST':
        database=all.objects
        search=request.POST['Search']
        location=request.POST['Location']
        return render(request, 'mainframe/mnframe.html',{'database':database,'search':search,'location':location})

def tservice(request):
    return render(request,'mainframe/tservice.html')