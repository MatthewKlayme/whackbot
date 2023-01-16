import cv2 #used to read computer images and read the screen
import pyautogui #used to control keyboard and mouse
from time import sleep


pyautogui.PAUSE = 0 

#template and dimensions
template = cv2.imread("../imgs/nose.png") #reads the image
template_gray = cv2.cvtColor(template, cv2.COLOR_RGB2GRAY) #convers template img to gray
template_w, template_h = template_gray.shape[::-1]

#game window dimensions
x,y,w,h = 415, 530, 640, 540

#wait
sleep(3)

#main
while True: #constantly run bot until told to stop

    #screenshot          name of scrnshot  where we want the screen shot to take a screen shot of
    pyautogui.screenshot("../imgs/image.png", (x,y,w,h))
    #read the scrnshot we just took
    image = cv2.imread("../imgs/image.png")

    while True:
        image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

        #matching scrnshot with nose picture
        result = cv2.matchTemplate(
            image = image_gray, #screen shot
            templ = template_gray, #compare to nose image provided
            method = cv2.TM_CCOEFF_NORMED #method used to compare images
        )

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        #threashold
        if max_val >= 0.8:
            pyautogui.click(
                #x and y coordiante of where to click
                x = max_loc[0] + x,
                y = max_loc[1] + y 
            )

            image = cv2.rectangle(
                img = image,
                #drawing a rectangle at pt1 = max_loc which is a tuple of the x and y coordinates of the img
                pt1 = max_loc,
                pt2 = (
                    max_loc[0] + template_w,
                    max_loc[1] + template_h
                ),
                color = (0,255,0),
                thickness = -1
            )

        else:
            break