from django.shortcuts import render

# Create your views here.

def amma(request):
    d={'name':'poorna'}
    return render(request,'amma.html',context=d)