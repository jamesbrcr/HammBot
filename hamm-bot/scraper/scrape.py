import requests
import json
import csv
import os
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def retrieve_messages(channelid, username, output_file, limit=1000):
    headers = {
        'authorization': os.getenv('DISCORD_AUTHORIZATION')
    }

    # Ensure the data directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Message'])

        message_count = 0
        last_message_id = None  # Used for pagination

        while message_count < limit:
            # Add the 'before' parameter for pagination
            params = {'limit': 50}
            if last_message_id:
                params['before'] = last_message_id

            r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages', headers=headers, params=params)
            if r.status_code != 200:
                print(f"Failed to retrieve messages: {r.status_code}")
                print(f"Response: {r.text}")  # Print the response for debugging
                break

            messages = json.loads(r.text)
            if not messages:
                print("No more messages found.")
                break

            for message in messages:
                if message['author']['username'] == username:
                    writer.writerow([message['content']])
                    print(f"Writing message: {message['content']}")
                    message_count += 1

                    if message_count >= limit:
                        break

            # Update the last_message_id for the next request
            last_message_id = messages[-1]['id']

            # Respect rate limits (5 requests per second)
            time.sleep(0.2)

        print(f"Total messages retrieved: {message_count}")

# Load sensitive information from environment variables
username = os.getenv('DISCORD_USERNAME')
output_file = 'hamm-bot/data/jarebear_messages_test.csv'

# general scrape
retrieve_messages(os.getenv('CHANNEL_ID_GENERAL'), username, output_file)

# plan-chat scrape
retrieve_messages(os.getenv('CHANNEL_ID_PLAN_CHAT'), username, output_file)

# mammoth scrape
retrieve_messages(os.getenv('CHANNEL_ID_MAMMOTH'), username, output_file)

# league-of-leggings scrape
retrieve_messages(os.getenv('CHANNEL_ID_LEAGUE_OF_LEGGINGS'), username, output_file)