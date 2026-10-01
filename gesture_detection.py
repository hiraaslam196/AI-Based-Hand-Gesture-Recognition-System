import cv2
import mediapipe as mp

# MediaPipe setup
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = HandLandmarkerOptions(
    base_options=BaseOptions(
        model_asset_path="hand_landmarker.task"
    ),
    running_mode=VisionRunningMode.IMAGE,
    num_hands=1
)

# Check which fingers are open
def get_gesture(hand_landmarks):

    # Landmark positions
    thumb_tip = hand_landmarks[4]
    thumb_ip = hand_landmarks[3]

    index_tip = hand_landmarks[8]
    index_pip = hand_landmarks[6]

    middle_tip = hand_landmarks[12]
    middle_pip = hand_landmarks[10]

    ring_tip = hand_landmarks[16]
    ring_pip = hand_landmarks[14]

    pinky_tip = hand_landmarks[20]
    pinky_pip = hand_landmarks[18]

    # Finger states
    index_open = index_tip.y < index_pip.y
    middle_open = middle_tip.y < middle_pip.y
    ring_open = ring_tip.y < ring_pip.y
    pinky_open = pinky_tip.y < pinky_pip.y

    # Thumb
    thumb_open = thumb_tip.x < thumb_ip.x

    # Gesture recognition

    if index_open and middle_open and ring_open and pinky_open:
        return "OPEN PALM"

    elif index_open and middle_open and not ring_open and not pinky_open:
        return "PEACE"

    elif index_open and not middle_open and not ring_open and not pinky_open:
        return "ONE"

    elif not index_open and not middle_open and not ring_open and not pinky_open:
        return "FIST"

    elif thumb_open and not index_open and not middle_open and not ring_open and not pinky_open:
        return "THUMBS UP"

    else:
        return "UNKNOWN"


# Open webcam
cap = cv2.VideoCapture(0)

print("Starting camera...")
print("Press Q to exit.")

with HandLandmarker.create_from_options(options) as landmarker:

    while True:

        success, frame = cap.read()

        if not success:
            print("Could not access camera.")
            break

        # Convert BGR to RGB
        rgb_frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        # Convert to MediaPipe image
        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb_frame
        )

        # Detect hand
        result = landmarker.detect(mp_image)

        # If hand detected
        if result.hand_landmarks:

            for hand_landmarks in result.hand_landmarks:

                # Draw landmarks
                for landmark in hand_landmarks:

                    x = int(landmark.x * frame.shape[1])
                    y = int(landmark.y * frame.shape[0])

                    cv2.circle(
                        frame,
                        (x, y),
                        5,
                        (0, 255, 0),
                        -1
                    )

                # Get gesture
                gesture = get_gesture(hand_landmarks)

                # Display gesture
                cv2.putText(
                    frame,
                    gesture,
                    (30, 60),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.5,
                    (0, 255, 0),
                    3
                )

        # Show camera
        cv2.imshow(
            "AI Hand Gesture Recognition",
            frame
        )

        # Exit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()