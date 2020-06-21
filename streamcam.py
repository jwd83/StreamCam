import cv2


def main():
    cap = cv2.VideoCapture(0)

    while True:
        # get frame
        success, img = cap.read()

        # generate mask
        mask = get_mask(img)

        # apply mask
        masked_img = apply_mask(img, mask)

        # show result
        # cv2.imshow("StreamCam", masked_img)
        cv2.imshow("StreamCam", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def get_mask(frame):
    pass

def apply_mask(image, mask):
    pass

if __name__ == "__main__":
    main()

