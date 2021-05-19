from dialog import Message
from bobber_window import Box

import win32api, pyautogui, time

WINDOW_DIALOG = Message()
class gamePlayer():
    def __init__(self):
        self.cast_button_position = self.cast_button_position()
        self.bobber_window = self.get_bobber_window()

    def __get_mouse_position_on_click(self):
        while True:
            cur_mouse = win32api.GetAsyncKeyState(0x01)
            if cur_mouse < 0:
                cur_pos = pyautogui.position()
                break
        
        return(cur_pos.x,cur_pos.y)

    def __auto_find_button(self):
        try:
            cast_button_img = pyautogui.locateOnScreen('../assets/fish_button.png')
            return(cast_button_img.left,cast_button_img.top)
        except:
            return False

    def cast_button_position(self):
        # Make it find the button automatically
        auto_found_button = self.__auto_find_button()
        if auto_found_button:
            return auto_found_button
        WINDOW_DIALOG.create_dialog_message("Information","After this dialog, Please click on the Cast/Reel Button")
        return self.__get_mouse_position_on_click()
    
    def get_bobber_window(self):
        WINDOW_DIALOG.create_dialog_message("Information","After this dialog, Please click on the Bobber\n\n(Please ensure the bobber is easily visible)")
        cur_mouse_pos = self.__get_mouse_position_on_click()
        return Box(cur_mouse_pos)
    
    def catch_fish_and_reset_bobber(self):
        ## Make it find the bobber on screen each time
        self.__click_cast_button()
        time.sleep(2)
        self.__click_cast_button()
        time.sleep(5)
    
    def check_key_pressed_for_cancel(self):
        if keyboard.read_key() == "esc":
            return True
        


    def __click_cast_button(self):
        pyautogui.moveTo(self.cast_button_position[0], self.cast_button_position[1])
        pyautogui.click()
