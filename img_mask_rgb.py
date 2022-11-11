import cv2
import numpy as np

print('Please enter the file path: ')
img_file_path=input()

### 이미지를 초록색 제외 검은색으로 배경분리하는 함수
def green_img_mask(file_path):
    image_bgr = cv2.imread(file_path) # 이미지 읽기

    image_hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV) # BGR에서 HSV로 변환

    lower_green = np.array([25,40,40]) # HSV에서 색의 값 범위 정의 

    upper_green = np.array([85,255,255]) # hue(색상), saturation(채도), value(명도)

    mask = cv2.inRange(image_hsv, lower_green, upper_green) # 마스크를 만듬 

    image_bgr_masked = cv2.bitwise_and(image_bgr, image_bgr, mask=mask) # 이미지에 마스크를 적용

    return image_bgr_masked

### 이미지 픽셀의 평균 색상값 hex로 도출, 면적계산
def img_average_color_and_area(img):

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # rgb변환

    img_size = img_rgb.shape[0]*img_rgb.shape[1] # 이미지 사이즈저장

    img_1D = img_rgb.reshape(img_size,3) # 이미지를 1D로 변환

    black_li = []
    for i in range(img_size): # 검은색 픽셀 위치 리스트에 저장
        if str(img_1D[i]) == '[0 0 0]':
            black_li.append(i)

    img_none_black = np.delete(img_1D, black_li, axis=0) #img에서 검은색 픽셀 제거
    color_mean = img_none_black.mean(axis=0) # 평균 색상값 계산 

    r,g,b = color_mean.astype(int) # rgb값 int변환

    hex = ('{:X}{:X}{:X}').format(r, g, b) # hex변환

    return hex, len(img_none_black) #hex값, black픽셀을 제외한 픽셀개수



img = green_img_mask(img_file_path)
print(img_average_color_and_area(img))