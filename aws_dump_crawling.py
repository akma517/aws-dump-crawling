# vsc에서 아나콘다 구동(ctr + shift + p)
# cmd에서 실행시킬 것

import urllib.request
from bs4 import BeautifulSoup
import pandas as PD

#url = input("크롤링할 url을 입력하세요. :")
url = "https://www.examtopics.com/exams/amazon/aws-certified-developer-associate/view/1/"
req = urllib.request.Request(url, headers={"User-Agent" : "Mozilla/5.0"})
html = urllib.request.urlopen(req).read()
soup = BeautifulSoup(html,'html.parser')

questions = soup.find_all(class_="question-body")

i = 0

columns = []
for question in questions:

    column = {}

    i = i+1

    question_text = question.find(class_="card-text").get_text().strip()
    question_text = question_text.replace(".What",". What")
    question_text = question_text.replace(".How",". How")
    question_text = question_text.replace(".Which",". Which")
    question_text = question_text.replace(".Why",". Why")
    question_text = question_text.replace(".Where",". Where")
    question_text = question_text.replace(".When",". What")

    column["INDEX"] = i
    column["QUESTION"] = question_text
    column["A"] = ""
    column["B"] = ""
    column["C"] = ""
    column["D"] = ""
    column["E"] = ""

    choice_items = question.find_all(class_="multi-choice-item")
    choice_label = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E"}
    
    j = 0

    for choice_item in choice_items:

        choice_text = choice_item.get_text().strip()
        choice_text = choice_text.split(".")[1].strip()
        column[choice_label[j]] = choice_text

        j+=1

    column["ANSWER"] = question.find(class_="correct-answer").get_text().strip()

    columns.append(column)


question_df = PD.DataFrame(columns)

question_df.to_excel("./dump.xlsx", index=False)





