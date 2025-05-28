import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QFileDialog,
    QLabel, QVBoxLayout, QWidget, QMessageBox
)

# logic from other classes
from file_manager.scanner import scan_folder
from file_manager.duplicates import find_duplicates


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # creating main windows
        self.setWindowTitle("Space Manager")
        self.setFixedSize(800, 400)

        # layout
        layout = QVBoxLayout()

        # default label if no folder is selected
        self.label = QLabel("No folder selected")
        layout.addWidget(self.label)

        # select button for folder
        self.select_button = QPushButton("Select Folder")

        # links button to running logic of select_folder
        self.select_button.clicked.connect(self.select_folder)
        layout.addWidget(self.select_button)

        # runs logic for scanning duplicates
        self.scan_button = QPushButton("Scan for Duplicates")
        # enables once a folder is selected
        self.scan_button.setEnabled(False)

        # links button to running logic of scan_for_duplicates
        self.scan_button.clicked.connect(self.scan_for_duplicates)
        layout.addWidget(self.scan_button)

        # contains the layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # variable of the selected folder, default to None
        self.selected_folder = None

    def select_folder(self):

        /////
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            self.selected_folder = folder
            self.label.setText(folder)
            self.scan_button.setEnabled(True)

    def scan_for_duplicates(self):
        try:
            files = scan_folder(self.selected_folder)
            duplicates = find_duplicates(files)

            if duplicates:
                count = sum(len(v) for v in duplicates.values())
                QMessageBox.information(self, "Duplicates Found", f"Found {count} duplicate files!")
            else:
                QMessageBox.information(self, "No Duplicates", "No duplicate files found.")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to scan: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
