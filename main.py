from telethon import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
import json
import asyncio


api_id = 24918248
api_hash = "5152db285d52601273a81e40e24c62a0"
group_users = -1001860640156
client = TelegramClient('session', api_id, api_hash)


# 1st task
async def main():
    await client.start()
    offset = 0
    users = []
    user_details = {}
    while True:
        participants = await client(GetParticipantsRequest(group_users, ChannelParticipantsSearch(''), 
                                                           offset=offset, limit=200, hash=0))
        users.extend(participants.users)
        offset += len(participants.users)
        if not participants.users:
            break

    for user in users:
        user_details[user.username] = {
        "name": user.first_name,
        "last_name": user.last_name
    }
        
    with open('user_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(user_details, json_file, ensure_ascii=False, indent=4)



# 2nd task
    with open('user_data.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    file_name = ''
    for username, data in data.items():
        name = data['name'] if 'name' in data else None
        if name:
            try:
                last_letter = name[-1].lower()
                if last_letter in 'aeiouаеёиоуыэюя':
                    file_name = 'female.txt'
                else:
                    file_name = 'male.txt'
            except Exception:
                file_name = 'male.txt' 
        else:
            file_name = 'male.txt'
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(f'{username}\n')

        

if __name__ == '__main__':
    asyncio.run(main())
