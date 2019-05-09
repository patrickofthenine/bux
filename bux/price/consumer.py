import json
import requests
import yaml
import pprint

pp = pprint.PrettyPrinter(indent=4)

#	https://stream-fxpractice.oanda.com/
class PriceConsumer():
	def consume_stream(self):
		return;	
	def get_account_id(self):
		with open('config.yml') as yams:
			conf 				= yaml.safe_load(yams)
			oanda_conf 			= conf['oanda']
			oanda_api_config    = oanda_conf['api']
			oanda_rest_base     = oanda_api_config['rest_base']
			oanda_account_list  = oanda_api_config['paths']['rest']['account']['list']
			token 				= oanda_conf['token']
			req_url 			= oanda_rest_base + oanda_account_list
			headers 			= {'Authorization': 'Bearer %s' %token}
			print(headers)
			res = requests.get(req_url, headers=headers)
			pp.pprint(res.content)

		return;	
