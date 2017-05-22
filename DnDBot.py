# DnDBot, a Discord bot 

import discord
from discord.ext import commands

TOKEN = "MzE1OTkzOTA2Njc4NDY0NTEz.DAOz4w.H3dG-7U6rUpcIrDOAFgDV8NiGQI"
PREFIX = ";"
DESC = "DnDBot, a Discord bot"

bot = commands.Bot(command_prefix = PREFIX)

@bot.command(pass_context = True)
async def whisper(ctx, user):
	# Server deafen everyone in the voice channel except the user who used the command and the member who is passed in the function
	server = ctx.message.server
	author = ctx.message.author
	voice_channel = author.voice_channel

	if author.mute_members and author.deafen_members:
		await bot.say("You do not have the appropriate permissions for that command.")
		return
	
	for i in voice_channel.voice_members:
		if i != author and i != user:
			# Deafen the user
			await bot.server_voice_state(i, True, True)

@bot.command(pass_context = True)
async def unwhisper(ctx):
	# Unmute and undeafen literally everyone
	server = ctx.message.server
	author = ctx.message.author
	voice_channel = author.voice_channel
	
	if !author.mute_members or !author.deafen_members:
		await bot.say("You do not have the appropriate permissions for that command.")
		return

	for i in voice_channel.voice_members:
		await bot.server_voice_state(i, False, False)
	
@bot.event
async def on_command_error(error, ctx):
	await bot.send_message(ctx.message.channel, "'%s' is not a valid DnDBot command." % ctx.message.content)

bot.run(TOKEN)

