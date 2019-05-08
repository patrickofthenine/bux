from django.db import models

# Create your models here.
class Account(models.Model):
	account_id: models.CharField(max_length=255)


class Price(models.Model):
	price_type: 	models.CharField(max_length=255)
	instrument: 	models.CharField(max_length=255)
	time:       	models.DateField()
	status:     	models.CharField(max_length=255)
	tradeable:  	models.BooleanField(default=False)
	bids:			models.FloatField()
	asks: 			models.FloatField()	
	closeoutBid: 	models.FloatField()
	closeoutAsk: 	models.FloatField()
