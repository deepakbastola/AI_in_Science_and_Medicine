import cv2
import os

def main():
    # The argument to VideoCapture is the camera index.
    cap = cv2.VideoCapture(0)

    # Define the directory to save frames
    desktop = os.path.expanduser("~/Desktop")  # adjust as needed
    directory = os.path.join(desktop, "DF")

    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Find the highest numbered existing frame
    frames = [f for f in os.listdir(directory) if f.startswith("frame_") and f.endswith(".png")]
    if frames:
        highest_frame = max(frames, key=lambda f: int(f.split('_')[1].split('.')[0]))
        frame_counter = int(highest_frame.split('_')[1].split('.')[0]) + 1
    else:
        frame_counter = 0

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
            frame_path = os.path.join(directory, f'frame_{frame_counter}.png')
            cv2.imwrite(frame_path, frame)
            print(f'{frame_path} saved!')
            frame_counter += 1

        # If 'q' is pressed on the keyboard, break the loop and close the application
        elif key & 0xFF == ord('q'):
            break

    # After the loop release the capture
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
