# resources
#
# https://elder.dev/posts/open-source-virtual-background/
# https://github.com/fangfufu/Linux-Fake-Background-Webcam/blob/master/bodypix/app.js

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
    # the following method in bodypix are needed
    # decodeImage
    # segmentPerson

    pass

def apply_mask(image, mask):
    return image

if __name__ == "__main__":
    main()

