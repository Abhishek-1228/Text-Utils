#I have created this file
from django.shortcuts import render
from django.http import HttpResponse
# def index(request):
#     return HttpResponse("<a href="" >Hello Abhishek</a>")

# def about(request):
#     return HttpResponse("about abhishek")
#code for txturls website

def index(request):
     
     return render(request, 'index.html')

def analyse(request):
     djtext=request.POST.get('text','default')
     # chech checkbox value
     rem=request.POST.get('remove','off')
     caps=request.POST.get('caps','off')
     nlr=request.POST.get('newlineremover','off')
     esr=request.POST.get('extraspaceremover','off')
     # count=request.POST.get('charcount','off')
     params={}
     print(rem)
     print(djtext)
     # remove pubctuations
     if rem=="on":
          punctuations ='''!()-[]{};:\'",.>/?@#$%^&*_~'''
          analysed=""
          for char in djtext:
               if char not in punctuations:
                    analysed=analysed+char
          params={'purpose':'Remove Punctuations','analysedtext':analysed}
          djtext=analysed
          # return render(request,"analyse.html",params)
     if caps=="on":
          analysed=""
          for char in djtext:
               analysed=analysed+char.upper()
          params={'purpose':'Changed to uppercase','analysedtext':analysed}
          djtext=analysed
          # return render(request,"analyse.html",params)
     if nlr=="on":
          analysed=""
          for char in djtext:
               if char !="\n" and char!="\r":
                    analysed=analysed+char
          params={'purpose':'removed new lines','analysedtext':analysed}
          djtext=analysed
          # return render(request,"analyse.html",params)
     if esr=="on":
          analysed=""
          for index,char in enumerate(djtext):
               if djtext[index] ==" " and djtext[index]==" ":
                    pass
               else:
                    analysed=analysed+char
          params={'purpose':'removed new lines','analysedtext':analysed}
          djtext=analysed
          # return render(request,"analyse.html",params)
     # if count=="on":
     #      c=0
     #      for char in djtext:
     #          c=c+1
     #      params={'purpose':'removed new lines','analysedtext':c}

     #      # return render(request,"analyse.html",params)
     

     if rem!="on" and caps!="on" and  nlr!="on"and  esr!="on":
          return HttpResponse("error")
     return render(request,"analyse.html",params)

# def capitalize(request):
#      return HttpResponse("capitalize")    
     
# def spaceremover(request):
#      return HttpResponse("spaceremover <a href='/' > back </a>")
     
# def newlinwremove(request):
#      return HttpResponse("newlinwremove")     
     
# def charcount(request):
#      return HttpResponse("charcount")                         