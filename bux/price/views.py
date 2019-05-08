from django.shortcuts import render
from . import consumer

consumer.PriceConsumer().consume_stream()
# Create your views here.

def index(request):
	template = 'price/price.html'
	return render(request, template) 
