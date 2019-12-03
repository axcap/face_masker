import os
import cv2
import dlib
import math
import argparse
import ffmpeg
import sys
import numpy as np
from tqdm import tqdm
from pathlib import Path, PosixPath


def load_image(image_path: PosixPath):
    return cv2.imread(str(image_path))


def find_faces(image, detector='hog', weights='/Users/axcap/Downloads/mmod_human_face_detector.dat'):
    if detector == 'hog':
        face_detector = dlib.get_frontal_face_detector()
    elif detector == 'cnn':
        face_detector = dlib.cnn_face_detection_model_v1(weights)
    else:
        raise NotImplementedError

    return face_detector(image, 0)


def hide_faces(image, faces, method='random'):
    def over_the_edge_correction(img, x, y, w, h):
        img_h, img_w, _ = img.shape
        if x < 0:
            x = 0
        if y < 0:
            y = 0
        if x + w > img_w:
            w = img_w - x
        if y + h > img_h:
            h = img_h - y

        return x, y, w, h

    # loop over detected faces
    for face in faces:
        try:
            x = face.left()
            y = face.top()
            w = face.right() - x
            h = face.bottom() - y
        except AttributeError:
            x = face.rect.left()
            y = face.rect.top()
            w = face.rect.right() - x
            h = face.rect.bottom() - y

        x, y, w, h = over_the_edge_correction(image, x, y, w, h)
        # draw box over face
        if method is 'pixelate':
            temp = cv2.resize(image[y:y+h, x:x+w], (w//15, h//15), interpolation=cv2.INTER_LINEAR)
            mask = cv2.resize(temp, (w, h), interpolation=cv2.INTER_NEAREST)
        elif method is 'random':
            mask = np.random.rand(h, w, 3)*255
        elif method is 'mask_out':
            mask = np.zeros((h, w, 3))

        image[y:y+h, x:x+w] = mask

    return image


def save_image(image, output_path, input_path):
    # save output image
    output_path = Path(output_path) / input_path.name
    cv2.imwrite(str(output_path), image)


def show_image(image):
    # display output image
    cv2.imshow("face detection with dlib", image)
    cv2.waitKey()

    # close all windows
    cv2.destroyAllWindows()


def pre_process_image(filename, output_dir, method='hog'):
    #print('pre_process_image: ', filename, output_dir, method)
    cvImg = load_image(filename)
    if cvImg is not None:
        faces = find_faces(cvImg, method)
        img = hide_faces(cvImg, faces)
        save_image(img, output_dir, filename)
        return 0
    return 1


def pre_process_folder(input: Path, output: Path, method='hog'):
    for image_path in sorted(input.glob('*.jpg')):
        pre_process_image(image_path, output, method)


def pre_process_video(input, output_dir, method='hog'):
    probe = ffmpeg.probe(input)
    video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
    width = int(video_stream['width'])
    height = int(video_stream['height'])

    out, _ = (
        ffmpeg
        .input(input)
        .output('pipe:', format='rawvideo', pix_fmt='rgb24')
        .run(capture_stdout=True)
    )
    video = np.frombuffer(out, np.uint8).reshape([-1, height, width, 3])
    for frame in video:
        return pre_process_image(frame, output_dir, method)


def get_frame_count(input):
    cap = cv2.VideoCapture(input)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    #length = math.ceil(length * (1 / 30))
    return length


def extract_frames(input, output, compression='jpg'):
    #ffmpeg -i video.webm -vf fps=1 thumb%04d.jpg -hide_banner

    p = Path(output)
    if not p.exists():
        os.makedirs(p, exist_ok=True)

    (
        ffmpeg
        .input(input)
        .output(str(p / ('frame%04d.'+compression)))
        #.global_args('-hide_banner', '-nostats', '-loglevel', 'panic')
        .run()
    )



if __name__ == '__main__':
    # handle command line arguments
    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--input', required=True, help='path to video file or folder with images')
    ap.add_argument('-o', '--output_dir', required=True, help='where to save processed images')
    ap.add_argument('-x', '--image_extention', default='*.jpg',
                    help='wildcard to select images in folder')
    ap.add_argument('-w', '--weights', default='./mmod_human_face_detector.dat',
                    help='path to weights file')
    args = ap.parse_args()

    '''
    p = Path(args.input_dir)
    length = len(list(p.glob(args.image_extention)))
    for image_path in tqdm(p.glob(args.image_extention), total=length):
        img = load_image(image_path)
        if img is not None:
            faces = find_faces(img, detector='cnn')
            img = hide_faces(img, faces)
            save_image(img, args.output_dir, image_path)
            # show_image(img)
    '''
    #extract_frames(args.input, args.output_dir)
    print(get_frame_count(args.input))
