## https://github.com/ultralytics/yolov5/blob/f11a8a62d27c2740af5df940973d231fd5fcb038/models/yolo.py
## Colab환경에서 구현함..

# 런타임 유형 확인
if torch.cuda.is_available():
  DEVICE = torch.device("cuda")
  print(DEVICE, torch.cuda.get_device_name(0))
else:
  DEVICE = torch.device("cpu")
  print(DEVICE)

# 필수 라이브러리 로딩
import torch
import torchvision
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms

import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image

# Model 불러오기
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# 구글 드라이브 연동
from google.colab import drive
drive.mount('/content/drive')

# test이미지 불러오기
im = cv2.imread("/content/drive/MyDrive/image/frame0.png")
im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB) # 색전환?

# Inference(모델에 적용)
results = model(im, size = 640)

results.pandas().xyxy[0]  # 결과 라벨정보 출력 
results.show() # 결과 이미지 출력

## 자동화 적용예시
# image 2개 일 때
for f in 'image.jpg', 'image1.jpg':
  torch.hub.download_url_to_file('파일경로/images/' +f,f)# 다운로드 이미지 파일 경로
image = Image.open('image.jpg)
image1 = cv2.imread('image1.jpg)[..., : : -1] 
# 모델 적용
result = model([image,image1], size = 640)
