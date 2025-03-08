from GZCTFOneClick.Question import Question
from GZCTFOneClick.QuestionEditor import QuestionEditor

class GameEditor:
    def __init__(self, domain, GZCTF_Token, games_id):
        self.domain = domain
        self.GZCTF_Token = GZCTF_Token
        self.games_id = games_id
    
    def delete_all_question(self):
        editor = QuestionEditor(self.domain, self.GZCTF_Token, self.games_id)
        for question_id in editor.get_question_all_id():
            editor.delete_question(question_id)

    def enable_all_question(self):
        editor = QuestionEditor(self.domain, self.GZCTF_Token, self.games_id)
        for question_id in editor.get_question_all_id():
            editor.enable_question(question_id)