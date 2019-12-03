import os, os.path
import cv2
import functools
from pathlib import Path
from multiprocessing import Process

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QMainWindow, QFileDialog, QWidget, QVBoxLayout, QGraphicsScene, QGraphicsView

from ui import Ui_MainWindow
import main as backend


def get_method(hwd):
    if hwd.process_hog_radioButton.isChecked():
        return 'hog'
    elif hwd.process_cnn_radioButton.isChecked():
        return 'cnn'
    else:
        raise NotImplementedError


def extract_select_input(hwd, path):
    # path is a typle of (filename, filter)
    if path[0]:
        hwd.extract_input_text.setText(path[0])

def extract_select_output(hwd, path):
    if path:
        hwd.extract_output_text.setText(path)
    process_select_input(hwd, path)

def process_select_input(hwd, path):
    if path:
        hwd.process_input_text.setText(path)

def count_dir_files(dir):
    return len([name for name in os.listdir(dir) if os.path.isfile(os.path.join(dir, name))])

def extract_update_progress_count(hwd, curr, total):
    txt = str(curr)+"/"+str(total)
    hwd.extract_progress_count.setText(txt)
    hwd.extract_progress_count.repaint()


def extract_update_process(hwd, output):
    hwd.current_frame = count_dir_files(output) - hwd.old_frames
    hwd.current_frame = hwd.current_frame if hwd.current_frame > 0 else 0
    extract_update_progress_count(hwd, hwd.current_frame, hwd.total_frames)

    print(hwd.current_frame, hwd.total_frames)
    if hwd.current_frame >= hwd.total_frames:
        for dir in hwd.fs_watcher.directories():
            hwd.fs_watcher.removePath(dir)
        print(hwd.fs_watcher.directories())
        hwd.statusbar.showMessage('Extraction done')

    hwd.extract_progressbar.setValue(hwd.current_frame)
    if hwd.current_frame > 0:
        preview(hwd, hwd.extract_output_text.text())



def preview(hwd, dir, order='latest'):
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
    QtCore.QTimer.singleShot(1000, lambda: set_image(hwd, image_path))
    #set_image(hwd, image_path)


def set_image(hwd, image_path):
    cvImg = backend.load_image(image_path)
    if cvImg is None:
        return

    label_Image = hwd.preview_placeholder
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


def extract_helper(hwd):
    input = hwd.extract_input_text.text()
    output = hwd.extract_output_text.text()

    p = Path(output)
    if not p.exists():
        os.makedirs(str(p), exist_ok=True)

    hwd.old_frames = count_dir_files(output)
    hwd.current_frame = 0
    hwd.total_frames = backend.get_frame_count(input)

    hwd.extract_progressbar.setMaximum(hwd.total_frames)
    extract_update_progress_count(hwd, hwd.current_frame, hwd.total_frames)

    hwd.fs_watcher = QtCore.QFileSystemWatcher([output], hwd.win)
    hwd.fs_watcher.directoryChanged.connect(lambda: extract_update_process(hwd, output))

    print(hwd.win)
    hwd.win.ffmpeg = Process(target=backend.extract_frames, args=(input, output, 'jpg'))
    hwd.win.ffmpeg.start()



def process_update_progress_count(hwd, curr, total):
    txt = str(curr)+"/"+str(total)
    hwd.process_progress_count.setText(txt)
    hwd.process_progress_count.repaint()


def process_update_process(hwd, output):
    hwd.current_frame = count_dir_files(output) - hwd.old_frames
    hwd.current_frame = hwd.current_frame if hwd.current_frame > 0 else 0
    process_update_progress_count(hwd, hwd.current_frame, hwd.total_frames)

    #print(hwd.current_frame, hwd.total_frames)
    if hwd.current_frame == hwd.total_frames:
        for dir in hwd.fs_watcher.directories():
            hwd.fs_watcher.removePath(dir)
        hwd.fs_watcher = None
        hwd.statusbar.showMessage('Processing done')


    hwd.process_progressbar.setValue(hwd.current_frame)
    if hwd.current_frame > 0:
        preview(hwd, output)


def process_helper(hwd):
    input = Path(hwd.process_input_text.text())
    output = Path(input) / 'output'

    if not output.exists():
        os.makedirs(str(output), exist_ok=True)

    hwd.statusbar.showMessage('Starting threads')

    hwd.old_frames = count_dir_files(output)
    hwd.current_frame = 0
    hwd.total_frames = count_dir_files(input) - 1 # one is our output folder

    hwd.process_progressbar.setMaximum(hwd.total_frames)
    process_update_progress_count(hwd, hwd.current_frame, hwd.total_frames)

    hwd.fs_watcher = QtCore.QFileSystemWatcher([str(output)], hwd.win)
    hwd.fs_watcher.directoryChanged.connect(lambda: process_update_process(hwd, output))

    #backend.pre_process_folder(input, output, 'cnn')
    import threading

    hwd.win.masker = Process(target=backend.pre_process_folder, args=(input,output, get_method(hwd)))
    #hwd.win.masker = threading.Thread(target=backend.pre_process_folder, args=(input,output, get_method(hwd)))
    hwd.win.masker.start()


def set_up_actions(hwd):
    #hwd.extract_input_text.setText('/Users/axcap/Downloads/input.mp4')
    #hwd.extract_output_text.setText('/Users/axcap/Downloads/output')
    #hwd.process_input_text.setText('/Users/axcap/Downloads/output')

    ########
    hwd.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "FaceMasker", None, -1))
    hwd.extract_button.setFocus()
    hwd.process_hog_radioButton.setChecked(True)
    hwd.extract_progressbar.setValue(0)
    hwd.process_progressbar.setValue(0)

    hwd.extract_input_select_button.clicked.connect(lambda: extract_select_input(
        hwd,
        QFileDialog.getOpenFileName(None, 'Open input video', '.', 'Videos (*.mp4 *.mkv)')))

    hwd.extract_output_select_button.clicked.connect(lambda: extract_select_output(
        hwd,
        QFileDialog.getExistingDirectory(None, 'Open Directory', '.')))

    hwd.process_input_select_button.clicked.connect(lambda: process_select_input(
        hwd,
        QFileDialog.getExistingDirectory(None, 'Open Directory', '.')))

    hwd.extract_button.clicked.connect(lambda: extract_helper(hwd))
    hwd.process_button.clicked.connect(lambda: process_helper(hwd))

    '''
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(30)
    sizePolicy.setHeightForWidth(hwd.preview_placeholder.sizePolicy().hasHeightForWidth())
    '''


class MyDialog(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyDialog, self).__init__()
        self.ffmpeg = None

    def closeEvent(self, evnt):
        super(MyDialog, self).closeEvent(evnt)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyDialog()
    MainWindow.hello = 'foo'
    MainWindow.setUnifiedTitleAndToolBarOnMac(True)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    ui.app = app
    ui.win = MainWindow
    set_up_actions(ui)

    MainWindow.show()
    sys.exit(app.exec_())
