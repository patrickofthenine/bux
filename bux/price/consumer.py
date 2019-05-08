import asyncio
#	https://stream-fxpractice.oanda.com/
class PriceConsumer():
	async def consume_stream(message):
		reader, writer = await asyncio.open_opennection('https://stream-fxpractice.oanda.com/')
		writer.write(message.encode())
		data = await reader.read(100)
		print(f'recced: {data.decode()!r}')
		writer.close()
		await writer.wait_closed()
		return
	
asyncio.run(consume_stream('HAKDFJAKSDJFKASJDFKAJSFD'))	