# Object Detection Using Yolov5s & Detectron2🚘🚖
> DeepLearning 프로젝트, 차량객체 탐지를 위해 yolo v5s와 detectron2모델을 사용함  
> 라벨링을위해 labelme 툴을 활용하였고, yolo모델을 위해 roboflow를 활용함  
> 기간 : 22.12.12. ~ 22.12.23.
<br>

## 프로젝트 소개
**1. 프로젝트 주제** : 도로 이동량 급중률을 파악(이상치)하여 사전에 사고를 예방하는 차량객체 탐지 모델링  
**<활용방안>**  
① 위험 상황을 사전 방지하는 시스템 구축  
② 차량뿐만 아니라 사고 위험성이 높은곳의 지역별 이상치를 설정하여 사고예방에 도움될 것  

#### 2. 작업 내용
- 데이터 탐색 및 수집
- 데이터 변환
- AI모델 탐색 및 설정
- 학습 및 평가

#### 3.. 모델 선정 이유
- 다소 최신의 모델이며 이미 훈련된 모델도 존재하여 초기 접근이 쉬움
- 정확도는 조금 낮더라도 처리속도가 빠름
- 속도가 빠르기에 상용화되기 좋을것이라 판단
<br>

## 개발도구 및 언어
<img src="http://img.shields.io/badge/coLab-F9AB00?style=round&logo=googlecolab&logoColor=white" /> <img src="http://img.shields.io/badge/Python-3776AB?style=round&logo=Python&logoColor=white" /> <img src="http://img.shields.io/badge/PyTorch-EE4C2C?style=round&logo=PyTorch&logoColor=white" /> 
<br>
<br>

## 수행 내용  
#### 1. 데이터 수집  
- 국가교통정보센터의 오픈데이터 도로 영상
- open API를 통한 전국 CCTV 공공데이터 파일 확보  

#### 2. 데이터 전처리
- labelme를 사용
- 폴리곤타입, car, truck, bus로 구분
※ yolo에 적용하기위해 위에서 생성된 파일을 roboflow에 적용시켜 데이터화 시킴

#### 3. 결과
### ① YOLOv5s
<div align=center>

![image](https://user-images.githubusercontent.com/114147352/233818277-85b5f1a3-d6e5-42c0-9efa-5c752a0d1d69.png)

</div>

### ② Detectron2  
<div align=center>

![image](https://user-images.githubusercontent.com/114147352/233818302-e67ab40e-0bc1-4764-ad05-7705be211207.png) 

</div>

<div align=right>(추후 설명 추가)</div>

#### 4. 개선방안
![image](https://user-images.githubusercontent.com/114147352/233818225-88044aae-9b06-4579-ae25-8cc70fe46f32.png)
