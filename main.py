import pyautogui
import time
pyautogui.FAILSAFE = False

#this mean it will like first 5 posts where from you start liking . you can change the value no problem 
for i in range(0,10):
    #this for delay events of like on per post. other wise you get gifts from Facebook
    time.sleep(0.5)

    #for select post
    pyautogui.press("j")
    #for opening like tab
    pyautogui.press("l")

    #you can use more buttons event to select other option
    #like , love, sad , angry ... etc. let me show you .

    pyautogui.press(['right','right'])
    #execute
    pyautogui.press("enter")

# so easy to react anywhere
