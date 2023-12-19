import re
import cv2
import numpy as np
import pytesseract

from ktm_model import KTMModel


def ocr_raw(image):
    # image = cv2.resize(image, (50 * 16, 500))

    # img_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    # img_gray = cv2.equalizeHist(img_gray)
    # img_gray = cv2.fastNlMeansDenoising(img_gray, None, 3, 7, 21)
    # cv2.fillPoly(img_gray, pts=[np.asarray([(540, 150), (540, 499), (798, 499), (798, 150)])], color=(255, 255, 255))
    # th, threshed = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TRUNC)
    result_raw = pytesseract.image_to_string(image, lang="ind")

    return result_raw


def main(image):
    result_raw = ocr_raw(cv2.imread('image.jpg'))
    nim = ''
    nama = ''
    ttl = ''
    jurusan = ''
    alamat = ''

    lines = result_raw.split('\n')

    # for i in lines:
    #     print(i)

    # remove empty lines
    lines = list(filter(lambda x: x != '', lines))

    # Find NIM and its index
    nim_index = next((i for i, line in enumerate(lines) if re.match(r'^\d+$', line)), None)
    if nim_index is not None:
        nim = lines[nim_index]

        # Extract other information based on the index of NIM
        if nim_index + 1 < len(lines):
            nama = lines[nim_index + 1]

        if nim_index + 2 < len(lines):
            ttl = lines[nim_index + 2]

        if nim_index + 3 < len(lines):
            jurusan = lines[nim_index + 3]

        if nim_index + 4 < len(lines):
            alamat = ' '.join(lines[nim_index + 4:])

    # print('nim: ' + nim)
    # print('nama: ' + nama)
    # print('ttl: ' + ttl)
    # print('jurusan: ' + jurusan)
    # print('alamat: ' + alamat)

    return KTMModel(nim, nama, ttl, jurusan, alamat)


if __name__ == '__main__':
    main(sys.argv[1])
