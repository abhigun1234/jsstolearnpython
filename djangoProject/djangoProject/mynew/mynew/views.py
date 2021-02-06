from django.shortcuts import render

def home(request):
    return render(request,'hello.html',{'titles':'hello','link':'http://youtube.com'})
def aboutUs(request):
    return  render(request,'aboutus.html',{'titles':'hello','link':'http://youtube.com'})


