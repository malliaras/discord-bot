import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from asyncio import sleep
load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")

# εδώ θα προσθέτεις τα commands σου, π.χ.

@bot.command()
async def remind(ctx, minutes, *,message):
    time = int(minutes) * 60
    await sleep(time)
    await ctx.author.send(message) 

@bot.command()
async def poll(ctx, *message):
    if len(message) == 0:
        #πχ !poll
        await ctx.send("after '!poll' a question and choices should be provided")
        return 
    
    for i in range(len(message)):
        if i == len(message) - 1:
            if message[i][-1] == "?":
                #πχ !poll τι θα κανουμε?
                await ctx.send("Choices must be provided after the question")
                return 
            elif message[i][-1] != "?":
                #πχ !poll τι θα κανουμε βολτα net_cafe
                await ctx.send("the question should end in '?'")
                return 
            
        if message[i][-1] == "?":
            question_index = i
            break
    question = " ".join(message[:question_index + 1])
    choices = message[question_index + 1:]
    number_emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]

    if len(choices) > 10:
        #User inputs more than 10 choices
        await ctx.send("The given choices should not be more than 10")
        return 
    
    await ctx.send(question)

    index = 0
    reactions = []
    poll_message = ""
    for choice in choices:
        poll_message += f"{number_emojis[index]}: {choice}\n"
        reactions.append(number_emojis[index])
        index += 1

    new_message = await ctx.send(poll_message)
    for reaction in reactions:
        await new_message.add_reaction(reaction)
    return 


@bot.command()
async def userinfo(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
    
    join_date = user.joined_at.strftime("%d-%m-%Y")
    role_list = [role.name for role in user.roles]
    
    message = f"INFO:\n"
    message += f"Name: {user.name}\n"
    message += f"Global Name: {user.global_name}\n"
    message += f"Avatar: {user.avatar}\n"
    message += f"Roles: {" ".join(role_list)}\n"
    message += f"Member since: {join_date}\n"
    await ctx.send(message)
   
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int = None):
    if amount == None:
        await ctx.send("Type a number after '!clear'")
        return
    
    if amount <= 0:
        await ctx.send("The number of messages should be more than 0")
        return
    
    amount += 1
    await ctx.channel.purge(limit=amount) 



bot.run(TOKEN)