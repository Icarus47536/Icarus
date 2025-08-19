import random
import json
from ZM_IP import *


def select_Simple(question, choices):
    if 'affected_id' not in question:
        options = list(range(1, len(question['probabilities']) + 1))
        answer = random.choices(options, weights=question['probabilities'], k=1)[0]
    else:
        affected_id = question['affected_id']  # 受影响选项ID
        affected_value = choices[f'{affected_id}'][0]  # 受影响选项答案
        options = list(range(1, len(question['probabilities'][f'{affected_value}']) + 1))
        answer = random.choices(options, weights=question['probabilities'][f'{affected_value}'], k=1)[0]
    return [answer]


def select_Multiple(question, choices):
    options = list(range(1, len(question['probabilities']) + 1))
    # 使用random.choice选出3个，可能会重复，再用random.sample确保选择的答案不重复
    sampled_elements = random.choices(options, weights=question['probabilities'], k=3)
    seen = set()
    answers = [x for x in sampled_elements if x not in seen and not seen.add(x)]
    return answers


def select_Sort(question, choices):
    options = list(range(1, len(question['probabilities']) + 1))
    answers = random.sample(options, len(question['probabilities']))
    return answers


def select_Scale(question, choices):
    options = list(range(1, len(question['probabilities']) + 1))
    answer = random.choices(options, weights=question['probabilities'], k=1)[0]
    return [answer]


def input_Gap(question, choices):
    id = random.randint(1, 3)
    answer = question['input'][f'{id}']
    return answer


class Config(object):
    def __init__(self):
        '''
        :param id: 题号
        :param type: 题目类型,Simple单选,Multiple多选,Sort排序,Scale量表,Gap填空
        :param affected_id: 受影响选项的题号
        :param probabilities: 题目选项的概率分布
        '''
        self.batch = 300
        self.proxy = True
        self.questions = [
            # #抽烟1-12 24-31
            # {
            #    "id": 1,
            #    "type": "Simple",
            #    "probabilities": [1, 0]
            # },
            # {
            #    "id": 2,
            #    "type": "Simple",
            #    "probabilities": [0.7,0.2,0.1]
            # },
            # {
            #    "id": 3,
            #    "type": "Simple",
            #    "probabilities":[0.3,0.1,0.1,0.1,0.1,0.1,0.1]
            # },
            # {
            #    "id": 4,
            #  "type": "Simple",
            #    "probabilities":[0.6,0.4]
            # },
            # {   "id": 5,
            #    "type": "Simple",
            #    "probabilities": [0,1,0,0,0,0,0]
            # },
            # {
            #    "id": 6,
            #  "type": "Simple",
            #    "probabilities": [0.4,0.5,0.1,0,0]
            # },
            # {
            #    "id": 7,
            #    "type": "Simple",
            #    "probabilities": [0.4, 0.3,0.2,0.1]
            # },
            # {
            #    "id": 8,
            #    "type":"Multiple",
            #    "probabilities":[0.2,0.2,0.2,0.2,0.2]
            # },
            # {
            #    "id": 9,
            #    "type":"Simple",
            #    "probabilities":[0.3,0.1,0.2,0.6]
            # },
            # {
            #    "id": 10,
            #    "type": "Simple",
            #    "probabilities": [0.6, 0.1, 0.1, 0.2]
            # },
            # {
            #    "id": 11,
            #    "type": "Simple",
            #    "probabilities": [0.6, 0.1, 0.1, 0.2]
            # },
            # {
            #    "id": 12,
            #    "type": "Multiple",
            #    "probabilities": [0.3,0.1,0.3,0.1,0.2]
            # },
            # {
            #    "id": 24,
            #    "type": "Multiple",
            #    "probabilities": [0.2,0.2,0.2,0.2,0.2]
            # },
            # {
            #    "id": 25,
            #    "type": "Multiple",
            #    "probabilities": [0.1, 0.2, 0.1, 0.1, 0.2, 0.3, 0]
            # },
            # {
            #    "id": 26,
            #    "type": "Simple",
            #    "probabilities": [0.2, 0.3, 0.3, 0.2]
            # },
            # {
            #    "id": 27,
            #    "type": "Simple",
            #    "probabilities": [0.2, 0.3, 0.3, 0.2]
            # },
            # {
            #    "id": 28,
            #    "type": "Simple",
            #    "probabilities": [0.2, 0.3, 0.3, 0.2]
            # },
            # {
            #    "id": 29,
            #    "type": "Multiple",
            #    "probabilities": [0.5, 0.2, 0.1, 0.1, 0.1, 0]
            # },
            # {
            #    "id": 30,
            #    "type": "Multiple",
            #    "probabilities": [0.5, 0.2, 0.1, 0.1, 0.1, 0]
            # },
            # {
            #    "id": 31,
            #    "type": "Gap",
            #    "input": {
            #        "1": ['校园应定期举办禁烟宣传活动，通过讲座和海报提高学生对吸烟危害的认识，增强大家的禁烟意识'],
            #        "2": ['设立专门的吸烟区，减少非吸烟学生接触二手烟的机会，同时加强对违规吸烟行为的监管和处罚'],
            #        "3": ['鼓励学生参与禁烟志愿服务，通过同伴教育和积极引导，共同营造一个健康、清新的校园环境']
            #     }
            # }




         # 1,13-23,24-31
             {
                 "id": 1,
                 "type": "Simple",
                 "probabilities": [0, 1]
             },
             {
                 "id": 13,
                 "type": "Simple",
                 "probabilities": [0.7, 0.1, 0.2, 0]
             },
             {
                 "id": 14,
                 "type": "Multiple",
                 "probabilities": [0.5, 0.1, 0.1, 0.1, 0.1, 0.1,0]
             },
             {
                 "id": 15,
                 "type": "Simple",
                 "probabilities": [0.5, 0.5,]
             },
             {
                 "id": 16,
                 "type": "Simple",
             "probabilities": [0,0.8,0.1,0.1,0,0]
             },
             {
                 "id": 17,
             "type": "Simple",
                 "probabilities": [0.2, 0.3, 0.3, 0.2]
             },
             {
                 "id": 18,
                 "type":  "Simple",
                 "probabilities": [0.2,0.3,0.3,0.2]
             },
             {
                 "id": 19,
                 "type":  "Simple",
                 "probabilities": [0.3,0.3,0.4,0]
             },
             {
                 "id": 20,
                 "type": "Multiple",
                 "probabilities": [0.2, 0.2, 0.2, 0.2,0.2,0]
             },
             {
                 "id": 21,
                 "type": "Simple",
                 "probabilities": [0.3, 0.3, 0.4]
             },
             {
                 "id": 22,
                 "type": "Simple",
                 "probabilities": [0.25, 0.25, 0.25, 0.25]
             },
             {
                 "id": 23,
                 "type": "Simple",
                 "probabilities": [0.3, 0.3, 0.4, 0]
             },
        {
           "id": 24,
           "type": "Multiple",
           "probabilities": [0.2,0.2,0.2,0.2,0.2]
        },
        {
           "id": 25,
           "type": "Multiple",
           "probabilities": [0.1, 0.2, 0.1, 0.1, 0.2, 0.3, 0]
        },
        {
           "id": 26,
           "type": "Simple",
           "probabilities": [0.2, 0.3, 0.3, 0.2]
        },
        {
           "id": 27,
           "type": "Simple",
           "probabilities": [0.2, 0.3, 0.3, 0.2]
        },
        {
           "id": 28,
           "type": "Simple",
           "probabilities": [0.2, 0.3, 0.3, 0.2]
        },
        {
           "id": 29,
           "type": "Multiple",
           "probabilities": [0.5, 0.2, 0.1, 0.1, 0.1, 0]
        },
        {
           "id": 30,
           "type": "Multiple",
           "probabilities": [0.5, 0.2, 0.1, 0.1, 0.1, 0]
        },
        {
           "id": 31,
           "type": "Gap",
           "input": {
               "1": ['校园应定期举办禁烟宣传活动，通过讲座和海报提高学生对吸烟危害的认识，增强大家的禁烟意识'],
               "2": ['设立专门的吸烟区，减少非吸烟学生接触二手烟的机会，同时加强对违规吸烟行为的监管和处罚'],
               "3": ['鼓励学生参与禁烟志愿服务，通过同伴教育和积极引导，共同营造一个健康、清新的校园环境']
            }
        }

        #      {
        #          "id": 24,
        #          "type": "Multiple",
        #          "probabilities": [0.3, 0.1, 0.1, 0.2, 0.1,0.2]
        #      },
        #      {
        #          "id": 25,
        #          "type": "Multiple",
        #          "probabilities": [0.1, 0.2, 0.1, 0.1, 0.2, 0.3,0]
        #      },
        #      {
        #          "id": 26,
        #          "type": "Simple",
        #          "probabilities": [0.2, 0.3, 0.3, 0.2]
        #      },
        #      {
        #          "id": 27,
        #          "type": "Simple",
        #          "probabilities": [0.2, 0.3, 0.3, 0.2]
        #      },
        #      {
        #          "id": 28,
        #          "type": "Simple",
        #          "probabilities": [0.2, 0.3, 0.3, 0.2]
        #      },
        #      {
        #          "id": 29,
        #          "type": "Multiple",
        #          "probabilities": [0.5, 0.2, 0.1, 0.1, 0.1, 0]
        #      },
        #      {
        #          "id": 30,
        #          "type": "Multiple",
        #          "probabilities": [0.5, 0.2, 0.1, 0.1, 0.1, 0]
        #      },
        #      {
        #          "id": 31,
        #          "type": "Gap",
        #          "input": {
        #     "1": ['校园应定期举办禁烟宣传活动，通过讲座和海报提高学生对吸烟危害的认识，增强大家的禁烟意识'],
        # "2": ['设立专门的吸烟区，减少非吸烟学生接触二手烟的机会，同时加强对违规吸烟行为的监管和处罚'],
        # "3": ['鼓励学生参与禁烟志愿服务，通过同伴教育和积极引导，共同营造一个健康、清新的校园环境']
        ]


# TODO 自定义测试
if __name__ == "__main__":
    config = Config()
    # 答案汇总字典
    choices = {}
    # 遍历每个题目并选择答案
    for question in config.questions:
        id = question['id']
        if question['type'] == 'Simple':
            answers = select_Simple(question, choices)
        elif question['type'] == 'Multiple':
            answers = select_Multiple(question, choices)
        elif question['type'] == 'Sort':
            answers = select_Sort(question, choices)
        elif question['type'] == 'Scale':
            answers = select_Scale(question, choices)
        elif question['type'] == 'Gap':
            answers = input_Gap(question, choices)
        choices[f'{id}'] = answers
        print(f"For question {id}, the selected answer is: {answers}")
    print('Question selection presentation：', choices)

