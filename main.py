import time
import pyautogui

from pywinauto.keyboard import send_keys
from pywinauto import Application

app = Application(backend='uia').start(r'mspaint.exe')
dlg = app.window(title_re='.* - Paint')
if dlg.is_maximized() == False:
    dlg.maximize()

#app.dlg.print_control_identifiers()

#app.AdsızPaint.Button29.click()
#app.AdsızPaint.Yakınlaştır.click()
#app.AdsızPaint.YakınlaştırButton.click()
app.AdsızPaint.child_window(title="Yakınlaştır", auto_id="53253", control_type="Button").click()

pyautogui.moveTo(500, 200, 2)

time.sleep(2)

distance = 500
while distance > 0:
    pyautogui.drag(distance, 0, 1, button="left")       # move right
    distance = distance - 20
    pyautogui.drag(0, distance, 1, button="left")       # move down
    pyautogui.drag(-distance, 0, 1, button="left")      # move left
    distance = distance - 20
    if distance > 0:
        pyautogui.drag(0, -distance, 1, button="left")  # move up
time.sleep(2)


dlg.child_window(title="Kaydet", control_type="Button").invoke()
send_keys("Automated Drawing in Paint")
dlg.child_window(title="Kaydet", auto_id="1", control_type="Button").invoke()

# Close application
dlg.close()
