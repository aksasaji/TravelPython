from django.shortcuts import render
from django.http import HttpResponse
from . models import Place
from . models import Person
def demo(request):
    obj=Place.objects.all()
    objs=Person.objects.all()
    #name="india"
    return  render(request,"index.html",{'result':obj,'results':objs})
#def addition(request):
   # x=int(request.GET['num1'])
#    y=int(request.GET['num2'])
 #   res=x+y
  #  resu=x-y
   # resul=x*y
    #result=x/y
#    return render(request, "result.html", {'result':res,'sub': resu,'mul':resul,'div':result})

#def about(request):
    #return render(request,"result.html")
#def contact(request):
   # return render(request,"contact.html")
#def detail(request):
 #   return HttpResponse("details please")
#def thankyou(request):
#    return HttpResponse("thankyou for visiting")