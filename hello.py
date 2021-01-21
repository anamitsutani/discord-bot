import discord
import os
import sys

from dotenv import load_dotenv
load_dotenv()

client = discord.Client()

cList = []

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    command = message.content.split(" ", maxsplit=1)
    greeting = command[0]

    if greeting.startswith('$hello'):
        await client.send_message(message.channel, 'Done sleeping')

    elif greeting.startswith('$add'):
        items = command[1].split(",")
        # cList = [items[i] for i in range(len(items))]
        for i in range(len(items)):
            item = items[i]
            cList.append(item)
        await client.send_message(message.channel, '{0} new items(s) have been added to your list, use $list items to see updated list.'.format(len(items)))
        

    elif greeting.startswith('$delete'):
        item = cList[int(command[1])]
        if item in cList:
            await client.send_message(message.channel, '"{0}" has been removed from your list, use $list items to see updated list.'.format(item))
            cList.remove(item)
        else:
            await client.send_message(message.channel, '"{0}" is not in your list, use $add items to add new itemss.'.format(item))

    elif greeting.startswith('$list'):
        # listLenght = len(cList)
        # printList = ['[{0}] {1}'.format(j, cList[j]) for j in range(listLenght)]
        printList = []
        for j in range(len(cList)):
            printList.append('[{0}] {1}'.format(j, cList[j]))
        await client.send_message(message.channel, '\n'.join(printList))

client.run(os.getenv('TOKEN'))