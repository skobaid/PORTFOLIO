from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render (request, 'main/about.html', )

def services(request):
    return render (request, 'main/services.html', )

    
def portfolio(request):
    return render (request, 'main/portfolio.html', )

        
def blogs(request):
    return render (request, 'main/blog.html', )

def contact(request):
    return render (request, 'main/contact.html', )