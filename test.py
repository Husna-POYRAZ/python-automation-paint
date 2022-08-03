import pywinauto
import pyautogui
import time
from pywinauto import Application
from pywinauto.keyboard import send_keys
app = Application(backend='uia').start(r'mspaint.exe')
dlg = app.window(title_re='.* - Paint')
time.sleep(2)
#app.dlg.print_control_identifiers()

time.sleep(3)
pyautogui.moveTo(500, 200, 3)
time.sleep(1)
distance = 300
while distance > 0:
    pyautogui.dragRel(distance, 0, 1, button="left")
    distance = distance - 20
    pyautogui.dragRel(0, distance, 1, button="left")
    pyautogui.dragRel(-distance, 0, 1, button="left")
    distance = distance - 20
    if distance > 0:
        pyautogui.dragRel(0, -distance, 1, button="left")

time.sleep(2)


dlg.child_window(title="Kaydet", control_type="Button").invoke()
#dlg.child_window(title="Resimler (sabitlenmiş)", control_type="TreeItem").invoke()
send_keys("Automated Drawing in Paint")
dlg.child_window(title="Kaydet", auto_id="1", control_type="Button").invoke()





""" 
time.sleep(3)
pyautogui.moveTo(500, 200, 3)
time.sleep(1)
distance = 300
while distance > 0:
    pyautogui.dragRel(distance, 0, 1, button="left")
    distance = distance - 20
    pyautogui.dragRel(0, distance, 1, button="left")
    pyautogui.dragRel(-distance, 0, 1, button="left")
    distance = distance - 20
    if distance > 0:
        pyautogui.dragRel(0, -distance, 1, button="left")

time.sleep(2)
"""