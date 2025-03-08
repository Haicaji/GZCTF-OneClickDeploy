from GZCTFOneClick.QuestionEditor import QuestionEditor
from GZCTFOneClick.Question import Question
from GZCTFOneClick.GameEditor import GameEditor

def get_content(i):
    if i > 17:
        return "None"
    try:
        filepath = ".\content.txt"
        with open(filepath, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        if 0 <= i < len(lines):
            return lines[i].strip()
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None


# 示例
if __name__ == "__main__":
    # 抓个包这些就可以知道
    domain = ""
    GZCTF_Token = ""
    games_id = 1

    # 删除所有题目
    game_editor = GameEditor(domain, GZCTF_Token, games_id)
    game_editor.delete_all_question()

    question_editor = QuestionEditor(domain, GZCTF_Token, games_id)
    # 批量加载 PHPinclude-labs 的题目
    for i in range(24):
        question = Question()
        question.data["title"] = f"Level {i}"
        question.data["tag"] = "Web"
        question.data["type"] = "DynamicContainer"
        question = question_editor.creat_question(question)

        if question is None:
            continue

        print(f"创建题目: {question.data['title']}")

        # 完善题目信息
        question.data["content"] = get_content(i)
        question.data["containerImage"] = f"include_labs:v{i}"

        question = question_editor.update_question(question)
        if question is None:
            continue

        print(f"完善题目信息: {question.data['title']}")

    # 启用所有题目
    game_editor.enable_all_question()
