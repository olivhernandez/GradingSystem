import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from logic import *

def main():
    application = QApplication(sys.argv)
    window = QMainWindow()

    grade_submission = GradeSubmission()
    window.setCentralWidget(grade_submission)
    grade_submission.setupUi(window)

    window.setFixedSize(291,363)
    window.show()
    sys.exit(application.exec())

if __name__ == '__main__':
    main()
