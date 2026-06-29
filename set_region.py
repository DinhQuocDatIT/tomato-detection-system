import cv2
import numpy as np

video_path = "assets/test_v1.mp4"
points = []

def mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        print("Point:", (x, y))


cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Cannot open video")
    exit()

ret, frame = cap.read()
if not ret:
    print("Cannot read frame")
    exit()

cv2.namedWindow("Select Region")
cv2.setMouseCallback("Select Region", mouse)

while True:
    img = frame.copy()

    # vẽ điểm
    for p in points:
        cv2.circle(img, p, 5, (0, 0, 255), -1)

    # vẽ đường nối
    if len(points) > 1:
        cv2.polylines(img, [np.array(points, np.int32)], False, (0, 255, 255), 2)

    # nếu đủ 3 điểm trở lên thì vẽ preview khép kín
    if len(points) > 2:
        cv2.polylines(img, [np.array(points, np.int32)], True, (0, 255, 0), 2)

    cv2.putText(img, "Press S to save | ESC to exit", (20, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.imshow("Select Region", img)

    key = cv2.waitKey(1)

    # lưu
    if key == ord('s'):
        break

    # reset điểm
    if key == ord('r'):
        points = []
        print("Reset points")

    # thoát
    if key == 27:
        exit()

cv2.destroyAllWindows()

print("\nFINAL POLYGON:")
print(np.array(points, np.int32))