# 구글 코랩 기본 GPU환경에서 수행

# detectron2설치 및 기본세팅
!python -m pip install pyyaml==6.0 
import sys, os, distutils.core
!git clone 'https://github.com/facebookresearch/detectron2'
dist = distutils.core.run_setup("./detectron2/setup.py")
!python -m pip install {' '.join([f"'{x}'" for x in dist.install_requires])} 
sys.path.insert(0, os.path.abspath('./detectron2')) 

# 모듈 로딩 및 버전 확인
import torch, detectron2 
!nvcc --version
TORCH_VERSION = ".".join(torch.__version__.split(".")[:2]) 
CUDA_VERSION = torch.__version__.split("+")[-1]
print("torch: ", TORCH_VERSION, "; cuda: ", CUDA_VERSION)
print("detectron2:", detectron2.__version__)

# 필수 라이브러리 로딩
import detectron2
from detectron2.utils.logger import setup_logger
setup_logger()

import numpy as np
import os, json, cv2, random
from google.golab.patches import cv2_imshow

from detectron2 import model_zoo
from detectron2.engine import DefaultTrainer, DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog, DatasetCatalog

# 구글 드라이브 연동
from google.colab import drive
drive.mount('/content/drive')

# 데이터 로딩시 필요 
from detectron2.data.datasets import register_coco_instances

from os import path
if __name__ == '__main__'
 # 라벨링 파일 등록
 train_json_file_path = '/파일경로/train.json'
 test_json_file_path = '/파일경로/test.json'
 
 # 이미지 데이터셋 위치 등록
 train_dataset_dir = '/파일경로/'
 test_dataset_dir = '/파일경로/'

 # 데이터 로딩 
 register_coco_instances('train_dataset', {}, train_json_file_path, train_dataset_dir)
 register_coco_instances('test_dataset', {}, test_json_file_path, test_dataset_dir)
 
 # config파일 로딩
 cfg = get_cfg()
 # 사용 모델config파일과 병합
 cfg.merge_from_file(model_zoo.get_config_file('사용 모델 config파일.yaml') # mask_rcnn_R_50_FPN_3x사용

 # 훈련에 사용할 셋 지정
 cfg.DATASETS.TRAIN = ("train_dataset",)
 cfg.DATASETS.TEST =("test_dataset",)
 
 # 모델 가중치 등록
 cfg.MODEL.WEIGHTS = '가중치 파일'
##사용 가중치 : detectron2://COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x/137849600/model_final_f10217.pkl
 cfg.SOLVER.IMS_PER_BATCH = 2
 cfg.SOLVER.BASE_LR = 0.00025
 cfg.SOLVER.MAX_ITER = 300
 cfg.SOLVER.STEPS = []

 # 모델 훈련
 trainer = DefaultTrainer(cfg)
 trainer.resume_or_load(resume=False)
 trainer.train()
