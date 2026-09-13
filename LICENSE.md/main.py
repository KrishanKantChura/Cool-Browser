import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QAction, QApplication, QLineEdit, QMainWindow, QToolBar
from PyQt5.QtWebEngineWidgets import QWebEngineView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)
        self.setWindowTitle('Cool Browser')
        self.showMaximized()

        navbar = QToolBar('Navigation')
        self.addToolBar(navbar)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

        self.navigate_home()

    def normalize_url(self, value):
        text = value.strip()
        if not text:
            return QUrl('https://www.google.com')

        if '://' not in text:
            text = 'https://' + text

        url = QUrl(text)
        if not url.isValid() or url.scheme() == '':
            return QUrl('https://www.google.com')
        return url

    def navigate_home(self):
        self.browser.setUrl(self.normalize_url('https://www.instagram.com/bytestherapy/'))

    def navigate_to_url(self):
        self.browser.setUrl(self.normalize_url(self.url_bar.text()))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setApplicationName('Cool Browser')
    window = MainWindow()
    sys.exit(app.exec_()) 
