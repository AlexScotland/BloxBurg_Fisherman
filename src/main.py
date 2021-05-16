from pynput.mouse import Button, Controller, Listener
mouse = Controller()
from pynput.keyboard import Key, Controller
keyboard = Controller()
from pywinauto.application import Application
from PIL import Image, ImageGrab, ImageDraw
import pyautogui, cv2, time, numpy, mss

# X = 1294, Y= 1343
def calibration():
    while True:
        print(mouse.position)
class gamePlayer():
    def __init__(self):
        self.casted = False
        self.mouse = Controller()
        self.mouse.position = (1294,1343)
    
    def get_bobber_window(self):
        pass

    def cast_line(self):
        if not self.casted:
            self.casted = True
            self.mouse.click(Button.left,1)

def screenGrab():
    im = ImageGrab.grab()
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
'.png','PNG')
    return 'full_snap__' + str(int(time.time()))+'.png'

    



def screen_record():
    mon = {"top": 795, "left": 458, "width": 400, "height": 200}
    title = "Test"
    fps = 0
    sct = mss.mss()
    last_time = time.time()
    while True:
        img = numpy.asarray(sct.grab(mon))
        fps += 1
        img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        lower_white = numpy.array([0,0,0], dtype=numpy.uint8)
        upper_white = numpy.array([0,0,255], dtype=numpy.uint8)
        mask = cv2.inRange(img, lower_white, upper_white)
        if cv2.countNonZero(mask) == 0:
            mouse.position = (1294,1343)
            mouse.click(Button.left,1)
            time.sleep(2)
            mouse.click(Button.left,1)
            time.sleep(5)


        # Check whites and see if there is any
        # if there is a white, then we will wait
        # else the bobber is under water

        # if detChange(mask):
        #     mouse.position = (965,967)
        #     mouse.click(Button.left,1)
        #     time.sleep(2)
        #     mouse.click(Button.left,1)
        #     time.sleep(2)
        #     cv2.imwrite('pic2.png',mask)
        # else:
        #     pass
        # cv2.imwrite('pic2.png',mask)
        # cv2.imshow('Bobber cam',mask)
        # k = cv2.waitKey(5) & 0xFF
        # if k == 27:
        #     break
    return True


if __name__ == "__main__":
    # Run Calibration
    # calibration()
    # Select square
    screen_record()

