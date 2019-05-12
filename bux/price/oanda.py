import json
import requests
import yaml
import pprint
import os
import mock
import time

pp = pprint.PrettyPrinter(indent=4)
mock = mock.Mock()
item = mock.create_price_stream()
while(item):
	pp.pprint(item)
	time.sleep(1)


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
						self.query_string = {'instruments': self.instrument}
						self.is_streaming = True if self.stream_base else False
				#		price_res = requests.get(self.price_stream_req_url, headers=self.headers, params=self.query_string, stream=self.is_streaming)
				#		for line in price_res.iter_lines():
				#			if line:
				#				self.decoded = line.decode('utf-8')
				#				print(json.loads(self.decoded))

		else:
			return res.status_code

