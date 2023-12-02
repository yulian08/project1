from PyQt5.QtWidgets import *

app = QApplication([])

window = QWidget()
window.resize(500,500)

lbl = QLabel("Скільки буде 2+2")
ans1 = QRadioButton("4")
ans2 = QRadioButton("14")
ans3 = QRadioButton("22")
ans4 = QRadioButton("44")


main_line = QVBoxLayout()
main_line.addWidget(lbl)

h1 = QHBoxLayout()
h2 = QHBoxLayout()
h1.addWidget(ans1)
h1.addWidget(ans2)
h2.addWidget(ans3)
h2.addWidget(ans4)

main_line.addLayout(h1)
main_line.addLayout(h2)

def true_var_1():
    msg = QMessageBox()
    msg.setText("Правильно!")
    msg.exec()

ans1.clicked.connect(true_var_1)

def false_var_1():
    msg = QMessageBox()
    msg.setText("Неправильно!")
    msg.exec()

ans2.clicked.connect(false_var_1)
ans3.clicked.connect(false_var_1)
ans4.clicked.connect(false_var_1)
window.setLayout(main_line)
window.show()
app.exec()