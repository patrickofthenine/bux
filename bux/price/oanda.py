import json
import requests
import yaml
import pprint
import os

pp = pprint.PrettyPrinter(indent=4)

#	https://stream-fxpractice.oanda.com/
class OANDA():
	def consume_stream(self):
		return;	
	def get_account(self):
		#get yaml	
		with open('config.yml') as yams:
			self.conf 				= yaml.safe_load(yams)
			self.oanda_conf 		= self.conf['oanda']
			self.oanda_api_config   = self.oanda_conf['api']
			self.oanda_rest_base    = self.oanda_api_config['rest_base']
			self.oanda_account_list = self.oanda_api_config['paths']['rest']['account']['list']
			self.token 				= self.oanda_conf['token'] if self.oanda_conf['token'] else os.environ['OANDA_TOKEN']
			self.req_url 			= self.oanda_rest_base + self.oanda_account_list
			self.headers 			= {'Authorization': 'Bearer %s' %self.token}
			
		##make request
		res = requests.get(self.req_url, headers=self.headers)

		if(res.status_code == 200):
			# returns a list of accounts; using first
			if json.loads(res.content):
				instruments = []
				#get instruments we can trade
				self.account_id 			= json.loads(res.content)['accounts'][0]['id']
				self.instrument_list_path   = self.oanda_api_config['paths']['rest']['account']['instruments'].format(self.account_id)
				self.instrument_req_url     = self.oanda_rest_base + self.instrument_list_path
				instruments_res = requests.get(self.instrument_req_url, headers=self.headers)
				if json.loads(instruments_res.content):
					self.instruments = json.loads(instruments_res.content)['instruments']
					for self.instrument in self.instruments:
						self.instrument_name = self.instrument['name']
						instruments.append(self.instrument_name)


				#for price stream
				self.stream_base    	= self.oanda_api_config['streaming_base']
				self.price_stream_path 	= self.oanda_api_config['paths']['stream']['account']['price'].format(self.account_id)
				self.price_stream_req_url = self.stream_base + self.price_stream_path

				for self.instrument in instruments:
					if self.instrument == 'EUR_USD':
						print(self.instrument)
						#create price query parameters
						#create price stream req url
						#consume stream

		else:
			return res.status_code

