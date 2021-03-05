import os 
import cv2
import numpy as np
import win32api
import win32gui
import win32con
import subprocess
import pyautogui
from PIL import Image

# subprocess.call(r"D:\steam\steam.exe -applaunch 1499560")

hwnd = win32gui.FindWindow(None, "LastCloudia") 
left, top, right, bottom = win32gui.GetWindowRect(hwnd)

print(left, top, right, bottom)

middle = [int((left+right)/2), int((top+bottom)/2)]

w = right - left # width
h = bottom - top # height

win32gui.MoveWindow(hwnd, left, top, 540, 960, True)
# print(pyautogui.size())

# win32api.SetCursorPos(middle)
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
im = pyautogui.screenshot(region=(left,top, 540, 960))

test = pyautogui.screenshot(region=(1940,935, 2220-1940, 1020-935))
# test = test.save('stardt.jpg')
 
img = cv2.cvtColor(np.asarray(im),cv2.COLOR_RGB2BGR)  
# start_img = cv2.imread('stardt.JPG')
start_img = cv2.imread('yes.JPG')

result = cv2.matchTemplate(start_img, img, cv2.TM_CCOEFF_NORMED)
reslist = cv2.minMaxLoc(result)
print(reslist)

# win32api.SetCursorPos([reslist[3][0]+left,reslist[3][1]+top])
find_height, find_width = start_img.shape[:2:]
cv2.rectangle(img, reslist[3], (reslist[3][0]+find_width, reslist[3][1]+find_height), color=(0, 250, 0), thickness=2)

cv2.imshow('dd',img)
cv2.waitKey()








