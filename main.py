import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from logic import GradeSubmission

def main():
    application = QApplication(sys.argv)
    window = QMainWindow()

    grade_submission = GradeSubmission()
    window.setCentralWidget(grade_submission)
    window.setWindowTitle("Grading Submissions")
    window.setFixedSize(305,428)

    window.show()
    sys.exit(application.exec())

if __name__ == '__main__':
    main()
