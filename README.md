# mybrowser
MyBrowser is a simple, fast, and minimal web browser built for efficiency. Designed with a clean UI and essential browsing features, it offers a lightweight alternative to mainstream browsers.

Here's the complete README content in a single block that you can copy all at once:
markdown

# Simple Python Browser

A basic web browser built with Python and PyQt6, featuring a URL bar and basic navigation controls.

## Features
- URL input bar with Enter key support
- Navigation buttons (Back, Forward, Refresh)
- Web page rendering using QWebEngineView
- Default homepage set to Google
- Automatic HTTP prefix addition for URLs

## Requirements
- Python 3.x
- PyQt6 library

## Installation

1. Install Python 3.x if not already installed
2. Install PyQt6 using pip:

pip install PyQt6 PyQt6-WebEngine


## Usage

1. Clone or download this repository
2. Navigate to the project directory
3. Run the browser:

python simple_browser.py

4. Enter a URL in the text field and press Enter to navigate
5. Use the navigation buttons to:
   - Go Back to previous page
   - Go Forward to next page
   - Refresh current page

## Code Structure
```python
simple_browser.py
├── SimpleBrowser class
│   ├── __init__ - Initializes window and widgets
│   └── load_url - Handles URL loading
└── Main execution block
```
## Dependencies

    PyQt6.QtWidgets - GUI components
    PyQt6.QtWebEngineWidgets - Web browsing functionality
    PyQt6.QtCore - URL handling

## Screenshot

    ![](/browser1.png)
    ![](/browser2.png)
    ![](/browser3.png)
    The browser window is created using QMainWindow
    Web content is rendered with QWebEngineView
    Navigation controls are implemented with QPushButton
    URL input uses QLineEdit with Enter key detection
    Layout is managed with QVBoxLayout

## Limitations

    No bookmark functionality
    No tab support
    Basic error handling
    No history view

Contributing
Feel free to fork this repository and submit pull requests with improvements!