## 코랩 환경(기본 제공 GPU)
# roboflow에서 데이터셋 분리한 코드 붙여넣기
!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="s7YmJeUA9IgceS1oxPfd")
project = rf.workspace("project-ij6y9").project("moving-detection")
dataset = project.version(1).download("yolov5")

# 이미지 출력 라이브러리?
from IPython.display import Image

# 구글 드라이브 연동
from google.colab import drive
drive.mount('/content/drive')

# YOLOv5 모델 설치 및 기본 설정
!git clone https://github.com/ultralytics/yolov5  # clone
%cd yolov5
%pip install -qr requirements.txt  # install

import torch
import utils
display = utils.notebook_init()  # checks

# 모델 훈련(파라미터 조정 가능, yaml파일에 데이터 경로 수정해준후 드라이브 경로 맞춰주기)
!python train.py --img 640 --batch 20 --epochs 15 --data data.yaml --weights yolov5s.pt --cache

# 모델 적용
!python detect.py --weights 가중치_경로/best.pt --img 640 --conf 0.35 --source 이미지.jpg

# detect로 생성된 파일 확인
Image('/detect이미지.jpg')

# 영상도 같은 방식으로 적용
!python detect.py --weights /가중치_경로/best.pt --img 640 --conf 0.35 --source 영상.mp4
