import cv2
import os
from datetime import datetime

def main():
    # The argument to VideoCapture is the camera index.
    cap = cv2.VideoCapture(0)

    # Define the directory to save frames
    desktop = os.path.expanduser("~/Desktop")  # adjust as needed
    directory = os.path.join(desktop, "Noble")

    # Create the directory if it doesn't exist
    os.makedirs(directory, exist_ok=True)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Failed to grab frame")
            break

        # Display the resulting frame
        cv2.imshow('Webcam Feed', frame)

        key = cv2.waitKey(1)

        # If 'c' is pressed on the keyboard, save the frame
        if key & 0xFF == ord('c'):
            # Get the current date and time
            now = datetime.now()

            # Convert the date and time to a string in the format YYYYMMDD_HHMMSS
            now_str = now.strftime("%Y%m%d_%H%M%S")

            # Create the frame file name
            frame_file = f'frame_{now_str}.png'

            # Create the full path for the frame file
            frame_path = os.path.join(directory, frame_file)

            # Save the frame
            cv2.imwrite(frame_path, frame)
            print(f'{frame_path} saved!')

        # If 'q' is pressed on the keyboard, break the loop and close the application
        elif key & 0xFF == ord('q'):
            break

    # After the loop release the capture
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
