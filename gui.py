# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(305, 428)
        self.centralwidget = QtWidgets.QWidget(parent=mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Name_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.Name_label.setGeometry(QtCore.QRect(40, 30, 81, 20))
        self.Name_label.setObjectName("Name_label")
        self.Name_lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Name_lineEdit.setGeometry(QtCore.QRect(130, 30, 113, 20))
        self.Name_lineEdit.setObjectName("Name_lineEdit")
        self.Assignmentlabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.Assignmentlabel.setGeometry(QtCore.QRect(50, 60, 71, 20))
        self.Assignmentlabel.setObjectName("Assignmentlabel")
        self.Assignment_lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Assignment_lineEdit.setGeometry(QtCore.QRect(130, 60, 113, 20))
        self.Assignment_lineEdit.setObjectName("Assignment_lineEdit")
        self.Num_scores_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.Num_scores_label.setGeometry(QtCore.QRect(60, 90, 61, 20))
        self.Num_scores_label.setObjectName("Num_scores_label")
        self.One_radioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.One_radioButton.setGeometry(QtCore.QRect(130, 90, 82, 17))
        self.One_radioButton.setObjectName("One_radioButton")
        self.NumScores_buttonGroup = QtWidgets.QButtonGroup(mainWindow)
        self.NumScores_buttonGroup.setObjectName("NumScores_buttonGroup")
        self.NumScores_buttonGroup.addButton(self.One_radioButton)
        self.Two_radioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.Two_radioButton.setGeometry(QtCore.QRect(130, 110, 82, 17))
        self.Two_radioButton.setObjectName("Two_radioButton")
        self.NumScores_buttonGroup.addButton(self.Two_radioButton)
        self.Three_radioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.Three_radioButton.setGeometry(QtCore.QRect(130, 130, 82, 17))
        self.Three_radioButton.setObjectName("Three_radioButton")
        self.NumScores_buttonGroup.addButton(self.Three_radioButton)
        self.Score1_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.Score1_label.setGeometry(QtCore.QRect(80, 150, 47, 13))
        self.Score1_label.setObjectName("Score1_label")
        self.Score2_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.Score2_label.setGeometry(QtCore.QRect(80, 180, 47, 13))
        self.Score2_label.setObjectName("Score2_label")
        self.Score3_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.Score3_label.setGeometry(QtCore.QRect(80, 210, 47, 13))
        self.Score3_label.setObjectName("Score3_label")
        self.Score1_lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Score1_lineEdit.setGeometry(QtCore.QRect(130, 150, 113, 20))
        self.Score1_lineEdit.setObjectName("Score1_lineEdit")
        self.Score2_lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Score2_lineEdit.setGeometry(QtCore.QRect(130, 180, 113, 20))
        self.Score2_lineEdit.setObjectName("Score2_lineEdit")
        self.Score3_lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Score3_lineEdit.setGeometry(QtCore.QRect(130, 210, 113, 20))
        self.Score3_lineEdit.setObjectName("Score3_lineEdit")
        self.AvgScore_radioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.AvgScore_radioButton.setGeometry(QtCore.QRect(40, 260, 101, 17))
        self.AvgScore_radioButton.setObjectName("AvgScore_radioButton")
        self.ScoreSubmit_buttonGroup = QtWidgets.QButtonGroup(mainWindow)
        self.ScoreSubmit_buttonGroup.setObjectName("ScoreSubmit_buttonGroup")
        self.ScoreSubmit_buttonGroup.addButton(self.AvgScore_radioButton)
        self.HighScore_radioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.HighScore_radioButton.setGeometry(QtCore.QRect(160, 260, 101, 17))
        self.HighScore_radioButton.setObjectName("HighScore_radioButton")
        self.ScoreSubmit_buttonGroup.addButton(self.HighScore_radioButton)
        self.Submit_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Submit_pushButton.setGeometry(QtCore.QRect(100, 290, 75, 23))
        self.Submit_pushButton.setObjectName("Submit_pushButton")
        self.error_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.error_label.setGeometry(QtCore.QRect(40, 320, 201, 51))
        self.error_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.error_label.setObjectName("error_label")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 305, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Grading Submissions"))
        self.Name_label.setText(_translate("mainWindow", "Student Name:"))
        self.Assignmentlabel.setText(_translate("mainWindow", "Assignemnt:"))
        self.Num_scores_label.setText(_translate("mainWindow", "# of Scores:"))
        self.One_radioButton.setText(_translate("mainWindow", "One"))
        self.Two_radioButton.setText(_translate("mainWindow", "Two"))
        self.Three_radioButton.setText(_translate("mainWindow", "Three"))
        self.Score1_label.setText(_translate("mainWindow", "Score 1:"))
        self.Score2_label.setText(_translate("mainWindow", "Score 2:"))
        self.Score3_label.setText(_translate("mainWindow", "Score 3:"))
        self.AvgScore_radioButton.setText(_translate("mainWindow", "Average Score"))
        self.HighScore_radioButton.setText(_translate("mainWindow", "Highest Score"))
        self.Submit_pushButton.setText(_translate("mainWindow", "SUBMIT"))
        self.error_label.setText(_translate("mainWindow", " "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec())
