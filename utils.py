import requests
import aiofiles
import asyncio

def getRoles(TOKEN, GUILD_ID):
    URL = f'https://discord.com/api/v10/guilds/{GUILD_ID}/roles'

    headers = {
        'Authorization': TOKEN
    }

    response = requests.get(URL, headers=headers)

    if response.status_code == 200:
        roles = response.json()
        roles = {x['id']: {"name": x["name"], "position": x['position']} for x in roles}
        return roles
    else:
        print(f'Ошибка при получении ролей: {response.status_code}')

async def async_save_urls(lock, twitter_urls):
    async with aiofiles.open('output.txt', 'w', encoding='utf-8') as file:
        with lock:
            current_urls = twitter_urls.copy()
        for item in current_urls:
            await file.write(f"{item}\n")

def save_urls_background(lock, twitter_urls):
    asyncio.run(async_save_urls(lock, twitter_urls))
