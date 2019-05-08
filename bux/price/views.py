from django.shortcuts import render

# Create your views here.

def index(request):
	template = 'price/price.html'
	return render(request, template) 
