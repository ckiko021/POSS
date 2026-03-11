import cv2
from pyzbar.pyzbar import decode

def scan_barcode():

    cap = cv2.VideoCapture(0)

    while True:

        ret, frame = cap.read()

        for barcode in decode(frame):

            x, y, w, h = barcode.rect

            # Draw green rectangle
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

            barcode_data = barcode.data.decode("utf-8")

            cap.release()
            cv2.destroyAllWindows()

            return barcode_data

        cv2.imshow("POS Scanner", frame)

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()