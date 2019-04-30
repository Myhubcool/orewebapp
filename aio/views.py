from django.shortcuts import render ,redirect
from account.models import rtlrmodel
from .models import all

def filled(request):
    rmach = rtlrmodel.objects
    if request.method == 'POST':
        if request.POST['x']=='a':
            x='z'
            fun=request.POST['fusernane']
            fuid=request.POST['fusernameid']
            fm=request.POST['fmob']
            fc=request.POST['fcity']
            sdd=request.POST['fshopadd']
            fst=request.POST['fstate']
            fdt=request.POST['fdistrict']
            fcy=request.POST['fcolony']
            fpn=request.POST['fpincode']
            fsn=request.POST['shopname']
            return render(request, 'aio/fill.html',{'fsn':fsn,'fst':fst,'fdt':fdt,'fcy':fcy,'fpn':fpn,'x':x,'fun':fun,'fm':fm,'fc':fc,'rmach':rmach,'sdd':sdd,'fuid':fuid})
        elif request.POST['x']=='z':
          pksheck = all.objects.all()
          for ck in pksheck:
              if ck.acompanyname==request.POST['companyname'] and ck.auid==request.POST['userid']:
                go='1'
                return render(request, 'aio/congratulation.html',{'errorr':'This detail is already you filled','go':go})
          else:
            if request.POST['companyname'] is not None:
                srt=all()
                srt.acompanyname=request.POST['companyname']
                srt.aname=request.POST['username']
                srt.amob = request.POST['phoneno']
                srt.ascity = request.POST['city']
                srt.auid=request.POST['userid']
                srt.aaddress = request.POST['address']
                srt.aprice = request.POST['price']
                srt.asstate=request.POST['state']
                srt.ascolony=request.POST['colony']
                srt.aspinno=request.POST['pinno']
                srt.asdistrict=request.POST['district']
                srt.asshopname=request.POST['shopname']
                srt.save()
                return render(request, 'aio/congratulation.html',{'send':request.POST['companyname']})
    else:
        return render(request,'aio/fill.html',{'rmach':rmach})


def congratulation(request):
    return render(request, 'aio/congratulation.html')







# Create your views here.
