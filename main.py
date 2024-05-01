import cv2
import numpy as np
import pyautogui
import keyboard

fps = 24.0
output_file = 'grabacion.mp4'

screen_size = pyautogui.size()

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_file, fourcc, fps, screen_size)

try:
    while True:
        frame = np.array(pyautogui.screenshot())
        frame = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)

        out.write(frame)

        if keyboard.is_pressed('*'):
            break

except Exception as e:
    print(f"Error: {str(e)}")

finally:
    out.release()
    cv2.destroyAllWindows()


