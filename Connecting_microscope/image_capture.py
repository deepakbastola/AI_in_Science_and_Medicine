import cv2

def main():
    # The argument to VideoCapture is the camera index. 
    cap = cv2.VideoCapture(0) 
    DF_counter = 0  # Initialize frame counter

    while True:
        # Capture frame-by-frame
        ret, DF = cap.read()

        if not ret:
            print("Failed to grab DF")
            break

        # Display the resulting frame
        cv2.imshow('Webcam Feed', DF)

        key = cv2.waitKey(1)

        # If 'c' is pressed on the keyboard, save the frame
        if key & 0xFF == ord('c'):
            cv2.imwrite(f'DF_{DF_counter}.png', DF)
            print(f'DF_{DF_counter}.png saved!')
            DF_counter += 1

        # If 'q' is pressed on the keyboard, break the loop and close the application
        elif key & 0xFF == ord('q'):
            break

    # After the loop release the capture
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
