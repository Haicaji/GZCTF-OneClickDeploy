import requests
from GZCTFOneClick.Question import Question

class QuestionEditor:
    def __init__(self, domain, GZCTF_Token, games_id):
        self.domain = domain
        self.GZCTF_Token = GZCTF_Token
        self.games_id = games_id
    
    def get_question_all_id(self):
        url = f"{self.domain}/api/edit/games/{self.games_id}/challenges"
        
        headers = {
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Accept": "application/json, text/plain, */*",
        }
        
        cookies = {
            "GZCTF_Token": self.GZCTF_Token
        }
        
        try:
            response = requests.get(url, headers=headers, cookies=cookies)
            response.raise_for_status()
            challenges = response.json()
            return [challenge["id"] for challenge in challenges]
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")
            return []

    def creat_question(self, question):
        url = f"{self.domain}/api/edit/games/{self.games_id}/challenges"
        data = {
            "title": question.data["title"],
            "tag": question.data["tag"],
            "type": question.data["type"],
        }
        
        headers = {
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
        }
        
        cookies = {
            "GZCTF_Token": self.GZCTF_Token
        }
        
        try:
            response = requests.post(url, json=data, headers=headers, cookies=cookies)
            response.raise_for_status()
            question.load_data(response.text)
            return question
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")
            return None
        
    def update_question(self, question):
        url = f"{self.domain}/api/edit/games/{self.games_id}/challenges/{question.data['id']}"
        data = question.data
        
        headers = {
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
        }
        
        cookies = {
            "GZCTF_Token": self.GZCTF_Token
        }
        
        try:
            response = requests.put(url, json=data, headers=headers, cookies=cookies)
            response.raise_for_status()
            question.load_data(response.text)
            return question
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")
            return None
        
    def enable_question(self, question_id, isEnabled=True):
        url = f"{self.domain}/api/edit/games/{self.games_id}/challenges/{question_id}"
        data = {"isEnabled": isEnabled}
        
        headers = {
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
        }
        
        cookies = {
            "GZCTF_Token": self.GZCTF_Token
        }
        
        try:
            response = requests.put(url, json=data, headers=headers, cookies=cookies)
            response.raise_for_status()
            question = Question()
            question.load_data(response.text)
            return question
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")
            return None

    def delete_question(self, question_id):
        url = f"{self.domain}/api/edit/games/{self.games_id}/challenges/{question_id}"
        
        headers = {
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Accept": "application/json, text/plain, */*",
        }
        
        cookies = {
            "GZCTF_Token": self.GZCTF_Token
        }
        
        try:
            response = requests.delete(url, headers=headers, cookies=cookies)
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")
            return False