import cv2

face_ref = cv2.CascadeClassifier("training-code.xml") # This is training code reference
camera = cv2.VideoCapture(0)

def face_detection(frame):
    optimize_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    faces = face_ref.detectMultiScale(optimize_frame, scaleFactor=1.1)
    return faces

def drawer_box(frame):
    for x, y, w, h in face_detection(frame):

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2) # You can customize 0, 0, 255, it's the color of the box

        name = "5025251143 - Ahmad Fakhrul Bawani"  # Change with your name
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.6
        thickness = 2
        text_size, _ = cv2.getTextSize(name, font, font_scale, thickness)
        text_x = x + (w - text_size[0]) // 2  
        text_y = y + h + text_size[1] + 5     
        cv2.putText(frame, name, (text_x, text_y), font, font_scale, (0, 255, 0), thickness) # You can customize 0, 0, 255, it's the color of the text

def close_window():
    camera.release()
    cv2.destroyAllWindows()
    exit()

def main():
    while True:
        _, frame = camera.read()
        drawer_box(frame)
        cv2.imshow("GENICS SC AI", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'): # this ord can be changed to other key. This is exit key!
            close_window()

if __name__ == '__main__':
    main()
