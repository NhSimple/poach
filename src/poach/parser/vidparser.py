import cv2
import os
import numpy as np
from random import randint


class parsemethods:
    def __init__(self, video_file, write_path):
        self.video_file = video_file
        self.write_path = write_path
        self.filename = os.path.basename(self.video_file)
        self.filename, self.file_extension = os.path.splitext(self.filename)

        def create_folder():
            accepted = True
            backup_attempt = 0
            complete = False
            while not complete:
                try:
                    if accepted:
                        attempted_write_path = self.write_path + "/" + self.filename
                        os.mkdir(attempted_write_path)
                        self.write_path = attempted_write_path

                        complete = True
                    else:
                        attempted_write_path = (
                            self.write_path + self.filename + str(backup_attempt) + "/"
                        )
                        os.mkdir(attempted_write_path)

                        self.write_path = attempted_write_path

                        complete = True
                except Exception as e:
                    print(e)
                    print("will attempt to create new folder.")
                    accepted = False
                    backup_attempt += 1

        create_folder()

    def brightest_frame(self):
        # Open the video file
        video = cv2.VideoCapture(self.video_file)

        # Check if video opened successfully
        if not video.isOpened():
            print("Error opening video file")
            return Exception("video unable to load")

        # Initialize variables to track the brightest frame
        max_brightness = 0
        max_frame = None
        frames = 0

        # Calculate the brightness of the current frame

        # Read video frames until the end
        while True:
            # Read the current frame
            ret, frame = video.read()

            # Break the loop if no more frames are available
            if not ret:
                break

            brightness = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY).mean()

            if brightness > max_brightness:
                max_brightness = brightness
                max_frame = frame

        image_to_write = cv2.cvtColor(max_frame, cv2.COLOR_RGB2BGR)

        cv2.imwrite(f"{self.write_path}/brightest.jpg", max_frame)

    def loudest_frame(self):
        # Open the video file
        video = cv2.VideoCapture(self.video_file)

        # Variables to store the loudest frame
        loudest_frame = None
        loudest_frame_amplitude = 0

        # Read frames until the video ends
        while video.isOpened():
            ret, frame = video.read()

            # If there are no more frames, break the loop
            if not ret:
                break

            # Extract the audio from the current frame based on the channel layout
            audio = frame[:, :, 0]

            # Calculate the maximum amplitude of the audio
            amplitude = np.abs(audio).max()

            # Update the loudest frame if necessary
            if amplitude > loudest_frame_amplitude:
                loudest_frame = frame
                loudest_frame_amplitude = amplitude

        cv2.imwrite(f"{self.write_path}/loudest.jpg", loudest_frame)

    def first_ten_seconds(self):
        video = cv2.VideoCapture(self.video_file)
        fps = video.get(cv2.CAP_PROP_FPS)
        ten_seconds_frame = int(fps * 10)
        video.set(cv2.CAP_PROP_POS_FRAMES, ten_seconds_frame)
        ret, frame = video.read()  # Read the frame at the desired position

        cv2.imwrite(f"{self.write_path}/ten_seconds.jpg", frame)

    def before_half(self):
        video = cv2.VideoCapture(self.video_file)
        total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        halfway_frame = total_frames // 2
        framepoint = randint(1, halfway_frame)

        # Set the current frame position to less than halfway
        video.set(cv2.CAP_PROP_POS_FRAMES, framepoint)
        success, frame = video.read()

        cv2.imwrite(f"{self.write_path}/before_half.jpg", frame)

    def after_half(self):
        video = cv2.VideoCapture(self.video_file)
        total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

        framepoint = randint(total_frames // 2, total_frames)
        video.set(cv2.CAP_PROP_POS_FRAMES, framepoint)

        success, frame = video.read()

        cv2.imwrite(f"{self.write_path}/after_half.jpg", frame)
