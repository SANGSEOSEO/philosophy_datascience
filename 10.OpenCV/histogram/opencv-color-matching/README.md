# OpenCV, scikit-image, python을 이용한 히스토그램 일치

## 목표

OpenCV및 scikit-image를 사용하여 <span style="color:red">histogram matching</span>을 모두 수행하는 방법을 익히기

## 관련 사이트 

* [PyImageSearch](https://pyimagesearch.com)
* [히스토그램 매칭](https://en.wikipedia.org/wiki/Histogram_matching)

## 추가적인 패키지 설치

* `pip install scikit-image`

## 개요

히스토그램 이퀄라이제이션은 입력 이미지의 대비를 향상시키기 위해 하는 방법이다. 이번 시간은 입력 이미지와 참조용 이미지 두개가 있다고 가정하고 , 이 두개의 서로 대비와 색의 분포를 일치시킴으로 두 사진의 서로 합쳐진 사진을 만들어보려고 한다.

아래 이미지와 같이 두 개의 이미지가 있다.

1. 각 이미지에 대한 히스토그램 계산
2. 참조 이미지 히스토그램 가져 오기
3. 참조 히스토그램을 사용하여 입력 이미지의 픽셀 강도 값을 업데이트하여 일치하도록합니다.![](https://www.pyimagesearch.com/wp-content/uploads/2021/01/opencv_histogram_matching_header.png)

위의 3번째 이미지가 히스토그램 일치 방법을 적용시킨 후의 이미지입니다.

히스토그램 일치 방법은 이미지 처리 파이프 라인을 서로 다른 조건- 다른 명암 - 하에 촬영된 동일한 장소의 이미지를  "정규화된 이미지" 로 처리하는데 사용하는 유용한 이미지 처리 기술입니다.



## 히스토그램 매칭



![](https://www.pyimagesearch.com/wp-content/uploads/2021/01/opencv_histogram_matching_cdf.png)

빨간색 라인과 파란색을 서로 다른 환경 조건에서 찍은 동일한 이미지라고 가정한다면 이 둘의 이미지의 대비 및 색상의 분포를 나타낸 것을 히스토그램 매칭을 통해서 종국에는 우측 상단과 같이 입력 이미지의 히스토그램 분포가 참조이미지의 히스토그램 분포와 일치하도록 업데이트를 하는 것을 의미함.

입력 이미지의 실제 내용은 변경되지 않지만 *픽셀 분포* 는 변경 되므로 참조 이미지의 분포에 따라 입력 이미지의 조도와 대비를 조정합니다.

또한 히스토그램 일치를 기본 색상 보정 / 색상 불변성의 형태로 사용할 수 있으므로 복잡하고 계산 비용이 많이 드는 기계 학습 및 딥 러닝 알고리즘 을 활용 *하지 않고도*  더 좋고 안정적인 이미지 처리 파이프 라인을 구축 할 수 있습니다. 

히스토그램 일치 작업은 정말 고된 작업일수 있지만 다행히도, 사이킷런에 [훌륭한 문서](https://scikit-image.org/docs/dev/api/skimage.exposure.html#skimage.exposure.match_histograms)를 제공하고 있으며 `match_histograms`함수를 제공하고 있다.

## 인용

[NewYork YIMBY](https://newyorkyimby.com/2020/09/empire-state-building-restoration-nearly-complete.html)

[World Federation Great Tower](https://www.great-towers.com/tower/empire-state-building)

[scikit-image 의 공식 예제](https://scikit-image.org/docs/dev/auto_examples/color_exposure/plot_histogram_matching.html)