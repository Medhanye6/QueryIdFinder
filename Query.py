import os
import json
import random
import requests
from pathlib import Path
from telethon.sync import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import RequestWebViewRequest
from urllib.parse import unquote

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

class QueryIDExtractor:
    def __init__(self):
        self.session_path = "sessions"
        self.config_path = "config.json"
        self.devices_path = "devices.json"  # New path for devices.json

        if not Path(self.session_path).exists():
            os.makedirs(self.session_path)
        
        self.load_config()
        self.load_devices()  # Load devices information

    def load_config(self):
        if not Path(self.config_path).exists():
            raise FileNotFoundError(f"{self.config_path} file not found.")
        
        with open(self.config_path, "r") as f:
            config = json.load(f)
        
        self.api_id = config.get("api_id")
        self.api_hash = config.get("api_hash")
        
        if not self.api_id or not self.api_hash:
            raise ValueError("API ID or API Hash is missing in config.json.")

    def load_devices(self):
        if not Path(self.devices_path).exists():
            res = requests.get(
                "https://gist.githubusercontent.com/akasakaid/808a34986091b13d03b537584ea754dc/raw/b0dd89abd83c6403338ff7d6d95e0a89d159e6a2/devices.json"
            )
            Path(self.devices_path).write_text(res.text)
        
        with open(self.devices_path, "r") as f:
            self.devices = json.load(f)

    def add_session(self):
        phone = input("Enter the phone number (with country code, e.g., +1234567890): ").strip()

        model = random.choice(list(self.devices.keys()))
        system_version = self.devices[model]

        client = TelegramClient(
            str(Path(self.session_path) / f"{phone}.session"),
            api_id=self.api_id,
            api_hash=self.api_hash,
            device_model=model,
            system_version=system_version
        )

        client.connect()
        if not client.is_user_authorized():
            try:
                client.send_code_request(phone)
                otp = input('Input Login Code: ').strip()
                client.sign_in(phone=phone, code=otp)
            except SessionPasswordNeededError:
                pw2fa = input('Input 2FA Password: ').strip()
                client.sign_in(password=pw2fa)
            except Exception as e:
                print(f"Error: {e}")
                client.disconnect()
                return

        me = client.get_me()
        print(f"Logged in as {me.first_name}")

        if client.is_connected():
            client.disconnect()

    def telegram_connect(self, phone, bot_username, url):
        model = random.choice(list(self.devices.keys()))
        system_version = self.devices[model]

        client = TelegramClient(
            str(Path(self.session_path) / f"{phone}.session"),
            api_id=self.api_id,
            api_hash=self.api_hash,
            device_model=model,
            system_version=system_version
        )
        
        client.connect()
        if not client.is_user_authorized():
            print(f"Session for {phone} is not authorized.")
            client.disconnect()
            return None
        
        try:
            res = client(
                RequestWebViewRequest(
                    peer=bot_username,
                    platform="Android",
                    from_bot_menu=False,
                    bot=bot_username,
                    url=url,
                )
            )
            return res.url
        except Exception as e:
            print(f"Failed to get query_id for {phone}: {e}")
            return None
        finally:
            if client.is_connected():
                client.disconnect()

    def parse(self, url):
        query_params = unquote(url.split("#tgWebAppData=")[1].split("&tgWebAppVersion=")[0])
        return query_params

    def get_data(self):
        bot_username = input("Enter the Telegram bot username (e.g., @FirstFisher_bot): ").strip()
        if not bot_username.startswith('@'):
            print("Username should start with '@'.")
            return
        
        url = input("Enter the URL: ").strip()
        if not url:
            print("URL cannot be empty.")
            return

        sessions = Path(self.session_path).glob("*.session")
        query_data_list = []

        for session_file in sessions:
            phone = session_file.stem
            print(f"Processing {phone}")
            result = self.telegram_connect(phone, bot_username, url)
            if result:
                query_data = self.parse(result)
                query_data_list.append(query_data)
            else:
                print(f"{phone}: No result found, skipping")

        if query_data_list:
            with open("query.txt", "w") as file:
                file.write("\n".join(query_data_list))
            print("Query data saved to query.txt")
        else:
            print("No query data found.")

    def main(self):
        while True:
            clear_terminal()
            print("\nOptions:")
            print("1. Add Session")
            print("2. Get Data")
            print("3. Exit")
            choice = input("Select an option: ").strip()

            if choice == '1':
                self.add_session()
            elif choice == '2':
                self.get_data()
            elif choice == '3':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    app = QueryIDExtractor()
    app.main()
