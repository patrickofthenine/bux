import json
import requests
import yaml

#	https://stream-fxpractice.oanda.com/
class PriceConsumer():
	def consume_stream(self):
		return;	
	def get_account_id(self):
		with open('config.yml') as yams:
			conf = yaml.safe_load(yams)
			print(conf)
		return;	
