from collections import defaultdict

import cv2
import numpy as np

from ultralytics import YOLO

# Load the YOLOv8 model
# model = YOLO('yolov8n.pt')
model = YOLO('/usr/src/ultralytics/runs/detect/train/weights/last.pt')

# Open the video file
video_path = "/usr/src/datasets/vid/MVI_1569.MP4"
cap = cv2.VideoCapture(video_path)

# Store the track history
track_history = defaultdict(lambda: [])

i = 0

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 tracking on the frame, persisting tracks between frames
        results = model.track(frame, persist=True)

        # Get the boxes and track IDs
        if results[0].boxes.id is not None:
            boxes = results[0].boxes.xywh.cpu()
            track_ids = results[0].boxes.id.int().cpu().tolist()
        elif results[0].boxes.xywh.cpu().tolist() is not None:
            boxes = results[0].boxes.xywh.cpu()
            track_ids = [0]
        else:
            boxes = []
            track_ids = []

        # Visualize the results on the frame
        results_temp = results[0]
        results_temp.boxes = None
        results_temp.names = None
        annotated_frame = results_temp.plot()

        # Plot the tracks
        for box, track_id in zip(boxes, track_ids):
            x, y, w, h = box
            track = track_history[track_id]
            
            if i % 5 == 0:
                track.append((float(x), float(y)))  # x, y center point
                
                # if len(track) > 90:  # retain 90 tracks for 90 frames
                #     track.pop(0)

                # Draw the tracking lines
                points = np.hstack(track).astype(np.int32).reshape((-1, 1, 2))
            
            i = i + 1
            
            cv2.polylines(annotated_frame, [points], isClosed=False, color=(32., 177.664, 237.824), thickness=10)
            # cv2.polylines(annotated_frame, [points], isClosed=False, color=(142.336, 47.104, 126.464), thickness=10)

        # Display the annotated frame
        cv2.imshow("YOLOv8 Tracking", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()