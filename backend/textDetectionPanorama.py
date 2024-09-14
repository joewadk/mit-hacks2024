import cv2
import pytesseract
import time

pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

cap = cv2.VideoCapture(1)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480))
font = cv2.FONT_HERSHEY_COMPLEX

image_counter = 0
captured_images = []
start_time = time.time()
while cap.isOpened():
    (ret, frame) = cap.read()  # ret is False if frames couldn't be grabbed
    if ret == True:
        frame = cv2.flip(frame, 1)
        cv2.putText(frame, "RxLabel", (200, 100), font, 2, (0, 0, 255), 3)
        out.write(frame)
        cv2.imshow("current frame", frame)

        current_time = time.time()

        key = cv2.waitKey(1) & 0xFF

        if current_time - start_time <= 0.5:
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            equalized_frame = cv2.equalizeHist(gray_frame)
            improved_frame = cv2.cvtColor(equalized_frame, cv2.COLOR_GRAY2BGR)
            resized_frame = cv2.resize(improved_frame, (640, 480))
            captured_images.append(resized_frame)

            print(f"Captured frame {image_counter}")
            image_counter += 1

            start_time = current_time

            # image_filename = f"capture_{image_counter}.jpg"
            # cv2.imwrite(image_filename, frame)
            # print(f"Captured and saved: {image_filename}")
            # resized_frame = cv2.resize(frame, (640, 480))
            # captured_images.append(resized_frame)
            # image_counter += 1

        if key == ord("q"):
            break

    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Captured {len(captured_images)} images.")

# stich the images together
if len(captured_images) > 1:
    print("Stitching images together...")

    stitcher = cv2.Stitcher.create(cv2.Stitcher_SCANS)

    (status, stitched) = stitcher.stitch(captured_images)

    if status == cv2.Stitcher_OK:
        cv2.imshow("Panoramic Label", stitched)
        cv2.waitKey(0)
        cv2.imwrite("stitched_panorama.jpg", stitched)
    else:
        print(f"error in stitching: {status}")
