import streamlit as st
import cv2
import numpy as np

def sketch(frame):
    """
    Generate an improved sketch filter for real-time edge detection.
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7, 7), 0)
    canny = cv2.Canny(blur, 50, 150)
    
    sketch_img = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 8
    )

    return sketch_img

# Streamlit UI
st.title("Real-Time Sketch Filter with Toggle Option")

# Toggle Button
apply_sketch_filter = st.button("Toggle Sketch Filter")

# OpenCV Video Capture
capture = cv2.VideoCapture(0)

# Display video stream with or without the sketch filter
frame_placeholder = st.empty()

while True:
    response, frame = capture.read()
    if not response:
        break
    
    if apply_sketch_filter:
        frame = sketch(frame)
    
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_placeholder.image(frame_rgb, channels="RGB")
    
    # Break condition
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
