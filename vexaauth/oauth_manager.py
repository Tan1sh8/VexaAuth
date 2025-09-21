class OAuthManager:
    def __init__(self, client_id, client_secret, redirect_uri, database):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.db = database

    def generate_link(self):
        return f"https://discord.com/oauth2/authorize?client_id={self.client_id}&scope=identify&response_type=code&redirect_uri={self.redirect_uri}"

    def save_token(self, user_id, oauth_token):
        self.db.add_user(user_id, oauth_token)
