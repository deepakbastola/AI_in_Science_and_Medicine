import cv2
import torch

def main():
    # The argument to VideoCapture is the camera index.
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Failed to grab frame")
            break

        # Convert the frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Convert the numpy array to a PyTorch tensor
        tensor_frame = torch.from_numpy(gray_frame).float()

        # Add two extra dimensions to the tensor for batch size and channels
        tensor_frame = tensor_frame.unsqueeze(0).unsqueeze(0)

        # Create a random kernel
        kernel = torch.randn((1, 1, 3, 3))

        # Apply the convolution
        convolved_tensor = torch.nn.functional.conv2d(tensor_frame, kernel)

        # Remove the extra dimensions and convert back to a numpy array
        convolved_frame = convolved_tensor.squeeze(0).squeeze(0).numpy()

        # Normalize the convolved frame for display
        convolved_frame = cv2.normalize(convolved_frame, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

        # Display the resulting frame
        cv2.imshow('Webcam Feed', convolved_frame)

        # If 'q' is pressed on the keyboard, break the loop and close the application
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the capture
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
