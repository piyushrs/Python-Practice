import pyautogui as pyg
# import time
# time.sleep(2)
# print(pyg.position())
pyg.hotkey("Win", "4")
# print("Success")
# pyg.click(42,286) #for nutella's server
pyg.click(36,176) #for my server
pyg.click(744,996,1)
for i in range(5):
    pyg.typewrite("@mys")
    # pyg.typewrite("@chukka")
    pyg.press("enter")
    pyg.typewrite("@izze")
    pyg.press("enter")
    # pyg.typewrite("@briya")
    # pyg.press("enter")
    pyg.typewrite("@lelou")
    pyg.press("enter")
#     # # pyg.typewrite("@jermie")
    # pyg.press("enter")
    # pyg.typewrite(":bread~1:")
    pyg.typewrite(":fingerping:")
    pyg.press("enter")
    pyg.press("enter")
pyg.hotkey("Win", "m")

# print(pyg.KEYBOARD_KEYS)