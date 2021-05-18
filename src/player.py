from dialog import Message
from bobber_window import Box
import win32api, pyautogui

WINDOW_DIALOG = Message()
class gamePlayer():
    def __init__(self):
        self.cast_button_position = self.cast_button_position()
        self.bobber_window = self.get_bobber_window()

    def __get_mouse_position_on_click(self):
        while True:
            cur_mouse = win32api.GetAsyncKeyState(0x01)
            if cur_mouse < 0:
                break
        return pyautogui.position()

    def cast_button_position(self):
        WINDOW_DIALOG.create_dialog_message("Information","After this dialog, Please click on the Cast/Reel Button")
        return self.__get_mouse_position_on_click()
    
    def get_bobber_window(self):
        WINDOW_DIALOG.create_dialog_message("Information","After this dialog, Please click on the Bobber\n\n(Please ensure the bobber is easily visible)")
        cur_mouse_pos = self.__get_mouse_position_on_click()
        return Box(cur_mouse_pos)

    def cast_line(self):
        if not self.casted:
            self.casted = True
            self.mouse.click(Button.left,1)