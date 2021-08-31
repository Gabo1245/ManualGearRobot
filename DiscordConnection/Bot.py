import discord
from discord.ext import commands
from discord.utils import get
from NetworkTable.NetworkTable import NetworkTableConnection
import time as tim

class Bot(discord.Client):
    
    def __init__(self, **options):
            super().__init__(**options)
            self.networktable = NetworkTableConnection("127.0.0.1")
            self.time = tim.time()

    async def on_ready(self):
        print ('connected!')
        self.m = await self.fetch_user(578338940797583360)
        while True:
            if int(tim.time() - self.time) % 0.5 == 0:
                await self.m.send(str(self.networktable.getTableValue('SmartDashboard', 'Shift')))


                

            
        

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
    
    
bot = Bot()
bot.run('ODY3NTQ3MTUxNDQwNTQzNzQ0.YPisPw.bF7sQrsQutJi__OSNyJAWIfn_wc')

        

