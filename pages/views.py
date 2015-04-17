from django.shortcuts import render


def index(request):
	return render(request, 'pages/home.html', {})

    
def about(request):
	return render(request, 'pages/about.html', {})

    
def contact(request):
	return render(request, 'pages/contact.html', {})

    
def help(request):
	return render(request, 'pages/help.html', {})
