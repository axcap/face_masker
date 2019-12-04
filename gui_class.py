import sys
import os, os.path
import cv2
import functools
from pathlib import Path
from multiprocessing import Process

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QMainWindow, QFileDialog, QWidget, QVBoxLayout, QGraphicsScene, QGraphicsView, QMessageBox

from ui import Ui_MainWindow
import main as backend


class MyDialog(QtWidgets.QMainWindow):
    def __init__(self, app):
        super(MyDialog, self).__init__()
        #MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.app = app
        self.tr = self.app.tr
        self.ui = Ui_MainWindow()

        self.translator = QtCore.QTranslator(app)
        self.app.installTranslator(self.translator)

        # set system locale
        self.ui.setupUi(self)
        self.set_up_ui_actions()

    def get_method(self):
        if self.ui.process_hog_radioButton.isChecked():
            return 'hog'
        elif self.ui.process_cnn_radioButton.isChecked():
            return 'cnn'
        else:
            raise NotImplementedError

    def extract_select_input(self, path):
        # path is a typle of (filename, filter)
        if path[0]:
            self.ui.extract_input_text.setText(path[0])

    def extract_select_output(self, path):
        if path:
            self.ui.extract_output_text.setText(path)
        process_select_input(self, path)

    def process_select_input(self, path):
        if path:
            self.ui.process_input_text.setText(path)

    def count_dir_files(self, dir):
        return len([name for name in os.listdir(dir) if os.path.isfile(os.path.join(dir, name))])

    def extract_update_progress_count(self, curr, total):
        txt = str(curr)+"/"+str(total)
        self.ui.extract_progress_count.setText(txt)
        self.ui.extract_progress_count.repaint()

    def extract_update_process(self, output):
        self.current_frame = count_dir_files(output) - self.old_frames
        self.current_frame = self.current_frame if self.current_frame > 0 else 0
        extract_update_progress_count(self.ui, self.current_frame, self.total_frames)
        print(self.current_frame, self.total_frames)
        if self.current_frame >= self.total_frames:
            for dir in self.ui.fs_watcher.directories():
                self.ui.fs_watcher.removePath(dir)
            print(self.ui.fs_watcher.directories())
            self.ui.statusbar.showMessage(self.t('Extraction done'))

        self.ui.extract_progressbar.setValue(self.current_frame)
        if self.current_frame > 0:
            preview(self.ui, self.ui.extract_output_text.text())

    def preview(self, dir, order='latest'):
        glob = Path(dir).glob('*.jpg')
        if order is 'latest':
            # find latest image in the folder
            image_path = next(iter(glob))
            for path in glob:
                if path.stat().st_mtime > image_path.stat().st_mtime:
                    image_path = path
        elif order is 'random':
            # choose random image
            p = list(glob)
            try:
                image_path = str(random.choice(p))
            except e:
                print(e)
                pass
        else:
            raise NotImplementedError

        # Delay preview, let image be fully writen to disk
        QtCore.QTimer.singleShot(1000, lambda: set_image(self.ui, image_path))
        #set_image(self.ui, image_path)

    def set_image(self, image_path):
        cvImg = backend.load_image(image_path)
        if cvImg is None:
            return
        label_Image = self.ui.preview_placeholder
        widget_h = label_Image.height()
        widget_w = label_Image.width()
        img_h, img_w, _ = cvImg.shape
        if img_h > widget_h or img_w > widget_w:
            ratio = widget_w / img_w
            new_w = int(img_w * ratio)
            new_h = int(img_h * ratio)
            cvImg = cv2.resize(cvImg, (new_w, new_h))

        height, width, channel = cvImg.shape
        bytesPerLine = 3 * width
        qImg = QtGui.QImage(cvImg, width, height,bytesPerLine,
                            QtGui.QImage.Format_RGB888).rgbSwapped()
        qImg = QtGui.QPixmap(qImg)
        label_Image.setPixmap(qImg)
        app.processEvents()

    def extract_helper(self):
        input = self.ui.extract_input_text.text()
        output = self.ui.extract_output_text.text()

        p = Path(output)
        if not p.exists():
            os.makedirs(str(p), exist_ok=True)
        self.old_frames = count_dir_files(output)
        self.current_frame = 0
        self.total_frames = backend.get_frame_count(input)

        self.ui.extract_progressbar.setMaximum(self.total_frames)
        extract_update_progress_count(self.ui, self.current_frame, self.total_frames)

        self.fs_watcher = QtCore.QFileSystemWatcher([output], self.ui.win)
        self.fs_watcher.directoryChanged.connect(lambda: extract_update_process(self.ui, output))

        print(self.ui.win)
        self.ffmpeg = Process(target=backend.extract_frames, args=(input, output, 'jpg'))
        self.ffmpeg.start()

    def process_update_progress_count(self, curr, total):
        txt = str(curr)+"/"+str(total)
        self.ui.process_progress_count.setText(txt)
        self.ui.process_progress_count.repaint()

    def process_update_process(self, output):
        self.current_frame = count_dir_files(output) - self.old_frames
        self.current_frame = self.current_frame if self.current_frame > 0 else 0
        process_update_progress_count(self.ui, self.current_frame, self.total_frames)

        #print(self.current_frame, self.total_frames)
        if self.current_frame == self.total_frames:
            for dir in self.fs_watcher.directories():
                self.fs_watcher.removePath(dir)
            self.fs_watcher = None
            self.statusbar.showMessage(self.t('Processing done'))

        self.ui.process_progressbar.setValue(self.current_frame)
        if self.current_frame > 0:
            preview(self.ui, output)

    def process_helper(self):
        input = Path(self.ui.process_input_text.text())
        output = Path(input) / 'output'
        if not output.exists():
            os.makedirs(str(output), exist_ok=True)
        self.ui.statusbar.showMessage(self.t('Starting threads'))

        self.old_frames = count_dir_files(output)
        self.current_frame = 0
        self.total_frames = count_dir_files(input) - 1 # one is our output folder

        self.ui.process_progressbar.setMaximum(self.total_frames)
        process_update_progress_count(self.ui, self.current_frame, self.total_frames)

        self.fs_watcher = QtCore.QFileSystemWatcher([str(output)], self.ui.win)
        self.fs_watcher.directoryChanged.connect(lambda: process_update_process(self.ui, output))

        #backend.pre_process_folder(input, output, 'cnn')
        import threading
        self.masker = Process(target=backend.pre_process_folder, args=(input,output, get_method(self.ui)))
        #self.ui.win.masker = threading.Thread(target=backend.pre_process_folder, args=(input,output, get_method(self.ui)))
        self.masker.start()

    def set_menu_langugage_english(self):
        print("Englando")
        self.translator.load('tr_en', os.path.dirname(__file__))
        self.ui.retranslateUi(self)
        self.ui.actionJapanese.setChecked(False)

    def set_menu_langugage_japanese(self):
        print("Moshi moshi")
        self.translator.load('tr_jp', os.path.dirname(__file__))
        self.ui.retranslateUi(self)
        self.ui.actionEnglish.setChecked(False)

    def t(self, string):
        return self.app.translate('app', string)

    def about(self):
        QMessageBox.about(self, self.t('About Face Masker'),
                          self.t("""This program will help you mask out faces in a video to make it anonymous for future use. This is done by extracting every frame from a video, finding faces in the current frame and mask them out using various methods like pixelating the area, filling it with random noise (recomended) or just simply painting a block box over the face.

You can also skip over step one of inputting a video, and provide alreadt extracted frames or independant images you want to mask faces on"""))

    def exit(self):
        sys.exit(self.app.exec_())

    def set_up_ui_actions(self):
        #self.ui.extract_input_text.setText('/Users/axcap/Downloads/input.mp4')
        #self.ui.extract_output_text.setText('/Users/axcap/Downloads/output')
        #self.ui.process_input_text.setText('/Users/axcap/Downloads/output')

        ########
        #self.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", self.t('FaceMasker'), None, -1))
        self.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", self.t('FaceMasker'), None, -1))
        self.ui.extract_button.setFocus()
        self.ui.process_hog_radioButton.setChecked(True)
        self.ui.extract_progressbar.setValue(0)
        self.ui.process_progressbar.setValue(0)

        self.ui.extract_input_select_button.clicked.connect(lambda: self.extract_select_input(
            QFileDialog.getOpenFileName(None, self.t('Open input video'), '.', self.t('Videos (*.mp4 *.mkv)'))))

        self.ui.extract_output_select_button.clicked.connect(lambda: self.extract_select_output(
            QFileDialog.getExistingDirectory(None, self.t('Open Directory'), '.')))

        self.ui.process_input_select_button.clicked.connect(lambda: self.process_select_input(
            QFileDialog.getExistingDirectory(None, self.t('Open Directory'), '.')))

        self.ui.extract_button.clicked.connect(self.extract_helper)
        self.ui.process_button.clicked.connect(self.process_helper)

        # Set menubar actions
        self.ui.menubar.setNativeMenuBar(False);
        self.ui.actionExit.triggered.connect(self.exit)
        self.ui.actionEnglish.triggered.connect(self.set_menu_langugage_english)
        self.ui.actionJapanese.triggered.connect(self.set_menu_langugage_japanese)
        self.ui.actionAbout.triggered.connect(self.about)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyDialog(app)
    MainWindow.show()

    sys.exit(app.exec_())
