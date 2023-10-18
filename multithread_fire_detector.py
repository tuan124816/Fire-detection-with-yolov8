# from ultralytics import YOLO
# import cv2

# # Load your YOLOv5 model
# model = YOLO("/Users/huytuannguyen/Desktop/FPT/FAIC/FPTAI/FireDetectionYOLOv8/runs/detect/train/weights/best.pt")

# # Function to check for fire detection
# def check_fire_detection(results):
#     # Make predictions using your model
#     if len(results[0]) == 0:
#         # print('no fire')
#         return False
#     # print('have fire')
#     return True

# # Function to send an alarm message (adjust as needed)
# def send_alarm_message(camrera_ip):
#     print(f"Fire detected from camera {camera_ip}! Sending alarm message...")


# # Open the video capture from your camera (replace '0' with the camera index or the video file path)
# camera_ip = 0
# cap = cv2.VideoCapture(camera_ip)
# fire_frame = 0
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Process the frame (resize, normalize, etc.) as needed
#     # Make predictions using your YOLOv5 model
#     results = model(frame)

#     # Check for fire detection
#     fire_detected = check_fire_detection(results)

#     # If fire is detected, start a timer
#     if fire_detected == True:
#         # draw bouding boxes
#         for result in results:
#             coordinates = result.boxes.xyxy[0].numpy()
#             x_min = int(coordinates[0])
#             y_min = int(coordinates[1])

#             x_max = int(coordinates[2])
#             y_max = int(coordinates[3])
#             cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), color=(255, 0, 0))


#         fire_frame += 1
#     else: 
#         fire_frame = 0

#     # If the timer exceeds a certain threshold (4-5 seconds), trigger the alarm
#     if fire_frame >= 12:
#         send_alarm_message(camera_ip)

#     # You can add code here to display the video frame with detected objects (if needed)
#     # For example, draw bounding boxes around detected fires
#     cv2.imshow('fire detection', frame)

#     # Exit the loop if a key is pressed (for demonstration purposes)
#     key = cv2.waitKey(1)
#     if key == 27:  # Press 'Esc' to exit
#         break

# # Release the camera and close any OpenCV windows
# cap.release()
# cv2.destroyAllWindows()











# from ultralytics import YOLO
# import cv2

# class FireDetectionSystem:
#     def __init__(self, model_path, camera_ip):
#         self.model = YOLO(model_path)
#         self.camera_ip = camera_ip
#         self.fire_frame = 0

#     def check_fire_detection(self, results):
#         if len(results[0]) == 0:
#             return False
#         return True

#     def send_alarm_message(self):
#         print(f"Fire detected from camera {self.camera_ip}! Sending alarm message...")

#     def run(self):
#         cap = cv2.VideoCapture(self.camera_ip)
#         while True:
#             ret, frame = cap.read()
#             if not ret:
#                 break

#             results = self.model(frame)
#             fire_detected = self.check_fire_detection(results)

#             if fire_detected:
#                 for result in results:
#                     coordinates = result.boxes.xyxy[0].numpy()
#                     x_min, y_min, x_max, y_max = map(int, coordinates)
#                     cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), color=(255, 0, 0))
#                 self.fire_frame += 1
#             else:
#                 self.fire_frame = 0

#             if self.fire_frame >= 12:
#                 self.send_alarm_message()

#             cv2.imshow('fire detection', frame)

#             key = cv2.waitKey(1)
#             if key == 27:
#                 break

#         cap.release()
#         cv2.destroyAllWindows()

# if __name__ == "__main__":
#     model_path = "/Users/huytuannguyen/Desktop/FPT/FAIC/FPTAI/FireDetectionYOLOv8/runs/detect/train/weights/best.pt"
#     camera_ip = 0
#     fire_detection_system = FireDetectionSystem(model_path, camera_ip)
#     fire_detection_system.run()










# from ultralytics import YOLO
# import cv2
# import threading

# class FireDetectionSystem:
#     def __init__(self, model_path, camera_ips):
#         self.model = YOLO(model_path)
#         self.camera_ips = camera_ips
#         self.fire_frames = {camera_ip: 0 for camera_ip in camera_ips}
#         self.threads = []

#     def check_fire_detection(self, results):
#         if len(results[0]) == 0:
#             return False
#         return True

#     def send_alarm_message(self, camera_ip):
#         print(f"Fire detected from camera {camera_ip}! Sending alarm message...")

#     def process_camera(self, camera_ip):
#         cap = cv2.VideoCapture(camera_ip)
#         while True:
#             ret, frame = cap.read()
#             if not ret:
#                 break

#             results = self.model(frame)
#             fire_detected = self.check_fire_detection(results)

#             if fire_detected:
#                 for result in results:
#                     coordinates = result.boxes.xyxy[0].numpy()
#                     x_min, y_min, x_max, y_max = map(int, coordinates)
#                     cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), color=(255, 0, 0))
#                 self.fire_frames[camera_ip] += 1
#             else:
#                 self.fire_frames[camera_ip] = 0

#             if self.fire_frames[camera_ip] >= 12:
#                 self.send_alarm_message(camera_ip)

#             cv2.imshow(f'Fire detection - Camera {camera_ip}', frame)

#             key = cv2.waitKey(1)
#             if key == 27:
#                 break

#         cap.release()
#         cv2.destroyAllWindows()

#     def run(self):
#         for camera_ip in self.camera_ips:
#             thread = threading.Thread(target=self.process_camera, args=(camera_ip,))
#             self.threads.append(thread)
#             thread.start()

#         for thread in self.threads:
#             thread.join()

# if __name__ == "__main__":
#     model_path = "/Users/huytuannguyen/Desktop/FPT/FAIC/FPTAI/FireDetectionYOLOv8/runs/detect/train/weights/best.pt"
#     camera_ips = [0, '/Users/huytuannguyen/Desktop/FPT/FAIC/FPTAI/FireDetectionYOLOv8/ultralytics/yolo/v8/detect/forestfire4.mp4']  # Replace with your camera IPs
#     fire_detection_system = FireDetectionSystem(model_path, camera_ips)
#     fire_detection_system.run()











from ultralytics import YOLO
import cv2
import threading

class FireDetectionSystem:
    def __init__(self, model_path, camera_ips):
        self.model = YOLO(model_path)
        self.camera_ips = camera_ips
        self.fire_frames = {camera_ip: 0 for camera_ip in camera_ips}
        self.threads = []

    def check_fire_detection(self, results):
        if len(results[0]) == 0:
            return False
        return True

    def send_alarm_message(self, camera_ip):
        print(f"Fire detected from camera {camera_ip}! Sending alarm message...")

    def process_camera(self, camera_ip):
        cap = cv2.VideoCapture(camera_ip)
        cv2.namedWindow(f'Fire detection - Camera {camera_ip}', cv2.WINDOW_NORMAL)
        cv2.resizeWindow(f'Fire detection - Camera {camera_ip}', 640, 480)

        while True:
            ret, frame = cap.read()
            if frame is None:
                # Handle the case where the frame is not available (e.g., camera disconnected)
                print(f"Camera {camera_ip} is not providing valid frames.")
            break
            if not ret:
                break

            results = self.model(frame)
            fire_detected = self.check_fire_detection(results)

            if fire_detected:
                for result in results:
                    coordinates = result.boxes.xyxy[0].numpy()
                    x_min, y_min, x_max, y_max = map(int, coordinates)
                    cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), color=(255, 0, 0))
                self.fire_frames[camera_ip] += 1
            else:
                self.fire_frames[camera_ip] = 0

            if self.fire_frames[camera_ip] >= 12:
                self.send_alarm_message(camera_ip)

            cv2.imshow(f'Fire detection - Camera {camera_ip}', frame)

            key = cv2.waitKey(1)
            if key == 27:
                break

        cap.release()
        cv2.destroyWindow(f'Fire detection - Camera {camera_ip}')

    def run(self):
        for camera_ip in self.camera_ips:
            thread = threading.Thread(target=self.process_camera, args=(camera_ip,))
            self.threads.append(thread)
            thread.start()

        for thread in self.threads:
            thread.join()

if __name__ == "__main__":
    model_path = "runs/detect/train/weights/best.pt"
    camera_ips = [0, 'ultralytics/yolo/v8/detect/forestfire4.mp4']  # Replace with your camera IPs
    fire_detection_system = FireDetectionSystem(model_path, camera_ips)
    fire_detection_system.run()
