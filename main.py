from pynput.mouse import Button, Controller
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
    sift = cv2.xfeatures2d.SIFT_create()
    kp_1, desc_1 = sift.detectAndCompute(img, None)
    kp_2, desc_2 = sift.detectAndCompute(img2, None)
    index_params = dict(algorithm = 0, trees = 5)
    good_points = []
    search_params = dict()
    flann = cv2.FlannBasedMatcher(index_params,search_params)
    try:
        matches = flann.knnMatch(desc_1,desc_2,k=2)
        ratio = 0.6
        for m, n in matches:
            if m.distance < ratio*n.distance:
                good_points.append(m)
    except:
        return True
    return False


def detChange(img):
    pic2 = cv2.imwrite('pic2.png',img)
    master = cv2.imread('pic.png')
    imgs = cv2.imread('pic2.png')
    return checkSimilarity(master,imgs)
    



def screen_record():
    mon = {"top": 600, "left": 250, "width": 50, "height": 100}
    title = ""
    fps = 0
    sct = mss.mss()
    last_time = time.time()
    mouse = Controller()
    while True:
        img = numpy.asarray(sct.grab(mon))
        fps += 1
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        cv2.imwrite('pic.png',img)
        detChange(img)
        if detChange(img):
            mouse.position = (965,967)
            mouse.click(Button.left,1)
            time.sleep(2)
            mouse.click(Button.left,1)
            time.sleep(5)
            cv2.imwrite('pic2.png',img)
        else:
            pass
##        lower = numpy.array([100,0,0])
##        upper= numpy.array([255,255,255])
##        mask = cv2.inRange(img,lower,upper)
##        res = cv2.bitwise_and(img,img, mask= mask)
        cv2.imshow('hello',img)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    return True

screen_record()
