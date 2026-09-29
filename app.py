import os
import webview

def start_app():
    # 1. Locate the folder where this app.py file is saved
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 2. Point directly to your main index.html file in that folder
    entry_point = os.path.join(current_dir, 'index.html')
    
    # 3. Create a desktop window (Change the title and size if you want)
    webview.create_window(
        title='My Desktop App', 
        url=entry_point, 
        width=1024, 
        height=768,
        resizable=True
    )
    
    # 4. Launch the application window
    webview.start()

if __name__ == '__main__':
    start_app()