# pyautogui.click -> click with the mouse
# pyautogui.write -> type with the keyboard
# pyautogui.press -> press a keyboard key
# pyautogui.hotkey -> press a keyboard shortcut
# pyautogui.PAUSE = 1 -> waiting time between each command
# pyautogui -> mouse and keyboard automation library
# pandas -> data manipulation library
# openpyxl -> Excel file manipulation library

import pyautogui
import time
import pyperclip
import pandas

pyautogui.PAUSE = 0.5

# Challenge step-by-step
# Step 1: Access the company system using the Google Drive link
# Open the Opera browser
pyautogui.press('win')
pyautogui.write('opera')
pyautogui.press('enter')

time.sleep(2)  # Wait for the browser to open

# Type the Google Drive link
link = 'https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga'
pyautogui.write(link)

# Press Enter to access the Drive folder and wait for the page to load
pyautogui.press('enter')
time.sleep(3)  # Wait for the page to load

# Step 2: Navigate through the system to find the data folder
pyautogui.click(x=545, y=483, clicks=2)  # Click on the data folder
time.sleep(1)  # Wait for the folder to open

# Step 3: Download the data file
pyautogui.click(x=1777, y=482)  # Click on the file's three-dot menu
time.sleep(5)  # Wait for the file options menu to open

pyautogui.click(x=1382, y=606)  # Click on the download option
time.sleep(5)  # Wait for the download to finish

# Step 4: Calculate the indicators: revenue and number of products sold
# Open the database file
file_path = r"C:\Users\guiap\Downloads\Vendas - Dez.xlsx"
table = pandas.read_excel(file_path)

# Display the sales database
print(table)

# Calculate the total revenue by summing the "Final Value" column
revenue = table['Valor Final'].sum()

# Calculate the total number of products sold by summing the "Quantity" column
quantity_sold = table['Quantidade'].sum()

print(revenue)
print(quantity_sold)

# Step 5: Send the indicators to the manager by email
pyautogui.hotkey('ctrl', 't')  # Open a new browser tab
pyautogui.write('https://mail.google.com/')  # Access Gmail
pyautogui.press('enter')

time.sleep(5)  # Wait for Gmail to open

pyautogui.click(x=168, y=255)  # Click on the compose email button
time.sleep(5)  # Wait for the compose email window to open

# Email recipient
pyautogui.write('limaguiti@gmail.com')
pyautogui.press('tab')
pyautogui.press('tab')  # Move to the email subject field

# Email subject
pyperclip.copy('Sales Report')  # Copy the text to the clipboard
pyautogui.hotkey('ctrl', 'v')  # Paste the text into the subject field
pyautogui.press('tab')  # Move to the email body field

# Email body
message = f'''
Dear team,

Please find below today's sales report:

Revenue: R${revenue:,.2f}
Number of products sold: {quantity_sold:,}

If you have any questions, please let me know.

Best regards,
Guilherme
'''

pyperclip.copy(message)  # Copy the message to the clipboard
pyautogui.hotkey('ctrl', 'v')  # Paste the message into the email body

# Send the email
pyautogui.click(x=1225, y=985)  # Click on the send button