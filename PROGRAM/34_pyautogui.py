import pyautogui
def whasappMeseg():
    x=input("Enter Contact Name : ")
    pyautogui.press("win") 
    pyautogui.sleep(1) # Open the Run dialog
    pyautogui.typewrite("what")
    pyautogui.sleep(1)
    pyautogui.press("enter")
    pyautogui.sleep(3)
    pyautogui.hotkey("ctrl", "f")
    pyautogui.typewrite(f"{x}")
    pyautogui.sleep(1)  
    pyautogui.press('down')
    pyautogui.press("enter")
    pyautogui.sleep(2)

    import list_module as ls

    li=ls.gujarat_districts
    for i in range(3):
        pyautogui.typewrite(f"Good night ")
        pyautogui.press("enter")
        pyautogui.sleep(1)

whasappMeseg()