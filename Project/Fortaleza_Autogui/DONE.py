import pyautogui
from time import sleep

def auto(CNPJ,DATE):
    sleep(1.5)
    pyautogui.click(125, 462, clicks=1, interval=4, button='left')

    sleep(1)
    pyautogui.click(263, 462, clicks=1, interval=1, button='left')
    pyautogui.write(str(CNPJ))
    # pyautogui.write("23.542.756/0001-68")

    pyautogui.click(410, 462, clicks=1, interval=1, button='left')
    pyautogui.write(str(DATE))
    # pyautogui.write("25/10/1988")

    pyautogui.click(536, 462, clicks=1, interval=2, button='left')

cnpj = "12.279.725/0001-40"
data = "04/11/1987"