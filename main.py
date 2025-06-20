import threading
from utils import getRoles, save_urls_background
from config import TOKEN, GUILD_ID, CHANNEL_ID, ROLES, TIMEOUT_ACCOUNT
import discum
import time

bot = discum.Client(token=TOKEN, log=False)

roles = getRoles(TOKEN, GUILD_ID)
NEED_ROLE = [x for x in roles if roles[x]['name'] in ROLES]
print(NEED_ROLE)

handler_executed = False

twitter_urls = []

lock = threading.Lock()

@bot.gateway.command
def on_ready(resp):
    global handler_executed
    if handler_executed:
        return

    if resp.event.ready_supplemental:
        print("Вход в Дискорд аккаунт успешно выполнен!")
        print("Получаем пользователей канала...")
        bot.gateway.fetchMembers(GUILD_ID, CHANNEL_ID, keep='all', wait=1)


    if bot.gateway.finishedMemberFetching(GUILD_ID):
        handler_executed = True
        members = bot.gateway.session.guild(GUILD_ID).members
        members_id = [x for x in members if set(members[x]['roles']) & set(NEED_ROLE)]
        print(f"Пользователи успешно найдены ({len(members_id)} шт.)")

        print(f"0/{len(members_id)} (0 ссылок)", end="")

        count_processed = 0

        for member_id in members_id:
            while True:
                try:
                    connected_accounts = bot.getProfile(member_id)
                    if connected_accounts.status_code == 429:
                        print("Аккаунт заморожен...")
                        exit(0)

                    for conn_acc in connected_accounts.json()['connected_accounts']:
                        if conn_acc['type'] == 'twitter':
                            twitter_urls.append("https://x.com/" + conn_acc['name'])

                    break
                except KeyError as e:
                    continue

            save_urls_background(lock, twitter_urls)

            count_processed += 1
            print(f"\r{count_processed}/{len(members_id)} ({len(twitter_urls)} ссылок)", end="")

            time.sleep(TIMEOUT_ACCOUNT - 0.5)


        bot.gateway.removeCommand(on_ready)
        bot.gateway.close()

bot.gateway.run()








