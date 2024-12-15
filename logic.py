from PyQt6.QtWidgets import *
from gui import *
import csv
import os

class GradeSubmission(QMainWindow, Ui_GradeSubmissions):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.clear_score_inputs()
        self.add_csv_header()
        self.Submit_pushButton.clicked.connect(self.calculate_scores)
        self.NumOfScores_lineEdit.textChanged.connect(self.update_score_inputs)

    def clear_score_inputs(self):
        self.Score1_label.hide()
        self.Score1_lineEdit.clear()
        self.Score1_lineEdit.hide()
        self.Score2_label.hide()
        self.Score2_lineEdit.clear()
        self.Score2_lineEdit.hide()
        self.Score3_label.hide()
        self.Score3_lineEdit.clear()
        self.Score3_lineEdit.hide()
        self.AvgScore_radioButton.hide()
        self.HighScore_radioButton.hide()

    def update_score_inputs(self):
        try:
            self.clear_score_inputs()
            num = int(self.NumOfScores_lineEdit.text().strip() or 0)  # Safely parse as integer
            if num == 1:
                self.Score1_label.show()
                self.Score1_lineEdit.show()
            elif num == 2:
                self.Score1_label.show()
                self.Score1_lineEdit.show()
                self.Score2_label.show()
                self.Score2_lineEdit.show()
            elif num == 3:
                self.Score1_label.show()
                self.Score1_lineEdit.show()
                self.Score2_label.show()
                self.Score2_lineEdit.show()
                self.Score3_label.show()
                self.Score3_lineEdit.show()
            else:
                raise ValueError('Enter a number between 1-3')
        except ValueError as e:
            self.error_label.setText(str(e))

    def validate_inputs(self):
        self.error_label.setText('')
        name = self.Name_lineEdit.text().strip()
        assignment = self.Assignment_lineEdit.text().strip()
        scores = []

        if not name:
            self.error_label.setText('Enter student name')
            return None, None, []
        if not assignment:
            self.error_label.setText('Enter assignment name')
            return None, None, []

        try:
            if self.Score1_lineEdit.isVisible():
                scores.append(self.validate_score(self.Score1_lineEdit.text()))
            if self.Score2_lineEdit.isVisible():
                scores.append(self.validate_score(self.Score2_lineEdit.text()))
            if self.Score3_lineEdit.isVisible():
                scores.append(self.validate_score(self.Score3_lineEdit.text()))
        except ValueError as e:
            self.error_label.setText(str(e))
            return None, None, []

        return name, assignment, scores

    def validate_score(self, score):
        if not score.strip():
            raise ValueError("Score cannot be blank")
        try:
            score = int(score)
            if 0 <= score <= 100:
                return score
            else:
                raise ValueError("Score must be between 0 and 100")
        except ValueError:
            raise ValueError("Score must be a valid number between 0 and 100")

    def calculate_scores(self):
        self.error_label.setText('')
        try:
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

    def add_csv_header(self):
        if not os.path.exists('grades.csv'):
            with open('grades.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Name', 'Assignment', 'Score 1', 'Score 2', 'Score 3', 'Final Score'])

    def submit_score(self, name, assignment, scores, final_score):
        with open('grades.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            row = [name, assignment] + scores + [final_score]
            writer.writerow(row)

    def clear(self):
        self.Name_lineEdit.clear()
        self.Assignment_lineEdit.clear()
        self.NumOfScores_lineEdit.clear()
        self.clear_score_inputs()
        self.AvgScore_radioButton.setChecked(True)
        self.HighScore_radioButton.setChecked(False)
        self.error_label.setText('')
