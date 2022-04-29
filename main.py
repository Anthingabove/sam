print("[SERVER] Connecting to selenium server...")
import os
os.system("pip install selenium==3.141.0")
from webbot import Browser
print("[SELENIUM] Installing chromedriver.exe...")

driver = Browser()
print("[SELENIUM, SERVER] The operation has been completed.")

print("[SERVER] Listening keyboard input...")

input("Server connected!")

print("[SERVER] Disconnected. Please restart the server and try again.")