from pynput.mouse import Button, Controller
mouse = Controller()
from pynput.keyboard import Key, Controller
keyboard = Controller()
from pywinauto.application import Application
from PIL import Image, ImageGrab, ImageDraw
import pyautogui, cv2, time, numpy, mss

#X965, Y: 967
class gamePlayer():
    def __init__(self):
        self.casted = False
        self.mouse = Controller()
        self.mouse.position = (965,967)

    def cast_line(self):
        if not self.casted:
            self.casted = True
            self.mouse.click(Button.left,1)

def screenGrab():
    im = ImageGrab.grab()
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
'.png','PNG')
    return 'full_snap__' + str(int(time.time()))+'.png'

def checkSimilarity(img,img2):
    master_file = img
    black1 = numpy.array([0,0,0], dtype=numpy.uint8)
    black2 = numpy.array([0,0,0], dtype=numpy.uint8)
    mask = cv2.inRange(img2, black1, black2)
    cv2.imshow('m',mask)
    compare_file = img2
    difference = cv2.subtract(master_file,compare_file)
    r,g,b = cv2.split(difference)
    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
        return True
    else:
        return False


def detChange(img):
    pic2 = cv2.imwrite('pic2.png',img)
    master = cv2.imread('pic.png')
    imgs = cv2.imread('pic2.png')
    return checkSimilarity(master,imgs)
    



def screen_record():
    mon = {"top": 600, "left": 250, "width": 100, "height": 100}
    title = ""
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
        cv2.imwrite('pic.png',mask)
        if detChange(img):
            mouse.position = (965,967)
            mouse.click(Button.left,1)
            time.sleep(2)
            mouse.click(Button.left,1)
            time.sleep(2)
            cv2.imwrite('pic2.png',mask)
        else:
            pass
        cv2.imwrite('pic2.png',mask)
        cv2.imshow('Bobber cam',mask)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    return True

screen_record()

