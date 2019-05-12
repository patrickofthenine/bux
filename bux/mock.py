import json
import requests
import yaml
import pprint
import os
import datetime
import time
import random

pp = pprint.PrettyPrinter(indent=4)

class Mock():
	def create_price_stream_item(self, min, max, step):
			#type
			self.type   = 'PRICE'
			#time
			self.time	= datetime.datetime.today()
			self.min  	= min*100
			self.max  	= max*100
			self.step 	= step
			#bids - less than asks
			self.bid 			= random.randrange(self.min, self.max, self.step)
			self.bid_liquidity 	= random.randrange(1, 10000000, 1)
			self.closeout_bid  	= random.randrange(0, self.bid, self.step)
			#asks - more than bids
			self.ask 			= random.randrange(self.bid, self.max, self.step)
			self.ask_liquidity 	= random.randrange(1, 10000000, 1)
			self.closeout_ask  	= random.randrange(self.ask, self.max, self.step)
			#statuses
			self.status 		= 'tradeable' if random.randrange(1,100,1) >= 50 else 'non-tradeable'
			#tradeable
			self.tradeable      = True if self.status == 'tradeable' else False
			#instrument
			self.currencies  = ['EUR', 'USD', 'GBP', 'AUD', 'CAD', 'JPY']
			self.base_index  = random.randrange(0, len(self.currencies)-1)
			self.base        = self.currencies[slice(self.base_index, self.base_index+1)] 
			self.quote_index = random.randrange(0, len(self.currencies)-1)
			self.quote       = self.currencies[slice(self.quote_index, self.quote_index+1)]

			self.price_stream_item = {
				'type': self.type,
				'time': self.time,
				'bids': [{'price': self.bid/100, 'liquidity': self.bid_liquidity}],
				'asks': [{'price': self.ask/100, 'liquidity': self.ask_liquidity}],
				'closeoutBid': self.closeout_bid/100,
				'closeoutAsk': self.closeout_ask/100,
				'status': self.status,
				'tradeable': self.tradeable,
				'instrument': self.base[0] + '_' + self.quote[0]       
			}
			return self.price_stream_item

	def create_price_stream(self):
		self.price_stream_item = self.create_price_stream_item(0, 100, 1)
		pp.pprint(self.price_stream_item)
		return self.price_stream_item

