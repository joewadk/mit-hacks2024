import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

cap = cv2.VideoCapture(1)
img = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Video Stream - Press 'Space' to Capture", frame)

    key = cv2.waitKey(1)
    if key == ord(" "):
        img = frame
        break
    elif key == ord("q"):
        cap.release()
        cv2.destroyAllWindows()
        exit()

cap.release()

if img is not None:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    height, width, _ = img.shape

    boxes = pytesseract.image_to_data(img)
    for x, b in enumerate(boxes.splitlines()):
        if x != 0:
            b = b.split()
            if len(b) == 12:
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 1)
                cv2.putText(
                    img, b[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.75, (50, 50, 255), 1
                )

    cv2.imshow("Detected Text", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No image was captured.")

print(pytesseract.image_to_string(img))
