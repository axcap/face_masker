# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'v3.ui',
# licensing of 'v3.ui' applies.
#
# Created: Sat Nov 16 10:50:07 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(758, 477)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_Extract = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_Extract.sizePolicy().hasHeightForWidth())
        self.groupBox_Extract.setSizePolicy(sizePolicy)
        self.groupBox_Extract.setMinimumSize(QtCore.QSize(400, 200))
        self.groupBox_Extract.setObjectName("groupBox_Extract")
        self.layoutWidget_5 = QtWidgets.QWidget(self.groupBox_Extract)
        self.layoutWidget_5.setGeometry(QtCore.QRect(0, 20, 401, 166))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.layoutWidget_5)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.extract_progressbar = QtWidgets.QProgressBar(self.layoutWidget_5)
        self.extract_progressbar.setProperty("value", 0)
        self.extract_progressbar.setObjectName("extract_progressbar")
        self.gridLayout_10.addWidget(self.extract_progressbar, 3, 1, 1, 1)
        self.extract_input_text = QtWidgets.QLineEdit(self.layoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.extract_input_text.sizePolicy().hasHeightForWidth())
        self.extract_input_text.setSizePolicy(sizePolicy)
        self.extract_input_text.setText("")
        self.extract_input_text.setObjectName("extract_input_text")
        self.gridLayout_10.addWidget(self.extract_input_text, 0, 1, 1, 1)
        self.extract_output_select_button = QtWidgets.QPushButton(self.layoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.extract_output_select_button.sizePolicy().hasHeightForWidth())
        self.extract_output_select_button.setSizePolicy(sizePolicy)
        self.extract_output_select_button.setObjectName("extract_output_select_button")
        self.gridLayout_10.addWidget(self.extract_output_select_button, 1, 2, 1, 1)
        self.extract_input_label = QtWidgets.QLabel(self.layoutWidget_5)
        self.extract_input_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.extract_input_label.setObjectName("extract_input_label")
        self.gridLayout_10.addWidget(self.extract_input_label, 0, 0, 1, 1)
        self.extract_input_select_button = QtWidgets.QPushButton(self.layoutWidget_5)
        self.extract_input_select_button.setObjectName("extract_input_select_button")
        self.gridLayout_10.addWidget(self.extract_input_select_button, 0, 2, 1, 1)
        self.extract_output_label = QtWidgets.QLabel(self.layoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.extract_output_label.sizePolicy().hasHeightForWidth())
        self.extract_output_label.setSizePolicy(sizePolicy)
        self.extract_output_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.extract_output_label.setObjectName("extract_output_label")
        self.gridLayout_10.addWidget(self.extract_output_label, 1, 0, 1, 1)
        self.extract_output_text = QtWidgets.QLineEdit(self.layoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.extract_output_text.sizePolicy().hasHeightForWidth())
        self.extract_output_text.setSizePolicy(sizePolicy)
        self.extract_output_text.setMinimumSize(QtCore.QSize(250, 0))
        self.extract_output_text.setText("")
        self.extract_output_text.setObjectName("extract_output_text")
        self.gridLayout_10.addWidget(self.extract_output_text, 1, 1, 1, 1)
        self.extract_button = QtWidgets.QPushButton(self.layoutWidget_5)
        self.extract_button.setObjectName("extract_button")
        self.gridLayout_10.addWidget(self.extract_button, 4, 1, 1, 1)
        self.extract_progress_count = QtWidgets.QLabel(self.layoutWidget_5)
        self.extract_progress_count.setAlignment(QtCore.Qt.AlignCenter)
        self.extract_progress_count.setObjectName("extract_progress_count")
        self.gridLayout_10.addWidget(self.extract_progress_count, 2, 1, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_10, 1, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox_Extract)
        self.groupBox_Process = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_Process.sizePolicy().hasHeightForWidth())
        self.groupBox_Process.setSizePolicy(sizePolicy)
        self.groupBox_Process.setMinimumSize(QtCore.QSize(400, 200))
        self.groupBox_Process.setObjectName("groupBox_Process")
        self.layoutWidget_6 = QtWidgets.QWidget(self.groupBox_Process)
        self.layoutWidget_6.setGeometry(QtCore.QRect(0, 20, 401, 161))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.layoutWidget_6)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.process_button = QtWidgets.QPushButton(self.layoutWidget_6)
        self.process_button.setEnabled(True)
        self.process_button.setDefault(False)
        self.process_button.setObjectName("process_button")
        self.gridLayout_12.addWidget(self.process_button, 4, 1, 1, 3)
        self.process_input_select_button = QtWidgets.QPushButton(self.layoutWidget_6)
        self.process_input_select_button.setObjectName("process_input_select_button")
        self.gridLayout_12.addWidget(self.process_input_select_button, 0, 4, 1, 1)
        self.process_input_label = QtWidgets.QLabel(self.layoutWidget_6)
        self.process_input_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.process_input_label.setObjectName("process_input_label")
        self.gridLayout_12.addWidget(self.process_input_label, 0, 0, 1, 1)
        self.process_input_text = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.process_input_text.setText("")
        self.process_input_text.setObjectName("process_input_text")
        self.gridLayout_12.addWidget(self.process_input_text, 0, 1, 1, 3)
        self.process_cnn_radioButton = QtWidgets.QRadioButton(self.layoutWidget_6)
        self.process_cnn_radioButton.setObjectName("process_cnn_radioButton")
        self.gridLayout_12.addWidget(self.process_cnn_radioButton, 1, 2, 1, 2)
        self.process_method_label = QtWidgets.QLabel(self.layoutWidget_6)
        self.process_method_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.process_method_label.setObjectName("process_method_label")
        self.gridLayout_12.addWidget(self.process_method_label, 1, 0, 1, 1)
        self.process_hog_radioButton = QtWidgets.QRadioButton(self.layoutWidget_6)
        self.process_hog_radioButton.setObjectName("process_hog_radioButton")
        self.gridLayout_12.addWidget(self.process_hog_radioButton, 1, 1, 1, 1)
        self.process_progress_count = QtWidgets.QLabel(self.layoutWidget_6)
        self.process_progress_count.setAlignment(QtCore.Qt.AlignCenter)
        self.process_progress_count.setObjectName("process_progress_count")
        self.gridLayout_12.addWidget(self.process_progress_count, 2, 1, 1, 3)
        self.process_progressbar = QtWidgets.QProgressBar(self.layoutWidget_6)
        self.process_progressbar.setProperty("value", 0)
        self.process_progressbar.setObjectName("process_progressbar")
        self.gridLayout_12.addWidget(self.process_progressbar, 3, 1, 1, 3)
        self.gridLayout_11.addLayout(self.gridLayout_12, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_11.addItem(spacerItem1, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox_Process)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.groupBox_Preview = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_Preview.sizePolicy().hasHeightForWidth())
        self.groupBox_Preview.setSizePolicy(sizePolicy)
        self.groupBox_Preview.setMinimumSize(QtCore.QSize(320, 240))
        self.groupBox_Preview.setObjectName("groupBox_Preview")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_Preview)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.preview_placeholder = QtWidgets.QLabel(self.groupBox_Preview)
        self.preview_placeholder.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.preview_placeholder.sizePolicy().hasHeightForWidth())
        self.preview_placeholder.setSizePolicy(sizePolicy)
        self.preview_placeholder.setMaximumSize(QtCore.QSize(16777, 16777))
        self.preview_placeholder.setText("")
        self.preview_placeholder.setAlignment(QtCore.Qt.AlignCenter)
        self.preview_placeholder.setObjectName("preview_placeholder")
        self.horizontalLayout_2.addWidget(self.preview_placeholder)
        self.horizontalLayout.addWidget(self.groupBox_Preview)
        self.gridLayout_13.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 758, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuLanguage = QtWidgets.QMenu(self.menuOptions)
        self.menuLanguage.setObjectName("menuLanguage")
        self.menuHekp = QtWidgets.QMenu(self.menubar)
        self.menuHekp.setObjectName("menuHekp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionEnglish = QtWidgets.QAction(MainWindow)
        self.actionEnglish.setObjectName("actionEnglish")
        self.actionJapanese = QtWidgets.QAction(MainWindow)
        self.actionJapanese.setObjectName("actionJapanese")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionExit)
        self.menuLanguage.addAction(self.actionEnglish)
        self.menuLanguage.addAction(self.actionJapanese)
        self.menuOptions.addAction(self.menuLanguage.menuAction())
        self.menuHekp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHekp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.groupBox_Extract.setTitle(QtWidgets.QApplication.translate("MainWindow", "Extract", None, -1))
        self.extract_output_select_button.setText(QtWidgets.QApplication.translate("MainWindow", "Select", None, -1))
        self.extract_input_label.setText(QtWidgets.QApplication.translate("MainWindow", "Input", None, -1))
        self.extract_input_select_button.setText(QtWidgets.QApplication.translate("MainWindow", "Select", None, -1))
        self.extract_output_label.setText(QtWidgets.QApplication.translate("MainWindow", "Output", None, -1))
        self.extract_button.setText(QtWidgets.QApplication.translate("MainWindow", "Extract", None, -1))
        self.extract_progress_count.setText(QtWidgets.QApplication.translate("MainWindow", "0/0", None, -1))
        self.groupBox_Process.setTitle(QtWidgets.QApplication.translate("MainWindow", "Process", None, -1))
        self.process_button.setText(QtWidgets.QApplication.translate("MainWindow", "Process", None, -1))
        self.process_input_select_button.setText(QtWidgets.QApplication.translate("MainWindow", "Select", None, -1))
        self.process_input_label.setText(QtWidgets.QApplication.translate("MainWindow", "Input", None, -1))
        self.process_cnn_radioButton.setText(QtWidgets.QApplication.translate("MainWindow", "CNN", None, -1))
        self.process_method_label.setText(QtWidgets.QApplication.translate("MainWindow", "Method", None, -1))
        self.process_hog_radioButton.setText(QtWidgets.QApplication.translate("MainWindow", "HOG", None, -1))
        self.process_progress_count.setText(QtWidgets.QApplication.translate("MainWindow", "0/0", None, -1))
        self.groupBox_Preview.setTitle(QtWidgets.QApplication.translate("MainWindow", "Preview", None, -1))
        self.menuFile.setTitle(QtWidgets.QApplication.translate("MainWindow", "File", None, -1))
        self.menuOptions.setTitle(QtWidgets.QApplication.translate("MainWindow", "Options", None, -1))
        self.menuLanguage.setTitle(QtWidgets.QApplication.translate("MainWindow", "Language", None, -1))
        self.menuHekp.setTitle(QtWidgets.QApplication.translate("MainWindow", "Help", None, -1))
        self.actionExit.setText(QtWidgets.QApplication.translate("MainWindow", "Exit", None, -1))
        self.actionEnglish.setText(QtWidgets.QApplication.translate("MainWindow", "English", None, -1))
        self.actionJapanese.setText(QtWidgets.QApplication.translate("MainWindow", "Japanese", None, -1))
        self.actionAbout.setText(QtWidgets.QApplication.translate("MainWindow", "About", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
