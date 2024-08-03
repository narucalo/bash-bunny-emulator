import pyautogui
import time
import webbrowser

def run_payload():
    time.sleep(1)  # Initial delay
    print("Opening URL in web browser...")
    webbrowser.open('https://www.example.com')
    print("Payload executed.")

if __name__ == "__main__":
    run_payload()
