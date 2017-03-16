import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebKit import *
from PyQt5.QtWebKitWidgets import QWebPage


class Render(QWebPage):
    def __init__(self, url):
        self.app = QGuiApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self._loadFinished)
        