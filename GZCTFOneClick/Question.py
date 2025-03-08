import json

class Question:
    def __init__(self):
        self.data = {
            "id": None,
            "title": "",
            "content": "",
            "tag": "",
            "type": "",
            "hints": [],
            "flagTemplate": None,
            "isEnabled": False,
            "containerImage": "",
            "memoryLimit": 64,
            "cpuCount": 1,
            "storageLimit": 256,
            "containerExposePort": 80,
            "enableTrafficCapture": False,
            "originalScore": 500,
            "minScoreRate": 0.25,
            "difficulty": 5,
            "acceptedCount": 0,
            "fileName": "attachment",
            "attachment": None,
            "testContainer": None,
            "flags": []
        }

    def load_data(self, data):
        if isinstance(data, str):
            try:
                self.data = json.loads(data)
            except json.JSONDecodeError as e:
                raise ValueError(f"无效的JSON字符串: {e}")
        elif isinstance(data, dict):
            self.data = data
        else:
            raise TypeError("数据必须是JSON字符串或字典")
    
    def get_data(self):
        return json.dumps(self.data)

    def __str__(self):
        return str(self.data)
