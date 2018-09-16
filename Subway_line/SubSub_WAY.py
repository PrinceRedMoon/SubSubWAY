import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication , QMainWindow
import code.ui

def setup_hook():
    _excepthook = sys.excepthook

    def hook(exctype, value, traceback):
        print(exctype, value, traceback)
        _excepthook(exctype, value, traceback)
        sys.exit(1)

    sys.excepthook = hook


if __name__ == '__main__':
    setup_hook()

    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    #禁止最大化


    mainWindow.setWindowFlags(mainWindow.windowFlags()&~ Qt.WindowMaximizeButtonHint)
    ui = code.ui.Ui_SubSubWay()
    ui.setupUi(mainWindow)
    mainWindow.show()

    try:
        sys.exit(app.exec_())
    except:
        pass

