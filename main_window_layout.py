from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,QSpinBox,QVBoxLayout ,
                             QHBoxLayout , QLabel ,  QWidget, QRadioButton,
                             QButtonGroup,QGroupBox, QPushButton)
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory card')
main_win.resize(400,400)


qtext = QLabel('Питання')
v_line = QVBoxLayout()
rbtn1 = QRadioButton('')
rbtn2 = QRadioButton('')
rbtn3 = QRadioButton('')
rbtn4 = QRadioButton('')
RadioGroupBox = QGroupBox('Варіанти відповідей')
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()


layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

btn_menu = QPushButton('Меню')
btn_sleep = QPushButton('Відпочити')
box_Minutes = QSpinBox()
box_Minutes.setValue(30)
btn_OK=QPushButton('Відповісти')

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()

layout_line1.addWidget(btn_menu)
layout_line1.addWidget(btn_sleep)
layout_line1.addWidget(box_Minutes)
layout_line2.addWidget(qtext,alignment=Qt.AlignHCenter | Qt.AlignVCenter)
layout_line3.addWidget(RadioGroupBox)
layout_line4.addWidget(btn_OK,alignment=Qt.AlignCenter)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)
layout_card.addLayout(layout_line4)






main_win.setLayout(layout_card)

main_win.show()
app.exec_()