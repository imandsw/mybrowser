# Import necessary modules
import sys  # System-specific parameters and functions
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit  # GUI components
from PyQt6.QtWebEngineWidgets import QWebEngineView  # Web browser widget
from PyQt6.QtCore import QUrl  # URL handling class

# Define the browser class inheriting from QMainWindow
class SimpleBrowser(QMainWindow):
    def __init__(self):
        super().__init__()  # Initialize parent class

        # Set window properties
        self.setWindowTitle("My First Python Browser")  # Set window title
        self.setGeometry(100, 100, 800, 600)  # Set window position and size (x, y, width, height)

        # Create and configure the web browser view
        self.browser = QWebEngineView()  # Initialize web engine view
        self.browser.setUrl(QUrl("https://www.google.com"))  # Set default homepage to Google

        # Create and configure URL input bar
        self.url_bar = QLineEdit()  # Create text input field
        self.url_bar.setPlaceholderText("Enter URL and press Enter")  # Set placeholder text
        self.url_bar.returnPressed.connect(self.load_url)  # Connect Enter key to load_url method

        # Create navigation buttons and connect their click events
        self.back_button = QPushButton("Back")  # Back navigation button
        self.back_button.clicked.connect(self.browser.back)  # Connect to browser's back function

        self.forward_button = QPushButton("Forward")  # Forward navigation button
        self.forward_button.clicked.connect(self.browser.forward)  # Connect to browser's forward function

        self.refresh_button = QPushButton("Refresh")  # Refresh button
        self.refresh_button.clicked.connect(self.browser.reload)  # Connect to browser's reload function

        # Set up layout
        layout = QVBoxLayout()  # Create vertical box layout
        # Add widgets to layout in order (top to bottom)
        layout.addWidget(self.url_bar)  # Add URL bar at top
        layout.addWidget(self.back_button)  # Add back button
        layout.addWidget(self.forward_button)  # Add forward button
        layout.addWidget(self.refresh_button)  # Add refresh button
        layout.addWidget(self.browser)  # Add browser view (takes remaining space)

        # Create container widget and apply layout
        container = QWidget()  # Create central widget container
        container.setLayout(layout)  # Apply the vertical layout to container
        self.setCentralWidget(container)  # Set container as main window content

    # Method to handle URL loading
    def load_url(self):
        url = self.url_bar.text()  # Get text from URL bar
        # Ensure URL has proper protocol prefix
        if not url.startswith("http"):  # Check if URL starts with http
            url = "http://" + url  # Add http:// if missing
        self.browser.setUrl(QUrl(url))  # Load the URL in browser

# Main execution block
if __name__ == "__main__":
    app = QApplication(sys.argv)  # Create application instance with command line args
    window = SimpleBrowser()  # Create browser window instance
    window.show()  # Display the window
    sys.exit(app.exec())  # Start application event loop and exit when done