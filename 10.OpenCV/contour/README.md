# Component Labeling and Analysis

## 연구방향

* OpenCV를 사용하여 연결된 컴포넌트 라벨링 분석수행 방법
* `cv2.connectedComponentsWithStats`
* `Contour`
  - Contours란 동일한 색 또는 동일한 강도를 가지고 있는 영역의 경계선을 연결한 선입니다. 우리가 자주 보는 것으로는 등고선이나 일기예보에서 볼 수 있습니다.
  - 대상의 유형을 정확하게 파악하는데 도움이 된다.(자동차 번호판의 경우 아래 모양을 보면)
  - 이러한 이유로 contour를 찾는것은 검은색 배경에 하얀색대상을 찾는것과 비슷하며 그래서 대상은 흰색, 배경은 검은색으로 해야 합니다.

## 연결구성요소 라벨링 개요

![](https://www.pyimagesearch.com/wp-content/uploads/2021/02/opencv_connected_components_header.png)

연결된 구성 요소 레이블링(연결된 구성요소 분석, blob - 얼굴 - 추출, 영역 레이블링) 은 이진 이미지에서 "blob"유사 영역의 연결성을 결정하는 데 사용되는 [그래프 이론](https://en.wikipedia.org/wiki/Graph_theory) 의 알고리즘 적용입니다.

윤곽 분석은, 자동차 번호판과 같이 하나의 윤곽이 또 다른 윤곽에 포함되는 것과 같은 계층 구조를 갖는 구성요소를 분석하는데 사용됩니다.

연결된 구성 요소 분석의 좋은 예는 이진 (즉, 임계 값) 번호판 이미지의 연결된 구성 요소를 계산하고 속성 

(예 : 너비, 높이, 면적, 견고성 등)을 기반으로 블롭을 필터링하는 것입니다. 

## **OpenCV 연결 구성 요소 라벨링 및 분석**

이 튜토리얼의 첫 번째 부분에서는 OpenCV가 연결된 구성 요소 분석을 수행하기 위해 제공 하는 네 가지 (예, *네 가지* ) 함수를 검토합니다 . 

#### 구현방법

* OpenCV를 사용하여 연결된 컴포넌트 구성요소 분석 방법을 예시로 보여주고, 각 컴포넌트의 통계치를 계산하고,개개의 컴포넌트를 추출 및 시각화 구현
* 실 세계 구현 사례로 , 자동차 번호판을 통해 연결컴포넌트 분석을 통해 번호판 문자를 추출하는 방법 구현

### **OpenCV의 연결된 구성 요소 기능**

OpenCV는 4 개의 연결된 구성 요소 분석 기능을 제공합니다.

1. cv2.connectedComponents

   - 아래 2번과 같이 콤포넌트에 대한 통계정보를 제외하고는 동일한 정보를 리턴

2. cv2.connectedComponentsWithStats

   - The bounding box of the connected component

   - The area (in pixels) of the component

   - The centroid/center *(x, y)*-coordinates of the component

3. cv2.connectedComponentsWithAlgorithm

   - 연결된 컴포넌트 분석을 위해 더 성능이 좋은 알고리즘을 제공

4. cv2.connectedComponentsWithStatsWithAlgorithm

   - 병렬처리가 지원되는 머신환경이라면 3번), 4번) 의 경우가 앞이 두 경우보다 속도면에서 우월하다.