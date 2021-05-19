from player import gamePlayer
import cv2, time, numpy, mss,keyboard


# X = 1294, Y= 1343
def calibration():
    return gamePlayer()

        
def screen_record(player_obj):
    mon = {"top": player_obj.bobber_window.top, "left": player_obj.bobber_window.left, "width": player_obj.bobber_window.width, "height": player_obj.bobber_window.height}
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
            player_obj.catch_fish_and_reset_bobber()
        # cv2.imwrite('pic2.png',mask)
        # cv2.imshow('Bobber cam',mask)
        if keyboard.is_pressed("esc"): # hold esc to close
            break
    return True


if __name__ == "__main__":
    # Run Calibration
    Player = calibration()
    # Select square
    screen_record(Player)

