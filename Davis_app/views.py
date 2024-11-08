from django.shortcuts import render


# Create your views here.

def HomePage(request):
    return render(request, 'index.html')
def ContactPage(request):
    return render(request, 'contacts.html')
def Base(request):
    return render(request, 'base.html')
def AboutPage(request):
    return render(request, 'about.html')
