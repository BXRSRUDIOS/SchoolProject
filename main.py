### IMPORTS ###
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
import random as rd, time
### Create App ##
app = QApplication([])
main_win = QWidget()


### Creating Question Form
main_win.setWindowTitle("Memory Card Application")
question = QLabel("Which Nationality does not exist?")
RadioGroupBox = QGroupBox('Answer Options:')
rbtn_1 = QRadioButton('Enets')
rbtn_2 = QRadioButton('Aleuts')
rbtn_3 = QRadioButton('Chulyums')
rbtn_4 = QRadioButton('Smurfs')
answerButton = QPushButton('Answer')
layout_main = QVBoxLayout()
layout_main.addWidget(question, alignment = Qt.AlignHCenter)
layout_main.addWidget(RadioGroupBox, alignment = Qt.AlignHCenter)
layout_sub1 = QHBoxLayout()
layout_sub2 = QHBoxLayout()
layout_sub3 = QVBoxLayout()
layout_sub1.addWidget(rbtn_1, alignment = Qt.AlignHCenter)
layout_sub1.addWidget(rbtn_2, alignment = Qt.AlignHCenter)
layout_sub2.addWidget(rbtn_3, alignment = Qt.AlignHCenter)
layout_sub2.addWidget(rbtn_4, alignment = Qt.AlignHCenter)
layout_sub3.addLayout(layout_sub1)
layout_sub3.addLayout(layout_sub2)
RadioGroupBox.setLayout(layout_sub3)

class Question:
    def __init__(self, questions, right_answer, wrong1, wrong2, wrong3):
        self.questions = questions
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

'''
RadioGroupBox.hide()
answerButton.hide()
question.hide()
'''

# FOR LATER
style = '''
QLabel {
    font-size: 20px;
}
QWidget {
    color: black; 
} 

QPushButton {
    background-color: black;
    font-size: 10px;
    color: white;
    width: 50px;
    height: 30px;
}
QPushButton:hover {
    background-color: gray;
    color: white;
    font-size: 10px;
}

QGroupBox {
    color: black;
}

'''
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

def show_question():
    RadioGroupBox.show()
    RadioGroupBox2.hide()
    question.show()
    answerButton.setText("Answer")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
    answerButton.show()
    answerTitle.hide()

'''
def show_answer():
    RadioGroupBox2.show()
    RadioGroupBox.hide()
    question.hide()
    answerTitle.show()
    answerButton.show()
    answerButton.setText("Next Question")
'''

answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]  
def ask(q: Question):
    global answer
    rd.shuffle(answer)
    question.setText(q.questions)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    question.show()

main_win.total = 0
main_win.score = 0
def check_answer():
    if answer[0].isChecked():
        main_win.total += 1
        main_win.score += 1
        print(f"Current Score: {main_win.score},\nTotal Qs So Far: {main_win.total},\nPercentage: {(main_win.score / main_win.total) * 100}%")
        show_correct(f"Correct ")
    else:
        main_win.total += 1
        print(f"Current Score: {main_win.score},\nTotal Qs So Far: {main_win.total},\nPercentage: {(main_win.score / main_win.total) * 100}%")
        show_correct(f"Incorrect")
    RadioGroupBox2.show()
    RadioGroupBox.hide()
    

def show_correct(res):
    correct_mention.setText(f"Your Answer is {res}\n\nStatistics:\n\nScore: {main_win.score}\nTotal Amount of Questions: {main_win.total}\n\nPercentage of Results: {(main_win.score / main_win.total) * 100}%")
    question.hide()
    answerTitle.show()
    answerButton.setText("Next Question")


def click():
    if answerButton.text() == "Answer":
        check_answer()
    else:
        next_question()

def quitter():
    quit()

asked_q = []
questions_list = []
q = Question("The National Language of Brazil", "Portuguese", "Italian", "Brazillian", "CookeyLang")
questions_list.append(Question("The National Language of Brazil", "Portuguese", "Italian", "Brazillian", "CookeyLang"))
questions_list.append(Question("The Programming Language used to program this app is what?", "Python", "Ruby", "C#", "C++"))
questions_list.append(Question("What is 2+2+2 Squared?", "36", "24", "12", "60"))
questions_list.append(Question("What here is the odd one out?", "Box", "Table", "Chair", "Wardrobe"))
questions_list.append(Question("What programming language doesn't exist?", "DSTRUCTURES", "Crystal", "CookeyLang", "E"))
questions_list.append(Question("What is Love?", "Baby Don't Hurt me", "Don't hurt me", "Don't", "I am crazy..."))
questions_list.append(Question("Is LolCode a Language?", "Yes", "No", "Maybe", "Eggs"))
questions_list.append(Question("Avoir, what does this mean in English?", "To Have", "To Be", "To Go", "To Sell"))
questions_list.append(Question("Why should you like this Quiz", "Cause It's Nice", "Cause It's Bad", "Beans And Eggs", "Cause We Love Code"))
for i in range(1,5):
    rd.shuffle(questions_list)


main_win.cur_question = -1
ask(questions_list[main_win.cur_question])
def next_question():
    main_win.cur_question += 1
    RadioGroupBox.show()
    RadioGroupBox2.hide()
    answerButton.setText("Answer")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
    answerTitle.hide()
    if main_win.cur_question == len(questions_list):
        main_win.cur_question = -1
        answerButton.clicked.connect(quitter)
    ask(questions_list[main_win.cur_question])
# Creating Answer Form
answerTitle = QLabel("Answer Form")
RadioGroupBox2 = QGroupBox('Test Result')
correct_mention = QLabel("The Answer Will Be Here -> Aleuts")



layout_main.addWidget(answerTitle, alignment = Qt.AlignHCenter)
layout_main.addWidget(RadioGroupBox2, alignment = Qt.AlignHCenter)

layout_sub4 = QHBoxLayout()
layout_sub5 = QHBoxLayout()
layout_sub6 = QVBoxLayout()
layout_sub5.addWidget(correct_mention, alignment=Qt.AlignHCenter)

layout_sub6.addLayout(layout_sub4)
layout_sub6.addLayout(layout_sub5)
RadioGroupBox2.setLayout(layout_sub6)

layout_main.addWidget(answerButton, alignment = Qt.AlignHCenter)
# main_win.setStyleSheet(style)

answerButton.clicked.connect(click)

main_win.setLayout(layout_main)
layout_main.addWidget(answerButton, alignment = Qt.AlignHCenter)

RadioGroupBox.show()
RadioGroupBox2.hide()
answerTitle.hide()
### Execute App ###
main_win.show()
app.exec_()