from pymongo import MongoClient
from datetime import datetime

class Database:
    def __init__(self, uri):
        self.client = MongoClient(uri)
        self.db = self.client["vexaauth"]
        self.users = self.db["users"]
        self.config = self.db["config"]

    # Users
    def add_user(self, user_id: int, oauth_token: str):
        self.users.update_one(
            {"user_id": user_id},
            {"$set": {
                "oauth_token": oauth_token,
                "authorized": True,
                "verified_at": datetime.utcnow()
            }},
            upsert=True
        )

    def get_user(self, user_id: int):
        return self.users.find_one({"user_id": user_id})

    def get_all_authorized_users(self):
        return list(self.users.find({"authorized": True}))

    # Config
    def set_log_channel(self, guild_id: int, channel_id: int):
        self.config.update_one(
            {"guild_id": guild_id},
            {"$set": {"log_channel": channel_id}},
            upsert=True
        )

    def get_log_channel(self, guild_id: int):
        data = self.config.find_one({"guild_id": guild_id})
        return data.get("log_channel") if data else None
