import requests

class OneAPIManager:
    
    cursor_models = ["claude-3-5-sonnet-20241022", 
                              "claude-3-opus", 
                              "claude-3-5-haiku", 
                              "claude-3-5-sonnet", 
                              "cursor-small", 
                              "gemini-exp-1206",
                              "gemini-2.0-flash-exp",
                              "gemini-2.0-flash-thinking-exp",
                              "gpt-3.5-turbo",
                              "gpt-4",
                              "gpt-4-turbo-2024-04-09",
                              "gpt-4o",
                              "gpt-4o-mini",
                              "o1-mini",
                              "o1-preview"]

    def __init__(self, url, access_token):
        self.base_url = url
        self.access_token = access_token
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.access_token}"
        }

    def get_channel(self, id):
        url = self.base_url + f"/api/channel/{id}"

        response = requests.get(url, headers=self.headers)
        return response

    def get_channels(self, page, pagesize):
        url = self.base_url + f"/api/channel/?p={page}&page_size={pagesize}"

        response = requests.get(url, headers=self.headers)
        return response

    def add_channel(self, name, base_url, keys, models, rate_limit_count = 0):
        url = self.base_url + "/api/channels"

        data = {
            "name": name,
            "type": "openai",
            "baseURL": base_url,
            "models": models,
            "keys": keys,
            "priority": 0,
            "weight": 1,
            "rateLimit": rate_limit_count,
            "rateLimitDuration": 60,
            "groups": ["default"],
            "labels": ["Cursor"],
            "status": "active"
        }

        response = requests.post(url, json=data, headers=self.headers)
        return response
    
    def delete_channel(self, id):
        url = self.base_url + f"/api/channel/{id}"

        response = requests.delete(url, headers=self.headers)
        return response
