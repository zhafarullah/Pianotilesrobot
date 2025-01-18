import cv2
import numpy as np
import pygetwindow as gw
import mss
import time
import serial
import keyboard  

ser = serial.Serial('COM12', 115200)

window = gw.getWindowsWithTitle('SM-P615')[0]

left, top, width, height = window.left, window.top, window.width, window.height

custom_width = int(width * 0.97)
custom_height = int(height * 0.3)
offset_x = 0
offset_y = 0

monitor = {
    "top": top + offset_y,
    "left": left + offset_x,
    "width": custom_width,
    "height": custom_height
}

def tiles_filter(img):
    lower_black = np.array([0, 0, 0], dtype=np.uint8)
    upper_black = np.array([110, 70, 30], dtype=np.uint8)
    
    lower_blue = np.array([111, 66, 0], dtype=np.uint8)
    upper_blue = np.array([255, 157, 20], dtype=np.uint8)
    
    mask_black = cv2.inRange(img, lower_black, upper_black)
    mask_blue = cv2.inRange(img, lower_blue, upper_blue)
    
    mask = cv2.bitwise_or(mask_black, mask_blue)
    
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.dilate(mask, kernel, iterations=1)
    
    inverse_mask = cv2.bitwise_not(mask)
    result = img.copy()
    result[inverse_mask > 0] = [255, 255, 255] 
    
    return result

def detector_line(img, line_y_position, start_x, end_x, line_number):
    if reading:
        line_pixels = img[line_y_position, start_x:end_x]
        non_white = np.any(line_pixels != [255, 255, 255])
        if non_white:
            center_x = (start_x + end_x) // 2
            cv2.circle(img, (center_x, line_y_position), 20, (0, 0, 255), -1)
            return line_number
    return 0

reading = False 

def toggle_reading():
    global reading
    reading = not reading

keyboard.on_press_key('space', lambda _: toggle_reading())

previous_time = time.time()

with mss.mss() as sct:
    while True:
        screen = np.array(sct.grab(monitor))
        frame = cv2.cvtColor(screen, cv2.COLOR_BGRA2BGR)
        
        masked_frame = tiles_filter(frame)
        
        line_y_position = int(custom_height * 0.7)
        line_length = 100
        
        colors = [(0, 255, 0), (0, 0, 255), (255, 0, 0), (0, 255, 255)]
        results = []
        
        for i in range(4):
            center_x = int(((custom_width) / 4) * (i + 0.5)) 
            start_x = center_x - line_length // 2
            end_x = center_x + line_length // 2
            result = detector_line(masked_frame, line_y_position, start_x, end_x, i + 1)
            results.append(result)
            cv2.line(masked_frame, (start_x, line_y_position), (end_x, line_y_position), colors[i], 2)

        
        data_to_send = ','.join(map(str, results)) + '\n'
        ser.write(data_to_send.encode())
        print(data_to_send)
        
        current_time = time.time()
        fps = 1 / (current_time - previous_time)
        previous_time = current_time
        
        cv2.putText(masked_frame, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.imshow('Scrcpy HSV Mask', masked_frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()
ser.close()
