from PyQt6.QtWidgets import *
from gui import *
import csv

class GradeSubmission(QMainWindow, Ui_GradeSubmissions):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.hide_score_inputs()

        self.Submit_pushButton.clicked.connect(self.calculate_scores)

    def hide_score_inputs(self):
        self.Score1_label.setVisible(False)
        self.Score1_lineEdit.setVisible(False)
        self.Score2_label.setVisible(False)
        self.Score2_lineEdit.setVisible(False)
        self.Score3_label.setVisible(False)
        self.Score3_lineEdit.setVisible(False)
        self.AvgScore_radioButton.setVisible(False)
        self.HighScore_radioButton.setVisible(False)

    def validate_inputs(self):
        name = self.Name_lineEdit.text().strip()
        assignment = self.Assignment_lineEdit.text().strip()
        scores = []

        if not name:
            self.error_label.setText('Enter student name')
            return None, None, []
        if not assignment:
            self.error_label.setText('Enter assignment name')
            return None, None, []

        if self.Score1_lineEdit.isVisible():
            score1 = self.validate_score(self.Score1_lineEdit.text())
            scores.append(score1)
        if self.Score2_lineEdit.isVisible():
            score2 = self.validate_score(self.Score2_lineEdit.text())
            scores.append(score2)
        if self.Score3_lineEdit.isVisible():
            score3 = self.validate_score(self.Score3_lineEdit.text())
            scores.append(score3)

        return name, assignment, scores

    def validate_score(self, score):
        try:
            score = int(score)
            if 0 <= score <= 100:
                return score
            else:
                raise ValueError("Score must be between 0 and 100")
        except ValueError:
            raise ValueError("Score must be between 0 and 100")

    def calculate_scores(self):
        self.error_label.setText('')

        try:
            num = int(self.NumOfScores_lineEdit.text())
            if num < 1 or num > 3:
                raise ValueError('Enter a number between 1 and 3')

            # Set score fields visibility based on the number of scores
            if num == 1:
                self.Score1_label.setVisible(True)
                self.Score1_lineEdit.setVisible(True)
                self.Score2_label.setVisible(False)
                self.Score2_lineEdit.setVisible(False)
                self.Score3_label.setVisible(False)
                self.Score3_lineEdit.setVisible(False)
            elif num == 2:
                self.Score1_label.setVisible(True)
                self.Score1_lineEdit.setVisible(True)
                self.Score2_label.setVisible(True)
                self.Score2_lineEdit.setVisible(True)
                self.Score3_label.setVisible(False)
                self.Score3_lineEdit.setVisible(False)
            elif num == 3:
                self.Score1_label.setVisible(True)
                self.Score1_lineEdit.setVisible(True)
                self.Score2_label.setVisible(True)
                self.Score2_lineEdit.setVisible(True)
                self.Score3_label.setVisible(True)
                self.Score3_lineEdit.setVisible(True)

            name, assignment, scores = self.validate_inputs()

            if name and assignment and scores:
                if self.AvgScore_radioButton.isChecked():
                    final_score = sum(scores) / len(scores)
                elif self.HighScore_radioButton.isChecked():
                    final_score = max(scores)
                else:
                    raise ValueError('Select either Average Score or Highest Score')

                self.submit_score(name, assignment, scores, final_score)
                self.error_label.setText('Submitted')
                self.clear()

        except ValueError as e:
            self.error_label.setText(str(e))

    def submit_score(self, name, assignment, scores, final_score):
        with open('grades.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, assignment] + scores + [final_score])

    def clear(self):
        self.Name_lineEdit.clear()
        self.Assignment_lineEdit.clear()
        self.NumOfScores_lineEdit.clear()

        self.Score1_label.hide()
        self.Score1_lineEdit.clear()
        self.Score2_label.hide()
        self.Score2_lineEdit.clear()
        self.Score3_label.hide()
        self.Score3_lineEdit.clear()

        self.AvgScore_radioButton.setChecked(False)
        self.HighScore_radioButton.setChecked(False)

        self.error_label.setText('')