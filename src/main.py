import sys
import qdarkstyle
import pymongo
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from PySide6.QtCore import QSettings
from main_ui import Ui_MainWindow as main_ui
from about_ui import Ui_Form as about_ui
from cryptography.fernet import Fernet


class MainWindow(QMainWindow, main_ui): # used to display the main user interface
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # loads main_ui
        self.settings_manager = SettingsManager(self)  # Initializes SettingsManager
        self.settings_manager.load_settings()  # Load settings when the app starts
        self.mongo_db = MongoDB()  # Initialize MongoDB instance
        self.label_connection.setText("Not Connected")

        # QPushButton
        self.button_db_connect.clicked.connect(self.connect_to_mongo)
        self.button_user_connect.clicked.connect(self.hello_world)
        self.button_add.clicked.connect(self.add_new_user)

        # QLineEdit
        # Connect to Database
        self.mongo_url = self.line_mongo_url   
        self.mongo_database = self.line_mongo_database
        self.mongo_collection = self.line_mongo_collection
        self.mongo_username = self.line_mongo_username
        self.mongo_password = self.line_mongo_password

        # User Login
        self.username = self.line_username
        self.password = self.line_password

        # Add User
        self.add_user = self.line_add_user
        self.add_password = self.line_add_password

        # menubar
        self.action_dark_mode.toggled.connect(self.dark_mode)
        self.action_about.triggered.connect(self.show_about)
        self.action_about_qt.triggered.connect(self.about_qt)

    def connect_to_mongo(self):
        mongo_url = self.mongo_url.text()
        mongo_database = self.mongo_database.text()
        mongo_username = self.mongo_username.text()
        mongo_password = self.mongo_password.text()
        
        if any(not field for field in [mongo_url, mongo_username, mongo_password, mongo_database]):
            QMessageBox.warning(self, "Input Error", "Please fill in all fields: Server URL, Username, Password, and Database.")
            return

        # Create MongoDB instance with provided details
        self.mongo_db = MongoDB(mongo_url=mongo_url, mongo_username=mongo_username, mongo_password=mongo_password, mongo_database=mongo_database)
        self.mongo_db.connect()  # Try to connect

        # Update the connection status label
        self.update_connection_status()  # Refresh the connection status

    def update_connection_status(self):
        if self.mongo_db.is_connected:
            self.label_connection.setText("Connected to MongoDB")
        else:
            self.label_connection.setText("Failed to connect to MongoDB")

    def hello_world(self):
        input_username = self.username.text()
        input_password = self.password.text()
        mongo_collection = self.mongo_collection.text()
        
        # Check if MongoDB is connected
        if not self.mongo_db.is_connected:
            QMessageBox.critical(self, "Connection Error", "Not connected to MongoDB")
            return
        
        try:
            # Query the collection for matching username and password
            collection = self.mongo_db.db[mongo_collection]
            user = collection.find_one({
                "username": input_username,
                "password": input_password
            })
            
            # Check if a matching user was found
            if user:
                print("Hello World")
                QMessageBox.information(self, "Success", "Hello World - Login Successful!")
            else:
                QMessageBox.warning(self, "Login Failed", "Invalid username or password")
                
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

    def add_new_user(self):
        new_user = self.add_user.text()
        new_password = self.add_password.text()
        mongo_collection = self.mongo_collection.text()

        if any(not field for field in [new_user, new_password]):
            QMessageBox.warning(self, "Input Error", "New user and new password cannot be blank")
            return

        data = {"username":new_user,
                "password":new_password}
        
        if self.mongo_db.is_connected:
            collection = self.mongo_db.db[mongo_collection]
            collection.insert_one(data)
            QMessageBox.information(self, "Success", f"{new_user} added to the database")

        self.clear_fields()

    def clear_fields(self):
        self.add_user.clear()
        self.add_password.clear()

    def dark_mode(self, checked):
        if checked:
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
        else:
            self.setStyleSheet('')

    def show_about(self):  # loads the About window
        self.about_window = AboutWindow(dark_mode=self.action_dark_mode.isChecked())
        self.about_window.show()

    def about_qt(self):  # loads the About Qt window
        QApplication.aboutQt()

    def closeEvent(self, event):  # Save settings when closing the app
        self.settings_manager.save_settings()  # Save settings using the manager
        event.accept()

class MongoDB:
    def __init__(self, mongo_url=None, port=27017, mongo_username=None, mongo_password=None, mongo_database=None):
        self.mongo_url = mongo_url
        self.port = port
        self.mongo_username = mongo_username
        self.mongo_password = mongo_password
        self.mongo_database = mongo_database
        self.client = None
        self.db = None
        self.is_connected = False  # Initialize here

    def connect(self):
        try:
            uri = f"mongodb+srv://{self.mongo_username}:{self.mongo_password}@{self.mongo_url}/?retryWrites=true&w=majority&appName={self.mongo_username}"
            self.client = MongoClient(uri, server_api=ServerApi('1'))
            self.db = self.client[self.mongo_database]
            self.client.admin.command('ping')  # Test connection
            self.is_connected = True  # Set on successful connection
            print("Ping to MongoDB server successful")

        except pymongo.errors.OperationFailure as e:
            self.is_connected = False
            QMessageBox.critical(None, "FAILED TO CONNECT", "Please check your credentials\nIf your credentials are fine then check the database and collections and try again.")
        except Exception as e:
            self.is_connected = False
            QMessageBox.critical(None, "Connection Error", f"Error connecting to MongoDB: {e}")

class SettingsManager: # used to load and save settings when opening and closing the app
    def __init__(self, main_window):
        self.main_window = main_window
        self.settings = QSettings('settings.ini', QSettings.IniFormat)
        self.key = self.settings.value('encryption_key', None)
        if self.key is None:
            self.key = Fernet.generate_key()
            self.settings.setValue('encryption_key', self.key.decode())
        self.cipher = Fernet(self.key)

    def encrypt_text(self, text):
        if not text:
            return None
        return self.cipher.encrypt(text.encode()).decode()
    
    def decrypt_text(self, encrypted_text):
        if not encrypted_text:
            return None
        try:
            return self.cipher.decrypt(encrypted_text.encode()).decode()
        except Exception as e:
            print(f"Decryption error: {e}")
            return None

    def load_settings(self):
        size = self.settings.value('window_size', None)
        pos = self.settings.value('window_pos', None)
        dark = self.settings.value('dark_mode')

        mongo_url = self.settings.value('mongo_url')
        mongo_database = self.settings.value('mongo_database')
        mongo_collection = self.settings.value('mongo_collection')
        mongo_username = self.settings.value('mongo_username')
        encrypted_mongo_password = self.settings.value('mongo_password')
        
        if size is not None:
            self.main_window.resize(size)
        if pos is not None:
            self.main_window.move(pos)
        if dark == 'true':
            self.main_window.action_dark_mode.setChecked(True)
            self.main_window.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
        if mongo_url is not None:
            self.main_window.line_mongo_url.setText(mongo_url)
        if mongo_database is not None:
            self.main_window.line_mongo_database.setText(mongo_database)
        if mongo_collection is not None:
            self.main_window.line_mongo_collection.setText(mongo_collection)
        if mongo_username is not None:
            self.main_window.line_mongo_username.setText(mongo_username)
        
        if encrypted_mongo_password is not None:
            mongo_password = self.decrypt_text(encrypted_mongo_password)
            if mongo_password:
                self.main_window.line_mongo_password.setText(mongo_password)
            else:
                self.main_window.line_mongo_password.setText("")

    def save_settings(self):
        self.settings.setValue('window_size', self.main_window.size())
        self.settings.setValue('window_pos', self.main_window.pos())
        self.settings.setValue('dark_mode', self.main_window.action_dark_mode.isChecked())
        self.settings.setValue('mongo_url', self.main_window.line_mongo_url.text())
        self.settings.setValue('mongo_database', self.main_window.line_mongo_database.text())
        self.settings.setValue('mongo_collection', self.main_window.line_mongo_collection.text())
        self.settings.setValue('mongo_username', self.main_window.line_mongo_username.text())
        mongo_password = self.main_window.line_mongo_password.text()
        self.settings.setValue('mongo_password', self.encrypt_text(mongo_password))

class AboutWindow(QWidget, about_ui): # Configures the About window
    def __init__(self, dark_mode=False):
        super().__init__()
        self.setupUi(self)

        if dark_mode:
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())

if __name__ == "__main__":
    app = QApplication(sys.argv)  # needs to run first
    main_window = MainWindow()  # Instance of MainWindow
    main_window.show()
    sys.exit(app.exec())