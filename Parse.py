file_name = "var"
file_name_ans = "ans"
with open(file_name) as f:
    content = f.readlines()

with open(file_name_ans) as f:
    answer_file = f.readlines()

lists = content
list_questions = []
quest = []

def parse_quest():
    for one_list in range(len(lists)):
        strip_query = lists[one_list]
        strip_query.strip('\n')
        if 'Задание' in strip_query:
            pass
        if 'Вопрос' in strip_query:
            questions = lists[one_list + 1].strip('\n')
            list_questions.append(questions)
        if "ответа" in strip_query:
            answer = []
            while "Задание" not in lists[one_list]:
                one_list = one_list + 1
                try:
                    answer.append(lists[one_list].split(')')[1].strip("\n"))
                except:
                    pass

                if "Конец" in lists[one_list]:
                    break
            list_questions.append(answer)

            quest.append(list_questions.copy())
            list_questions.clear()

answers = []
def parse_answer():
    for one_list in range(len(answer_file)):
        answers.append(answer_file[one_list].split(":")[1].strip("\n").split(";"))

parse_answer()
#
parse_quest()


user_quest = input('ques ')


def search(user_quest_list):
    for i in range(len(quest)):
        matching = [s for s in quest[i] if any(xs in s for xs in user_quest_list)]
        if len(matching):
            return (matching)


def start(user_quest):
    user_quest_list = []
    user_quest_list.append(user_quest)
    query = search(user_quest_list)
    for i in range(len(quest)):
        if query[0] == quest[i][0]:
            return i



def show_answer(id_answer):
    answers_list = answers[id_answer]
    quest_with_id = quest[id_answer][1]
    print(quest[id_answer][0])
    for answer in answers_list:
        if answer == '':
            continue
        print(quest_with_id[int(answer)-1])

try:
    show_answer(start(user_quest))
except:
    pass
#
# for i in list_questions:
#     if i in user_quest:
#         print(user_quest)
