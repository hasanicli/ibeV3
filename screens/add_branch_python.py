# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Erhan/Desktop/Koordinator/workplace_control/add_branch.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(435, 225)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        Form.setStyleSheet("/*\n"
" * The MIT License (MIT)\n"
" *\n"
" * Copyright (c) <2013-2014> <Colin Duquesnoy>\n"
" * Copyright (c) <2017> <Michell Stuttgart>\n"
" *\n"
" * Permission is hereby granted, free of charge, to any person obtaining a copy\n"
" * of this software and associated documentation files (the \"Software\"), to deal\n"
" * in the Software without restriction, including without limitation the rights\n"
" * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n"
" * copies of the Software, and to permit persons to whom the Software is\n"
" * furnished to do so, subject to the following conditions:\n"
"\n"
" * The above copyright notice and this permission notice shall be included in\n"
" * all copies or substantial portions of the Software.\n"
"\n"
" * THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n"
" * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n"
" * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n"
" * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n"
" * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n"
" * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN\n"
" * THE SOFTWARE.\n"
" */\n"
"QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #D1DBCB;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    selection-background-color:#323232;\n"
"    selection-color: black;\n"
"    background-clip: border;\n"
"    border-image: none;\n"
"    border: 0px transparent black;\n"
"    outline: 0;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: #D1DBCB;\n"
"    color: black;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: #D1DBCB;\n"
"    border: 0px\n"
"}\n"
"\n"
"QCheckBox\n"
"{\n"
"    spacing: 5px;\n"
"    outline: none;\n"
"    color: #eff0f1;\n"
"    margin-bottom: 2px;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"    color: #76797C;\n"
"}\n"
"\n"
"QCheckBox::indicator,QGroupBox::indicator\n"
"{\n"
"    width: 18px;\n"
"    height: 18px;\n"
"}\n"
"\n"
"QGroupBox::indicator\n"
"{\n"
"    margin-left: 2px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked\n"
"{\n"
"    image: url(:/qss_icons/rc/checkbox_unchecked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover,\n"
"QCheckBox::indicator:unchecked:focus,\n"
"QCheckBox::indicator:unchecked:pressed,\n"
"QGroupBox::indicator:unchecked:hover,\n"
"QGroupBox::indicator:unchecked:focus,\n"
"QGroupBox::indicator:unchecked:pressed\n"
"{\n"
"  border: none;\n"
"    image: url(:/qss_icons/rc/checkbox_unchecked_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image: url(:/qss_icons/rc/checkbox_checked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover,\n"
"QCheckBox::indicator:checked:focus,\n"
"QCheckBox::indicator:checked:pressed,\n"
"QGroupBox::indicator:checked:hover,\n"
"QGroupBox::indicator:checked:focus,\n"
"QGroupBox::indicator:checked:pressed\n"
"{\n"
"    border: none;\n"
"    image: url(:/qss_icons/rc/checkbox_checked_focus.png);\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:indeterminate\n"
"{\n"
"    image: url(:/qss_icons/rc/checkbox_indeterminate.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:focus,\n"
"QCheckBox::indicator:indeterminate:hover,\n"
"QCheckBox::indicator:indeterminate:pressed\n"
"{\n"
"    image: url(:/qss_icons/rc/checkbox_indeterminate_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled,\n"
"QGroupBox::indicator:checked:disabled\n"
"{\n"
"    image: url(:/qss_icons/rc/checkbox_checked_disabled.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:disabled,\n"
"QGroupBox::indicator:unchecked:disabled\n"
"{\n"
"    image: url(:/qss_icons/rc/checkbox_unchecked_disabled.png);\n"
"}\n"
"\n"
"QRadioButton\n"
"{\n"
"    spacing: 5px;\n"
"    outline: none;\n"
"    color: #eff0f1;\n"
"    margin-bottom: 2px;\n"
"}\n"
"\n"
"QRadioButton:disabled\n"
"{\n"
"    color: #76797C;\n"
"}\n"
"QRadioButton::indicator\n"
"{\n"
"    width: 21px;\n"
"    height: 21px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked\n"
"{\n"
"    image: url(:/qss_icons/rc/radio_unchecked.png);\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:unchecked:hover,\n"
"QRadioButton::indicator:unchecked:focus,\n"
"QRadioButton::indicator:unchecked:pressed\n"
"{\n"
"    border: none;\n"
"    outline: none;\n"
"    image: url(:/qss_icons/rc/radio_unchecked_focus.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    border: none;\n"
"    outline: none;\n"
"    image: url(:/qss_icons/rc/radio_checked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover,\n"
"QRadioButton::indicator:checked:focus,\n"
"QRadioButton::indicator:checked:pressed\n"
"{\n"
"    border: none;\n"
"    outline: none;\n"
"    image: url(:/qss_icons/rc/radio_checked_focus.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:disabled\n"
"{\n"
"    outline: none;\n"
"    image: url(:/qss_icons/rc/radio_checked_disabled.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:disabled\n"
"{\n"
"    image: url(:/qss_icons/rc/radio_unchecked_disabled.png);\n"
"}\n"
"\n"
"\n"
"QMenuBar\n"
"{\n"
"    background-color: #323232;\n"
"    color: #D1DBCB;\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background-color: #323232;\n"
"    background: transparent;\n"
"    /* padding: 2px 20px 2px 20px; */\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    /* border: 1px solid #76797C; */\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    border: 0px solid #76797C;\n"
"    background-color: #D1DBCB;\n"
"    color: #000;\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    background-color: #323232;\n"
"    /* border: 1px solid #76797C; */\n"
"    color: #eff0f1;\n"
"    /*margin: 2px; */\n"
"}\n"
"\n"
"QMenu::icon\n"
"{\n"
"    /*margin: 5px;*/\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 30px 2px 30px;\n"
"    /*margin-left: 5px;*/\n"
"    border: 1px solid transparent; /* reserve space for selection border */\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 2px;\n"
"    background: #D1DBCB;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QMenu::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"}\n"
"\n"
"/* non-exclusive indicator = check box style indicator\n"
"   (see QActionGroup::setExclusive) */\n"
"QMenu::indicator:non-exclusive:unchecked {\n"
"    image: url(:/qss_icons/rc/checkbox_unchecked.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:unchecked:selected {\n"
"    image: url(:/qss_icons/rc/checkbox_unchecked_disabled.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked {\n"
"    image: url(:/qss_icons/rc/checkbox_checked.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked:selected {\n"
"    image: url(:/qss_icons/rc/checkbox_checked_disabled.png);\n"
"}\n"
"\n"
"/* exclusive indicator = radio button style indicator (see QActionGroup::setExclusive) */\n"
"QMenu::indicator:exclusive:unchecked {\n"
"    image: url(:/qss_icons/rc/radio_unchecked.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:unchecked:selected {\n"
"    image: url(:/qss_icons/rc/radio_unchecked_disabled.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked {\n"
"    image: url(:/qss_icons/rc/radio_checked.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked:selected {\n"
"    image: url(:/qss_icons/rc/radio_checked_disabled.png);\n"
"}\n"
"\n"
"QMenu::right-arrow {\n"
"    margin: 5px;\n"
"    image: url(:/qss_icons/rc/right_arrow.png)\n"
"}\n"
"\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #454545;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    alternate-background-color: #323232;\n"
"    color: #eff0f1;\n"
"    border: 1px solid 3A3939;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QWidget:focus, QMenuBar:focus,QToolBar:focus,QScrollAreaViewer:focus\n"
"{\n"
"    /* border: 2px solid #D1DBCB; */\n"
"}\n"
"\n"
"QTabWidget:focus, QCheckBox:focus, QRadioButton:focus, QSlider:focus\n"
"{\n"
"    border: none;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: #1e1e1e;\n"
"    selection-background-color: #D1DBCB;\n"
"    selection-color: black;\n"
"    padding: 5px;\n"
"    border-style: solid;\n"
"    border: 1px solid #76797C;\n"
"    border-radius: 2px;\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    border:1px solid #76797C;\n"
"    border-radius: 2px;\n"
"    margin-top: 20px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 10px;\n"
"}\n"
"\n"
"QAbstractScrollArea\n"
"{\n"
"    border-radius: 0px;\n"
"    border: 0px solid #76797C;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar:horizontal\n"
"{\n"
"    height: 15px;\n"
"    margin: 3px 15px 3px 15px;\n"
"    border: 1px transparent #2A2929;\n"
"    border-radius: 4px;\n"
"    background-color: #2A2929;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-width: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
"{\n"
"    border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
"{\n"
"    border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #2A2929;\n"
"    width: 15px;\n"
"    margin: 15px 3px 15px 3px;\n"
"    border: 1px transparent #2A2929;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-height: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"{\n"
"\n"
"    border-image: url(:/qss_icons/rc/up_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"{\n"
"    border-image: url(:/qss_icons/rc/down_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #1e1e1e;\n"
"    color: #eff0f1;\n"
"    border: 1px solid #76797C;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #1e1e1e;;\n"
"    color: #eff0f1;\n"
"    border-radius: 2px;\n"
"    border: 1px solid #76797C;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: #76797C;\n"
"    color: #eff0f1;\n"
"    padding: 5px;\n"
"    border: 1px solid #76797C;\n"
"}\n"
"\n"
"QSizeGrip {\n"
"    image: url(:/qss_icons/rc/sizegrip.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: #323232;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    spacing: 2px;\n"
"    border: 1px dashed #76797C;\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: #787876;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #76797C;\n"
"    spacing: 2px;\n"
"}\n"
"\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 1px;\n"
"    background-color: #76797C;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QFrame\n"
"{\n"
"    border-radius: 0px;\n"
"    /*border: 1px solid #76797C;*/\n"
"}\n"
"\n"
"\n"
"QFrame[frameShape=\"0\"]\n"
"{\n"
"    border-radius: 0px;\n"
"    border: 0px transparent #76797C;\n"
"}\n"
"\n"
"QStackedWidget\n"
"{\n"
"    border: 1px transparent black;\n"
"}\n"
"\n"
"QToolBar {\n"
"    border: 0px transparent #393838;\n"
"    background: 0px solid #323232;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QToolBar::handle:horizontal {\n"
"    image: url(:/qss_icons/rc/Hmovetoolbar.png);\n"
"}\n"
"QToolBar::handle:vertical {\n"
"    image: url(:/qss_icons/rc/Vmovetoolbar.png);\n"
"}\n"
"QToolBar::separator:horizontal {\n"
"    image: url(:/qss_icons/rc/Hsepartoolbar.png);\n"
"}\n"
"QToolBar::separator:vertical {\n"
"    image: url(:/qss_icons/rc/Vsepartoolbar.png);\n"
"}\n"
"QToolButton#qt_toolbar_ext_button {\n"
"    background: #58595a\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: #323232;\n"
"    border-width: 1px;\n"
"    border-color: #76797C;\n"
"    border-style: solid;\n"
"    padding: 5px;\n"
"    border-radius: 0px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:disabled\n"
"{\n"
"    background-color: #323232;\n"
"    border-width: 1px;\n"
"    border-color: #454545;\n"
"    border-style: solid;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    border-radius: 2px;\n"
"    color: #454545;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    background-color: #D1DBCB;\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    color: black;\n"
"    background-color: #D1DBCB;\n"
"    padding-top: -15px;\n"
"    padding-bottom: -17px;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #D1DBCB;\n"
"    background-color: #31363B;\n"
"    border-style: solid;\n"
"    border: 1px solid #76797C;\n"
"    border-radius: 2px;\n"
"    padding: 5px;\n"
"    min-width: 75px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color: #76797C;\n"
"    border-color: #6A6969;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover,QAbstractSpinBox:hover,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QAbstractView:hover,QTreeView:hover\n"
"{\n"
"    border: 1px solid #D1DBCB;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 0px;\n"
"    padding-left: 4px;\n"
"    selection-background-color: #4a4a4a;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: #1e1e1e;\n"
"    border-radius: 2px;\n"
"    border: 1px solid #76797C;\n"
"    selection-background-color: #D1DBCB;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 0px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on, QComboBox::down-arrow:hover,\n"
"QComboBox::down-arrow:focus\n"
"{\n"
"    image: url(:/qss_icons/rc/down_arrow.png);\n"
"}\n"
"\n"
"QAbstractSpinBox {\n"
"    padding: 2px;\n"
"    margin: 2px;\n"
"    background-color: #1e1e1e;\n"
"    color: #eff0f1;\n"
"    border-radius: 0px;\n"
"    min-width: 75px;\n"
"    selection-background-color: #D1DBCB;\n"
"    selection-color: black;\n"
"}\n"
"\n"
"QAbstractSpinBox:up-button\n"
"{\n"
"    background-color: transparent;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: center right;\n"
"}\n"
"\n"
"QAbstractSpinBox:down-button\n"
"{\n"
"    background-color: transparent;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: center left;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow,QAbstractSpinBox::up-arrow:disabled,QAbstractSpinBox::up-arrow:off {\n"
"    image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"QAbstractSpinBox::up-arrow:hover\n"
"{\n"
"    image: url(:/qss_icons/rc/up_arrow.png);\n"
"}\n"
"\n"
"\n"
"QAbstractSpinBox::down-arrow,QAbstractSpinBox::down-arrow:disabled,QAbstractSpinBox::down-arrow:off\n"
"{\n"
"    image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"QAbstractSpinBox::down-arrow:hover\n"
"{\n"
"    image: url(:/qss_icons/rc/down_arrow.png);\n"
"}\n"
"\n"
"\n"
"QLabel\n"
"{\n"
"    border: 0px solid black;\n"
"    margin-left: 2px;\n"
"    margin-right: 2px;\n"
"    color: #D1DBCB;\n"
"}\n"
"\n"
"QTabWidget{\n"
"    border: 0px transparent black;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #76797C;\n"
"    padding: 5px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 5px; /* move to the right by 5px */\n"
"}\n"
"\n"
"QTabBar\n"
"{\n"
"    qproperty-drawBase: 0;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::focus\n"
"{\n"
"    border: 0px transparent black;\n"
"    color: black;\n"
"}\n"
"\n"
"QTabBar::hover\n"
"{\n"
"    border: 0px transparent black;\n"
"    color: black;\n"
"}\n"
"\n"
"QTabBar::close-button  {\n"
"    image: url(:/qss_icons/rc/close.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabBar::close-button:hover\n"
"{\n"
"    image: url(:/qss_icons/rc/close-hover.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabBar::close-button:pressed {\n"
"    image: url(:/qss_icons/rc/close-pressed.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* TOP TABS */\n"
"QTabBar::tab:top {\n"
"    color: #eff0f1;\n"
"    border: 1px solid #76797C;\n"
"    border-bottom: 1px transparent black;\n"
"    background-color: #323232;\n"
"    padding: 5px;\n"
"    min-width: 50px;\n"
"    border-top-left-radius: 2px;\n"
"    border-top-right-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: #54575B;\n"
"    border: 1px solid #76797C;\n"
"    border-bottom: 1px transparent black;\n"
"    border-top-left-radius: 2px;\n"
"    border-top-right-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:hover {\n"
"    background-color: #D1DBCB;\n"
"    color: black;\n"
"}\n"
"\n"
"/* BOTTOM TABS */\n"
"QTabBar::tab:bottom {\n"
"    color: #eff0f1;\n"
"    border: 1px solid #76797C;\n"
"    border-top: 1px transparent black;\n"
"    background-color: #323232;\n"
"    padding: 5px;\n"
"    border-bottom-left-radius: 2px;\n"
"    border-bottom-right-radius: 2px;\n"
"    min-width: 50px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: #54575B;\n"
"    border: 1px solid #76797C;\n"
"    border-top: 1px transparent black;\n"
"    border-bottom-left-radius: 2px;\n"
"    border-bottom-right-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected:hover {\n"
"    background-color: #D1DBCB;\n"
"    color: black;\n"
"}\n"
"\n"
"/* LEFT TABS */\n"
"QTabBar::tab:left {\n"
"    color: #eff0f1;\n"
"    border: 1px solid #76797C;\n"
"    border-left: 1px transparent black;\n"
"    background-color: #323232;\n"
"    padding: 5px;\n"
"    border-top-right-radius: 2px;\n"
"    border-bottom-right-radius: 2px;\n"
"    min-height: 50px;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: #54575B;\n"
"    border: 1px solid #76797C;\n"
"    border-left: 1px transparent black;\n"
"    border-top-right-radius: 2px;\n"
"    border-bottom-right-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:hover {\n"
"    background-color: #D1DBCB;\n"
"    color: black;\n"
"}\n"
"\n"
"\n"
"/* RIGHT TABS */\n"
"QTabBar::tab:right {\n"
"    color: #eff0f1;\n"
"    border: 1px solid #76797C;\n"
"    border-right: 1px transparent black;\n"
"    background-color: #323232;\n"
"    padding: 5px;\n"
"    border-top-left-radius: 2px;\n"
"    border-bottom-left-radius: 2px;\n"
"    min-height: 50px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: #54575B;\n"
"    border: 1px solid #76797C;\n"
"    border-right: 1px transparent black;\n"
"    border-top-left-radius: 2px;\n"
"    border-bottom-left-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected:hover {\n"
"    background-color: #D1DBCB;\n"
"    color: black;\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:enabled {\n"
"     image: url(:/qss_icons/rc/right_arrow.png);\n"
" }\n"
"\n"
" QTabBar QToolButton::left-arrow:enabled {\n"
"     image: url(:/qss_icons/rc/left_arrow.png);\n"
" }\n"
"\n"
"QTabBar QToolButton::right-arrow:disabled {\n"
"     image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
" }\n"
"\n"
" QTabBar QToolButton::left-arrow:disabled {\n"
"     image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
" }\n"
"\n"
"\n"
"QDockWidget {\n"
"    background: #323232;\n"
"    border: 1px solid #403F3F;\n"
"    titlebar-close-icon: url(:/qss_icons/rc/close.png);\n"
"    titlebar-normal-icon: url(:/qss_icons/rc/undock.png);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button {\n"
"    border: 1px solid transparent;\n"
"    border-radius: 2px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover {\n"
"    background: rgba(255, 255, 255, 10);\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed {\n"
"    padding: 1px -1px -1px 1px;\n"
"    background: rgba(255, 255, 255, 10);\n"
"}\n"
"\n"
"QTreeView, QListView\n"
"{\n"
"    border: 1px solid #76797C;\n"
"    background-color: #1e1e1e;\n"
"}\n"
"\n"
"QTreeView:branch:selected, QTreeView:branch:hover\n"
"{\n"
"    background: url(:/qss_icons/rc/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:!adjoins-item {\n"
"    border-image: url(:/qss_icons/rc/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:adjoins-item {\n"
"    border-image: url(:/qss_icons/rc/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:!has-children:!has-siblings:adjoins-item {\n"
"    border-image: url(:/qss_icons/rc/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings {\n"
"    image: url(:/qss_icons/rc/branch_closed.png);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  {\n"
"    image: url(:/qss_icons/rc/branch_open.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed:hover,\n"
"QTreeView::branch:closed:has-children:has-siblings:hover {\n"
"    image: url(:/qss_icons/rc/branch_closed-on.png);\n"
"    }\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings:hover,\n"
"QTreeView::branch:open:has-children:has-siblings:hover  {\n"
"    image: url(:/qss_icons/rc/branch_open-on.png);\n"
"    }\n"
"\n"
"QListView::item:!selected:hover, QTreeView::item:!selected:hover  {\n"
"    background: #848383;\n"
"    outline: 0;\n"
"    color: #eff0f1;\n"
"}\n"
"\n"
"QListView::item:selected:hover, QTreeView::item:selected:hover  {\n"
"    background: #D1DBCB;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #565a5e;\n"
"    height: 4px;\n"
"    background: #565a5e;\n"
"    margin: 0px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #D1DBCB;\n"
"    border: 1px solid #999999;\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    margin: -5px 0;\n"
"}\n"
"\n"
"QSlider::add-page:qlineargradient {\n"
"    background: #595858;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QSlider::sub-page::qlineargradient:horizontal {\n"
"    background:  #D1DBCB;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-top-left-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid #565a5e;\n"
"    width: 4px;\n"
"    background: #565a5e;\n"
"    margin: 0px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: #D1DBCB;\n"
"    border: 1px solid #999999;\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    margin: 0 -5px;\n"
"}\n"
"\n"
"QToolButton {\n"
"    color: #D1DBCB;\n"
"    background-color: transparent;\n"
"    border: 0px transparent #76797C;\n"
"    border-radius: 0px;\n"
"    padding: 1px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
" padding-right: 20px; /* make way for the popup button */\n"
" border: 1px #76797C;\n"
" border-radius: 0px;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"2\"] { /* only for InstantPopup */\n"
" padding-right: 10px; /* make way for the popup button */\n"
" border: 0px #76797C;\n"
"}\n"
"\n"
"\n"
"QToolButton:hover, QToolButton::menu-button:hover {\n"
"    background-color: transparent;\n"
"    border: 1px solid #D1DBCB;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QToolButton:checked, QToolButton:pressed,\n"
"        QToolButton::menu-button:pressed {\n"
"    color: black;\n"
"    background-color: #D1DBCB;\n"
"    border: 0px solid #D1DBCB;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"/* the subcontrol below is used only in the InstantPopup or DelayedPopup mode */\n"
"QToolButton::menu-indicator {\n"
"    image: url(:/qss_icons/rc/down_arrow.png);\n"
"    top: -7px; left: -2px; /* shift it a bit */\n"
"}\n"
"\n"
"/* the subcontrols below are used only in the MenuButtonPopup mode */\n"
"QToolButton::menu-button {\n"
"    border: 1px transparent #76797C;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    /* 16px width + 4px for border = 20px allocated above */\n"
"    width: 16px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QToolButton::menu-arrow {\n"
"    image: url(:/qss_icons/rc/down_arrow.png);\n"
"}\n"
"\n"
"QToolButton::menu-arrow:open {\n"
"    border: 1px solid #76797C;\n"
"}\n"
"\n"
"QPushButton::menu-indicator  {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: bottom right;\n"
"    left: 8px;\n"
"}\n"
"\n"
"QTableView\n"
"{\n"
"    border: 1px solid #76797C;\n"
"    gridline-color: #323232;\n"
"    background-color: #1e1e1e;\n"
"}\n"
"\n"
"\n"
"QTableView, QHeaderView\n"
"{\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QTableView::item:pressed, QListView::item:pressed, QTreeView::item:pressed  {\n"
"    background: #D1DBCB;\n"
"    color: black;\n"
"}\n"
"\n"
"QTableView::item:selected:active, QTreeView::item:selected:active, QListView::item:selected:active  {\n"
"    background: #D1DBCB;\n"
"    color: black;\n"
"}\n"
"\n"
"QHeaderView\n"
"{\n"
"    background-color: #323232;\n"
"    border: 1px transparent;\n"
"    border-radius: 0px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"\n"
"}\n"
"\n"
"QHeaderView::section  {\n"
"    background-color: #323232;\n"
"    color: #eff0f1;\n"
"    padding: 5px;\n"
"    border: 1px solid #76797C;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QHeaderView::section::vertical::first, QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 1px solid #76797C;\n"
"}\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: transparent;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal::first, QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 1px solid #76797C;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: transparent;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
" {\n"
"    color: white;\n"
"    background-color: #848383;\n"
" }\n"
"\n"
" /* style the sort indicator */\n"
"QHeaderView::down-arrow {\n"
"    image: url(:/qss_icons/rc/down_arrow.png);\n"
"}\n"
"\n"
"QHeaderView::up-arrow {\n"
"    image: url(:/qss_icons/rc/up_arrow.png);\n"
"}\n"
"\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #323232;\n"
"    border: 1px transparent #76797C;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QToolBox  {\n"
"    padding: 5px;\n"
"    border: 1px transparent black;\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"    color: #eff0f1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #76797C;\n"
"    border-bottom: 1px transparent #323232;\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"}\n"
"\n"
"QToolBox::tab:selected { /* italicize selected tabs */\n"
"    font: italic;\n"
"    background-color: #323232;\n"
"    border-color: #D1DBCB;\n"
" }\n"
"\n"
"QStatusBar::item {\n"
"    border: 0px transparent dark;\n"
"    margin: 0px;\n"
"    border: 0px;\n"
" }\n"
"\n"
"\n"
"QFrame[height=\"3\"], QFrame[width=\"3\"] {\n"
"    background-color: #76797C;\n"
"}\n"
"\n"
"\n"
"QSplitter::handle {\n"
"    border: 1px dashed #76797C;\n"
"}\n"
"\n"
"QSplitter::handle:hover {\n"
"    background-color: #787876;\n"
"    border: 1px solid #76797C;\n"
"}\n"
"\n"
"QSplitter::handle:horizontal {\n"
"    width: 1px;\n"
"}\n"
"\n"
"QSplitter::handle:vertical {\n"
"    height: 1px;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: 1px solid #76797C;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #D1DBCB;\n"
"}\n"
"\n"
"QDateEdit\n"
"{\n"
"    selection-background-color: #D1DBCB;\n"
"    border-style: solid;\n"
"    border: 1px solid #CEE343;\n"
"    border-radius: 2px;\n"
"    padding: 1px;\n"
"    min-width: 75px;\n"
"}\n"
"\n"
"QDateEdit:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    selection-background-color: #4a4a4a;\n"
"}\n"
"\n"
"QDateEdit QAbstractItemView\n"
"{\n"
"    background-color: #1e1e1e;\n"
"    border-radius: 2px;\n"
"    border: 1px solid #3375A3;\n"
"    selection-background-color: #D1DBCB;\n"
"}\n"
"\n"
"QDateEdit::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-left-width: 0px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow\n"
"{\n"
"    image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"}\n"
"\n"
"QDateEdit::down-arrow:on, QDateEdit::down-arrow:hover,\n"
"QDateEdit::down-arrow:focus\n"
"{\n"
"    image: url(:/qss_icons/rc/down_arrow.png);\n"
"}\n"
"\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.cmb_department = QtWidgets.QComboBox(Form)
        self.cmb_department.setObjectName("cmb_department")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cmb_department)
        self.le_branch = QtWidgets.QLineEdit(Form)
        self.le_branch.setObjectName("le_branch")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.le_branch)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_save = QtWidgets.QPushButton(Form)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout.addWidget(self.btn_save)
        self.btn_delete = QtWidgets.QPushButton(Form)
        self.btn_delete.setObjectName("btn_delete")
        self.horizontalLayout.addWidget(self.btn_delete)
        self.btn_edit = QtWidgets.QPushButton(Form)
        self.btn_edit.setObjectName("btn_edit")
        self.horizontalLayout.addWidget(self.btn_edit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_2.addWidget(self.line_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.lw_branch = QtWidgets.QListWidget(Form)
        self.lw_branch.setObjectName("lw_branch")
        self.verticalLayout_2.addWidget(self.lw_branch)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.setStretch(0, 55)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(4, 35)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Alan : "))
        self.label_4.setText(_translate("Form", "Dal : "))
        self.btn_save.setText(_translate("Form", "Kaydet"))
        self.btn_delete.setText(_translate("Form", "Sil"))
        self.btn_edit.setText(_translate("Form", "Düzenle"))
        self.label_5.setText(_translate("Form", "Oluşturulmuş Dallar"))

