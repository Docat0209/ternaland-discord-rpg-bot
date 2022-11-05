from discord.ext import commands
import discord
import requests
import io
import base64
from PIL import Image

class StableDiffusoinApi(commands.Cog):
	def __init__(self, client):
		self.client = client # sets the client variable so we can use it in cogs
	
	@commands.Cog.listener()
	async def on_ready(self):
		print("stable_diffusoin_api online")

	@commands.command()
	async def picture(self, ctx , prompt , negative_prompt):
		await ctx.send("wait")
		url = "http://127.0.0.1:7860"

		payload = {
			"prompt": prompt,
			"negative_prompt": negative_prompt,
			"steps": 20,
			"width": 960,
  			"height": 512
		}

		response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)

		r = response.json()

		payload = {
			"upscaling_resize": 2,
			"upscaler_1": "SwinIR_4x",
			"upscaler_2": "SwinIR_4x",
			"image":";,"+r["images"][0]
		}

		response = requests.post(url=f'{url}/sdapi/v1/extra-single-image', json=payload)

		r = response.json()
		
		with io.BytesIO(base64.b64decode(r["image"])) as image_binary:
			await ctx.send(file=discord.File(image_binary, 'image.png'))
	
async def setup(client):
	await client.add_cog(StableDiffusoinApi(client))
