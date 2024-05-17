import os
import sys
import datetime
import time
import json
import multiprocessing
import re
from functools import partial
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem, QFileDialog, QMessageBox, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget, QTreeWidget, QLabel
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QMetaObject, Q_ARG
from PyQt5 import uic
from tqdm import tqdm

def worker(folder_path):
    folders = []
    for entry in os.scandir(folder_path):
        if entry.is_dir():
            folders.append(entry.path)
    return folders

class FolderLister(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()

        buttons_layout = QHBoxLayout()
        self.addFolderButton = QPushButton("Add Directory")
        buttons_layout.addWidget(self.addFolderButton)
        self.removeFolderButton = QPushButton("Remove Directory")
        buttons_layout.addWidget(self.removeFolderButton)
        main_layout.addLayout(buttons_layout)

        directory_label = QLabel("Added Directories:")
        main_layout.addWidget(directory_label)

        self.directoryListWidget = QListWidget()
        main_layout.addWidget(self.directoryListWidget)
        self.directoryListWidget.setFixedHeight(100)

        bottom_buttons_layout = QHBoxLayout()
        self.startButton = QPushButton("Start")
        bottom_buttons_layout.addWidget(self.startButton)
        self.openButton = QPushButton("Open Selected Folders")
        bottom_buttons_layout.addWidget(self.openButton)
        self.exportButton = QPushButton("Export List")
        bottom_buttons_layout.addWidget(self.exportButton)
        main_layout.addLayout(bottom_buttons_layout)

        self.treeWidget = QTreeWidget()
        self.treeWidget.setHeaderLabels(["Folder Name", "Size (GB)", "Date Last Modified", "Path"])
        self.treeWidget.setSortingEnabled(True)
        self.treeWidget.header().setSortIndicator(0, Qt.AscendingOrder)
        self.treeWidget.header().setSectionsClickable(True)
        self.treeWidget.header().sectionClicked.connect(lambda column: self.sort_by(column))
        self.treeWidget.setSelectionMode(QTreeWidget.ExtendedSelection)
        self.treeWidget.itemDoubleClicked.connect(self.open_folder)
        main_layout.addWidget(self.treeWidget)

        search_layout = QHBoxLayout()
        self.searchLineEdit = QLineEdit()
        search_label = QLabel("Search:")
        search_layout.addWidget(search_label)
        search_layout.addWidget(self.searchLineEdit)
        self.searchButton = QPushButton("Search")
        search_layout.addWidget(self.searchButton)
        main_layout.addLayout(search_layout)

        self.searchLineEdit.returnPressed.connect(self.search_folders)

        self.startButton.clicked.connect(self.start)
        self.addFolderButton.clicked.connect(self.add_folder)
        self.removeFolderButton.clicked.connect(self.remove_folder)
        self.searchButton.clicked.connect(self.search_folders)
        self.openButton.clicked.connect(self.open_selected_folders)
        self.exportButton.clicked.connect(self.export_list)

        self.setWindowTitle("Folder Lister")

        self.load_directories()
        self.load_cache()

        self.folder_cache = {}
        central_widget.setLayout(main_layout)
     
    def load_cache(self):
        if not os.path.exists("folder_cache.json"):
            with open("folder_cache.json", "w") as f:
                json.dump({}, f)

        with open("folder_cache.json", "r") as f:
            self.folder_cache = json.load(f)
     
    def save_cache(self):
        with open("folder_cache.json", "w") as f:
            json.dump(self.folder_cache, f)
     
    def sort_by(self, column):
        items = [(item.text(column), item) for item in self.treeWidget.invisibleRootItem().takeChildren()]
        if column in [0, 3]:
            order = self.treeWidget.header().sortIndicatorOrder()
            self.treeWidget.sortItems(column, order)
        elif column == 1:
            items.sort(reverse=True, key=lambda x: float(x[0]) if x[0].lower() != "n/a" else -1)

            if self.treeWidget.header().sortIndicatorOrder() == Qt.AscendingOrder:
                items.reverse()

        else:
            items.sort(reverse=True, key=lambda x: datetime.datetime.strptime(x[0], "%Y-%m-%d %H:%M:%S") if x[0] != "N/A" else datetime.datetime.min)

            if self.treeWidget.header().sortIndicatorOrder() == Qt.AscendingOrder:
                items.reverse()

        self.treeWidget.clear()
        self.treeWidget.addTopLevelItems([item for _, item in items])

    def update_progress_bar(self, value):
        print(f"\rProgress: {value}%", end="", flush=True)

    def search_folders(self):
        keyword = self.searchLineEdit.text().lower().strip()
        if not keyword:
            self.restore_folder_list()
        else:
            self.treeWidget.clear()
            for folder_name in self.folder_names:
                if keyword in os.path.basename(folder_name).lower():
                    size_gb = self.get_folder_size_gb(folder_name)
                    date_modified = self.get_date_modified(folder_name)
                    item = QTreeWidgetItem([os.path.basename(folder_name), str(size_gb), date_modified, folder_name])
                    self.treeWidget.addTopLevelItem(item)

    def restore_folder_list(self):
        self.treeWidget.clear()
        for i, folder_name in enumerate(self.folder_names):
            size_gb = float(self.get_folder_size_gb(folder_name))
            date_modified = self.get_date_modified(folder_name)
            item = QTreeWidgetItem([os.path.basename(folder_name), f"{size_gb:.2f}", date_modified, folder_name])
            self.treeWidget.addTopLevelItem(item)
            self.update_progress_bar(int((i+1) / len(self.folder_names) * 100))

    def start(self):
        self.update_folder_names()
        self.save_cache()

    def add_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Directory")
        if folder_path:
            self.directoryListWidget.addItem(folder_path)

    def remove_folder(self):
        for item in self.directoryListWidget.selectedItems():
            self.directoryListWidget.takeItem(self.directoryListWidget.row(item))

        self.start()

    def folder_exists_and_unchanged(self, folder_path):
        if folder_path not in self.folder_cache:
            return False
        
        if not os.path.exists(folder_path):
            return False

        current_modification_time = os.path.getmtime(folder_path)
        cached_modification_time = self.folder_cache[folder_path]['modification_time']
        
        return current_modification_time == cached_modification_time

    def update_folder_names(self):
        self.folder_names = []
        total_directories = self.directoryListWidget.count()

        for i in range(total_directories):
            folder_path = self.directoryListWidget.item(i).text()
            if not self.folder_exists_and_unchanged(folder_path):
                with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
                    folders_list = pool.map(worker, [folder_path])
                folder_sizes = {folder: self.get_folder_size_gb(folder) for folders in folders_list for folder in folders if folder}
                self.folder_cache[folder_path] = {
                    'folders': list(folder_sizes.keys()),
                    'folder_sizes': folder_sizes,
                    'modification_time': os.path.getmtime(folder_path)
                }
            self.folder_names.extend(self.folder_cache[folder_path]['folders'])
            self.update_progress_bar(int((i + 1) / total_directories * 100))

        self.restore_folder_list()

    def get_folder_size_gb(self, folder_path):
        for cache in self.folder_cache.values():
            if folder_path in cache['folders']:
                return cache['folder_sizes'][folder_path]

        total_size_bytes = 0
        try:
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    total_size_bytes += os.path.getsize(file_path)
            size_gb = f"{round(total_size_bytes / 1024 / 1024 / 1024, 2)}"
        except FileNotFoundError:
            size_gb = "N/A"
        return size_gb

    def get_date_modified(self, folder_path):
        try:
            timestamp = os.path.getmtime(folder_path)
            date_modified = datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
        except FileNotFoundError:
            date_modified = "N/A"
        return date_modified

    def open_folder(self, item, column):
        folder_path = item.text(3)
        if sys.platform == "win32":
            os.startfile(folder_path)
        elif sys.platform == "darwin":
            os.system(f'open "{folder_path}"')
        else:
            os.system(f'xdg-open "{folder_path}"')

    def open_selected_folders(self):
        for item in self.treeWidget.selectedItems():
            folder_path = item.text(3)
            if sys.platform == "win32":
                os.startfile(folder_path)
            elif sys.platform == "darwin":
                os.system(f'open "{folder_path}"')
            else:
                os.system(f'xdg-open "{folder_path}"')

    def export_list(self):
        export_path, _ = QFileDialog.getSaveFileName(self, "Export List As", "", "Text files (*.txt);;HTML files (*.html)")
        if export_path:
            if export_path.endswith(".txt"):
                with open(export_path, "w") as f:
                    for i in range(self.treeWidget.topLevelItemCount()):
                        item = self.treeWidget.topLevelItem(i)
                        f.write(f"{item.text(0)}\t{item.text(1)}\t{item.text(2)}\t{item.text(3)}\n")
            elif export_path.endswith(".html"):
                with open(export_path, "w") as f:
                    f.write("<html>\n<body>\n<table>\n")
                    f.write("<tr><th>Folder Name</th><th>Size (GB)</th><th>Date Last Modified</th><th>Path</th></tr>\n")
                    for i in range(self.treeWidget.topLevelItemCount()):
                        item = self.treeWidget.topLevelItem(i)
                        f.write(f"<tr><td>{item.text(0)}</td><td>{item.text(1)}</td><td>{item.text(2)}</td><td>{item.text(3)}</td></tr>\n")
                    f.write("</table>\n</body>\n</html>\n")
            QMessageBox.information(self, "Export Successful", f"List exported to {export_path}")

    def load_directories(self):
        if not os.path.exists("FolderLister.txt"):
            with open("FolderLister.txt", "w"):
                pass

        with open("FolderLister.txt", "r") as f:
            for line in f:
                self.directoryListWidget.addItem(line.strip())

    def closeEvent(self, event):
        self.save_cache()
        with open("FolderLister.txt", "w") as f:
            for i in range(self.directoryListWidget.count()):
                f.write(self.directoryListWidget.item(i).text() + "\n")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FolderLister()
    window.show()
    sys.exit(app.exec_())
