import pyautogui
from time import sleep

# Para ENcontrar a possiçao Point(x=125, y=462)
# sleep(2)
# print(pyautogui.position())
#
sleep(1.5)
pyautogui.click(125, 462, clicks=1, interval=4, button='left')


# possiçao --> CNPJ  Point(x=263, y=462)
# sleep(2)
# print(pyautogui.position())

sleep(1)
pyautogui.click(263, 462, clicks=1, interval=1, button='left')
pyautogui.write("12.279.725/0001-40")
# pyautogui.write("23.542.756/0001-68")

# possiçao --> Data  Point(x=410, y=462)
# sleep(2)
# print(pyautogui.position())

# sleep(1)
pyautogui.click(410, 462, clicks=1, interval=1, button='left')
pyautogui.write("04/11/1987")
# pyautogui.write("25/10/1988")

# possiçao --> Data  Point(x=536, y=462)
# sleep(2)
# print(pyautogui.position())

# sleep(1)
pyautogui.click(536, 462, clicks=1, interval=2, button='left')
