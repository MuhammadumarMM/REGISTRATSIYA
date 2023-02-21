from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QCheckBox, QMessageBox, QApplication, QWidget
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import re, requests



class MainWindow(QMainWindow):
    def __init__(self, width=600, height=650, title="Ro'yhatdan o'tish") -> None:
        super().__init__()
        self.setupWindow()
        self.setGeometry(600, 250, width, height)
        self.setWindowTitle(title)
       

    def setupWindow(self):
        style_label = """
        font-size: 18px;
        font-weight: 800;
        """

        style_input = """
        QLineEdit{
            font-size: 20px;
            font-weight: 300;
            border-radius: 7px;
        }
        """

        style_button = """
        QPushButton{
            font-size: 20px;
            font-weight: 600;
            border-radius: 7px;
            background-color:  rgb(170, 170, 127);
            color: rgb(0, 0, 0);
        }

        QPushButton::hover{
        background-color: rgb(213, 255, 215);
        color:rgb(255, 58, 23);
        }

        """
        ab=QIcon('img/online-registration.png')
       
        self.setWindowIcon(ab)
        self.signup_label = QLabel('REGISTRATSIYA')
        self.signup_label.setObjectName("signup_label")
        self.signup_label.setStyleSheet("#signup_label{font-size: 30px; font-weight: 500; color: rgb(85, 0, 127);}")


        signup_layout = QHBoxLayout()
        signup_layout.addStretch()
        signup_layout.addWidget(self.signup_label)
        signup_layout.addStretch()


        self.name_label = QLabel("ISM :")
        self.name_label.setFixedWidth(140)
        self.name_label.setFixedHeight(60)
        self.name_label.setStyleSheet(style_label)

        self.name_input = QLineEdit()
        self.name_input.setFixedWidth(250)
        self.name_input.setFixedHeight(60)
        self.name_input.setPlaceholderText("Ismingizni kiriting:")
        self.name_input.setStyleSheet(style_input)

        name_layout = QHBoxLayout()
        name_layout.addStretch()
        name_layout.addWidget(self.name_label)
        name_layout.addWidget(self.name_input)
        name_layout.addStretch()


        self.email_label  =QLabel("G-MAIL:")
        self.email_label.setFixedWidth(140)        
        self.email_label.setFixedHeight(60)        
        self.email_label.setStyleSheet(style_label)

        self.email_input = QLineEdit()
        self.email_input.setFixedWidth(250)        
        self.email_input.setFixedHeight(60)        
        self.email_input.setPlaceholderText("Gmaillingizni kiriting:")
        self.email_input.setStyleSheet(style_input)

        email_layout = QHBoxLayout()     
        email_layout.addStretch()
        email_layout.addWidget(self.email_label)
        email_layout.addWidget(self.email_input)
        email_layout.addStretch()


        self.password_label  =QLabel("PAROL:")
        self.password_label.setFixedWidth(140)      
        self.password_label.setFixedHeight(60)      
        self.password_label.setStyleSheet(style_label)

        self.password_input = QLineEdit()
        self.password_input.setFixedWidth(250)      
        self.password_input.setFixedHeight(60)      
        self.password_input.setPlaceholderText("Parolingizni eslab qoling:")
        self.password_input.setStyleSheet(style_input)
        self.password_input.setEchoMode(QLineEdit().echoMode().Password)

        self.passwd_view = QPushButton(QIcon('./img/hide.png'), '')
        self.passwd_view.setFixedSize(25, 25)
        self.passwd_view.setObjectName("passwd_view_btn")
        self.passwd_view.setStyleSheet("#passwd_view_btn{background: transparent;}")
        self.passwd_view.clicked.connect(self.unhide_password)

        passwd_view_layout = QHBoxLayout()
        passwd_view_layout.addStretch()
        passwd_view_layout.addSpacing(400)
        passwd_view_layout.addWidget(self.passwd_view)
        passwd_view_layout.addStretch()

        passwd_layout = QHBoxLayout()     
        passwd_layout.addStretch()
        passwd_layout.addWidget(self.password_label)
        passwd_layout.addWidget(self.password_input)
        passwd_layout.addStretch()


        self.telegram_id_label  =QLabel("Telegram ID:")
        self.telegram_id_label.setFixedWidth(140)  
        self.telegram_id_label.setFixedHeight(60)  
        self.telegram_id_label.setStyleSheet(style_label)

        self.telegram_id_input = QLineEdit()
        self.telegram_id_input.setFixedWidth(250)  
        self.telegram_id_input.setFixedHeight(60)  
        self.telegram_id_input.setPlaceholderText("Telegram IDingizni kiriting:")
        self.telegram_id_input.setStyleSheet(style_input)

        telegram_id_layout = QHBoxLayout()     
        telegram_id_layout.addStretch()
        telegram_id_layout.addWidget(self.telegram_id_label)
        telegram_id_layout.addWidget(self.telegram_id_input)
        telegram_id_layout.addStretch()

        self.terms_conditions_check = QCheckBox("Roziligingizni bildiring!")
        self.terms_conditions_check.setStyleSheet("QCheckBox{font-size: 14px; font-weight: 800;}")

        terms_layout = QHBoxLayout()
        terms_layout.addStretch()
        terms_layout.addWidget(self.terms_conditions_check)
        terms_layout.addStretch()

        self.cancel_button = QPushButton("Chiqish")
        self.cancel_button.setFixedSize(200, 60)
        self.cancel_button.setStyleSheet(style_button)
        self.cancel_button.clicked.connect(self.exit)


        self.singup_button = QPushButton("Jo'natish")
        self.singup_button.setFixedSize(200, 60)
        self.singup_button.setStyleSheet(style_button)
        self.singup_button.clicked.connect(self.signup)

        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.cancel_button)
        button_layout.addSpacing(25)
        button_layout.addWidget(self.singup_button)
        button_layout.addStretch()


        vertical_layout = QVBoxLayout()
        vertical_layout.addStretch()
        vertical_layout.addLayout(signup_layout)
        vertical_layout.addSpacing(25)
        vertical_layout.addLayout(name_layout)
        vertical_layout.addSpacing(15)
        vertical_layout.addLayout(email_layout)
        vertical_layout.addSpacing(15)
        vertical_layout.addLayout(passwd_layout)
        vertical_layout.addLayout(passwd_view_layout)
        vertical_layout.addLayout(telegram_id_layout)
        vertical_layout.addSpacing(8)
        vertical_layout.addLayout(terms_layout)
        vertical_layout.addSpacing(8)
        vertical_layout.addLayout(button_layout)
        vertical_layout.addStretch()


        center = QWidget()
        center.setLayout(vertical_layout)
        self.setCentralWidget(center)

    def send_notification(self):
        chat_id = int(self.telegram_id_input.text())
        text = f"You are signed up on Our platform\nYour email: {self.email_input.text()}\nYour password: {self.password_input.text()}"
        url = f"https://api.telegram.org/bot5774374755:AAE-AmaHt7WAwnxHov2Zs3NsIGXU2L-RxQI/sendMessage?chat_id={chat_id}&text={text}"
        response = requests.post(url)
        print(response.json())
        if response.status_code == 200:
            return True
        return False

    def unhide_password(self):
        echo_mode = str(self.password_input.echoMode()).split('.')[-1]
        if echo_mode == 'Password':
            self.password_input.setEchoMode(QLineEdit().echoMode().Normal)
            self.passwd_view.setIcon(QIcon("./img/witness.png"))
        elif echo_mode == 'Normal':
            self.password_input.setEchoMode(QLineEdit().echoMode().Password)
            self.passwd_view.setIcon(QIcon("./img/hide.png"))


    def signup(self):
        if len(self.name_input.text()) < 1:
            self.name_input_error = QMessageBox.critical(self, 'Xatolik', 'Ism kiritmadingiz!')
        elif not re.match(r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+", self.email_input.text()):
            self.email_input_error = QMessageBox.critical(self, 'Xatolik', "G-mailni tog'ri kiriting!")
        elif len(self.password_input.text()) < 8:
            self.password_error = QMessageBox.critical(self, 'Xatolik', 'Parol kiriting!')
        elif not (7 < len(self.telegram_id_input.text()) < 11 and self.telegram_id_input.text().isdigit()):
            self.telegram_id_input_error = QMessageBox.critical(self, 'Xatolik', "O'zingizni Idingizni to'g'ri kiriting!")
        elif not self.terms_conditions_check.isChecked():
            self.check_error = QMessageBox.critical(self, 'Xatolik', "Rozilik bildiring, ya'ni tugmachani bosing!")
        else:
            if self.send_notification():
                self.name_input.clear()
                self.email_input.clear()
                self.password_input.clear()
                self.telegram_id_input.clear()
                self.terms_conditions_check.setChecked(False)
                self.signedup = QMessageBox.about(self, "Jo'natish", "Ajoyib!\nBiz sizning telegramizga habar yolladik!")
            else:
                self.check_error = QMessageBox.critical(self, 'Xatolik', "Telegram ID noto'g'ri!")


    def exit(self):
        QApplication.quit()
