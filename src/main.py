import sys
import qdarkstyle
import pymongo
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QTableWidget, QTableWidgetItem
from PySide6.QtCore import QSettings
from main_ui import Ui_MainWindow as main_ui
from about_ui import Ui_Dialog as about_ui
from cryptography.fernet import Fernet
import bcrypt

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
        self.button_add.clicked.connect(self.register_new_user)
        self.button_search.clicked.connect(self.search_for_user)
        self.button_delete.clicked.connect(self.delete_user)

        # Radio Buttons
        self.radio_on_mongo_cloud.toggled.connect(self.toggle_mongo_cluster)

        # menubar
        self.action_dark_mode.toggled.connect(self.dark_mode)
        self.action_about.triggered.connect(lambda: AboutWindow(dark_mode=self.action_dark_mode.isChecked()).exec())
        self.action_about_qt.triggered.connect(lambda: QApplication.aboutQt())

    def toggle_mongo_cluster(self,checked):
        self.line_mongo_cluster.setEnabled(checked)

    def connect_to_mongo(self):
        mongo_url = self.line_mongo_url.text().strip()
        mongo_database = self.line_mongo_database.text().strip()
        mongo_collection = self.line_mongo_collection.text().strip()
        mongo_username = self.line_mongo_username.text().strip()
        mongo_password = self.line_mongo_password.text().strip()
        cluster = self.line_mongo_cluster.text().strip()
        
        if any(not field for field in [mongo_url, mongo_username, mongo_password, mongo_database]):
            QMessageBox.warning(self, "Input Error", "Please fill in all fields: Server URL, Username, Password, and Database.")
            return

        self.mongo_db = MongoDB(
            mongo_url=mongo_url, 
            mongo_username=mongo_username, 
            mongo_password=mongo_password, 
            mongo_database=mongo_database, 
            mongo_collection=mongo_collection,
            cluster=cluster,
            parent=self)
        self.mongo_db.connect()

        self.mongo_query()

    def hello_world(self):
        username = self.line_username.text().strip()
        password = self.line_password.text().strip()
        mongo_collection = self.line_mongo_collection.text().strip()

        # Check if MongoDB is connected
        if not self.mongo_db.is_connected:
            QMessageBox.critical(self, "Connection Error", "Not connected to MongoDB")
            return
        
        # Query the collection for matching username and password
        try:
            collection = self.mongo_db.db[mongo_collection]
            user = collection.find_one({"username": username})
            
            if user and bcrypt.checkpw(password.encode('utf-8'), user["password"].encode('utf-8')):
                QMessageBox.information(self, "Success", f"Hello {username} - Login Successful!")
            else:
                QMessageBox.warning(self, "Login Failed", "Invalid username or password")
                
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

    def register_new_user(self): # Add new user to the database
        new_user = self.line_new_user.text().strip()
        new_password = self.line_new_password.text().strip()
        mongo_collection = self.line_mongo_collection.text().strip()

        if any(not field for field in [new_user, new_password]):
            QMessageBox.warning(self, "Input Error", "New user and new password cannot be blank")
            return
        
        # Check if new_user contains '@' symbol
        if '@' not in new_user:
            QMessageBox.warning(self, "Input Error", "Username must contain a valid email")
            return
        
        # Check if user already exists in database
        if self.mongo_db.is_connected:
            collection = self.mongo_db.db[mongo_collection]
            existing_user = collection.find_one({"username": new_user})
            if existing_user:
                QMessageBox.warning(self, "User Error", f"User '{new_user}' already exists in the database")
                return
        else:
            QMessageBox.critical(self, "Connection Error", "Not connected to MongoDB")
            return
        
        # Hash the password with bcrypt
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), salt).decode('utf-8')

        data = {"username": new_user,
                "password": hashed_password}
        
        if self.mongo_db.is_connected:
            collection = self.mongo_db.db[mongo_collection]
            collection.insert_one(data)
            QMessageBox.information(self, "Success", f"{new_user} added to the database")

        self.clear_fields()
        self.mongo_query()

    def search_for_user(self): # Search the database for user
        mongo_collection = self.line_mongo_collection.text().strip()
        username_search = self.line_user_search.text().strip()
        query = {}
        if username_search:
            query["username"] = username_search

        self.initialize_table()

        if self.mongo_db.is_connected:
            collection = self.mongo_db.db[mongo_collection]

            documents = collection.find(query)

            for doc in documents:
                row = self.table.rowCount()  # Get the next empty row index
                self.table.insertRow(row)  # Add a new row

                # Insert data into respective columns
                self.table.setItem(row, 0, QTableWidgetItem(doc.get('username', '')))

            self.table.resizeColumnsToContents()
            self.table.resizeRowsToContents()
        else:
            print("MongoDB is not connected. Cannot query data.")

    def delete_user(self):
        mongo_collection = self.line_mongo_collection.text().strip()

        # Get the selected rows from the table
        selected_rows = self.table.selectedIndexes()

        # Check if any rows are selected
        if not selected_rows:
            return  # Early return if no rows are selected

        # Collect IDs from the selected rows
        users_to_delete = {self.table.item(index.row(), 0).text() for index in selected_rows}

        # Confirm deletion with the user (optional)
        confirmation = QMessageBox.question(self, "Confirm Deletion",
                                            f"Are you sure you want to delete the selected {len(users_to_delete)} records?",
                                            QMessageBox.Yes | QMessageBox.No)

        # Proceed only if the user confirms
        if confirmation != QMessageBox.Yes:
            return  # Early return if deletion is cancelled

        # Check MongoDB connection
        if not self.mongo_db.is_connected:
            return  # Early return if not connected to MongoDB

        # Perform the deletion
        collection = self.mongo_db.db[mongo_collection]
        result = collection.delete_many({"username": {"$in": list(users_to_delete)}})

        # Handle the result of the deletion
        if result.deleted_count > 0:
            # Remove the rows from the table UI
            for row in sorted([index.row() for index in selected_rows], reverse=True):
                self.table.removeRow(row)
        else:
            print("No documents found to delete in MongoDB")

    def clear_fields(self):
        self.line_new_user.clear()
        self.line_new_password.clear()

    def mongo_query(self):
        mongo_collection = self.line_mongo_collection.text().strip()
        self.initialize_table()

        if self.mongo_db.is_connected:
            collection = self.mongo_db.db[mongo_collection]

            # Query to get all documents from the collection
            documents = collection.find()

            self.table.setRowCount(0)

            # Populate the table with data from MongoDB
            for doc in documents:
                row = self.table.rowCount()  # Get the next empty row index
                self.table.insertRow(row)
                # Insert data into respective columns
                self.table.setItem(row, 0, QTableWidgetItem(doc.get('username', '')))

            self.table.resizeColumnsToContents()
            self.table.resizeRowsToContents()

        else:
            print("MongoDB is not connected. Cannot query data.")

    def initialize_table(self):
        self.table.setRowCount(0) # clears the table
        self.table.setColumnCount(1)
        self.table.setHorizontalHeaderLabels(['User'])
        self.table.setSelectionMode(QTableWidget.MultiSelection)

    def populate_table(self, row, username):
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(username))
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

    def dark_mode(self, checked):
        if checked:
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
        else:
            self.setStyleSheet('')

    def closeEvent(self, event): # Save settings when closing the app
        self.settings_manager.save_settings()
        event.accept()

class MongoDB:
    def __init__(self, mongo_url=None, port=27017, mongo_username=None, mongo_password=None, mongo_database=None, mongo_collection=None, cluster=None, parent=None):
        self.mongo_url = mongo_url
        self.port = port
        self.mongo_username = mongo_username
        self.mongo_password = mongo_password
        self.mongo_database = mongo_database
        self.mongo_collection = mongo_collection
        self.cluster = cluster
        self.client = None
        self.db = None
        self.is_connected = False
        self.parent = parent  # Add reference to parent window to access radio button

    def connect(self):
        try:
            # Check radio button state and use appropriate URI
            if self.parent and self.parent.radio_on_mongo_cloud.isChecked():
                # MongoDB Atlas (Cloud) connection
                uri = f"mongodb+srv://{self.mongo_username}:{self.mongo_password}@{self.mongo_url}/?retryWrites=true&w=majority&appName={self.cluster}"
                self.client = MongoClient(uri, server_api=ServerApi('1'))
            else:
                # Local MongoDB connection
                uri = f"mongodb://{self.mongo_username}:{self.mongo_password}@{self.mongo_url}:{self.port}/"
                self.client = MongoClient(uri)

            # Check if the database exists by listing databases
            db_list = self.client.list_database_names()
            self.db = self.client[self.mongo_database]

            self.client.admin.command('ping')
            self.is_connected = True

            if self.parent:
                self.parent.label_connection.setText("Connected to MongoDB")
            print("Ping to MongoDB server successful")
            QMessageBox.information(None, "MongoDB", f"Successfully connected {self.mongo_url}")
            
            if self.mongo_database not in db_list:
                print(f"Database '{self.mongo_database}' not found. Creating it...")
                self.db.create_collection(self.mongo_collection)
                print(f"Database '{self.mongo_database}' and empty collection '{self.mongo_collection}' created successfully.")

            else:
                collection_list = self.db.list_collection_names()
                if self.mongo_collection not in collection_list:
                    print(f"Collection '{self.mongo_collection}' not found in '{self.mongo_database}'. Creating it...")
                    self.db.create_collection(self.mongo_collection)
                    print(f"Empty collection '{self.mongo_collection}' created in existing database '{self.mongo_database}'.")
                else:
                    print(f"Connected to existing database '{self.mongo_database}' and collection '{self.mongo_collection}'.")

        except pymongo.errors.OperationFailure as e:
            if self.parent:
                self.parent.label_connection.setText("Failed to connected to MongoDB")
            QMessageBox.critical(None, "FAILED TO CONNECT", "Authentication failed. Please check your credentials.")
        except pymongo.errors.ServerSelectionTimeoutError as e:
            if self.parent:
                self.parent.label_connection.setText("Failed to connect to MongoDB")
            QMessageBox.critical(None, "Connection Error", f"Could not connect to MongoDB server: {e}")
        except Exception as e:
            if self.parent:
                self.parent.label_connection.setText("Failed to connect to MongoDB")
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
        on_mongo_cloud = self.settings.value('on_mongo_cloud')
        mongo_database = self.settings.value('mongo_database')
        mongo_collection = self.settings.value('mongo_collection')
        mongo_username = self.settings.value('mongo_username')
        encrypted_mongo_password = self.settings.value('mongo_password')
        mongo_cluster = self.settings.value('mongo_cluster')

        if size is not None:
            self.main_window.resize(size)
        if pos is not None:
            self.main_window.move(pos)
        if dark == 'true':
            self.main_window.action_dark_mode.setChecked(True)
            self.main_window.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
        if mongo_url is not None:
            self.main_window.line_mongo_url.setText(mongo_url)
        if on_mongo_cloud == 'true':
            self.main_window.radio_on_mongo_cloud.setChecked(True)
            self.main_window.line_mongo_cluster.setEnabled(True)
        if mongo_cluster is not None:
            self.main_window.line_mongo_cluster.setText(mongo_cluster)
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
        self.settings.setValue('on_mongo_cloud', self.main_window.radio_on_mongo_cloud.isChecked())
        self.settings.setValue('mongo_cluster', self.main_window.line_mongo_cluster.text())

class AboutWindow(QDialog, about_ui): 
    def __init__(self, dark_mode=False):
        super().__init__()
        self.setupUi(self)
        if dark_mode:
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
        self.button_ok.clicked.connect(self.accept)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())