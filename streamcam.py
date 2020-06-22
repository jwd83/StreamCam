import cv2


def main():
    cap = cv2.VideoCapture(0)

    while True:
        # get frame
        success, frame = cap.read()

        # generate mask
        mask = get_mask(frame)

        # apply mask
        masked_frame = apply_mask(frame, mask)

        # show result
        cv2.imshow("StreamCam", masked_frame)

        # wait for next frame
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def get_mask(frame):
    pass

def apply_mask(image, mask):
    return image

if __name__ == "__main__":
    main()

