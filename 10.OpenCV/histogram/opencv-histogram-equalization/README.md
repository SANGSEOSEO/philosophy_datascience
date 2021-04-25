# 히스토그램 및 적응형 히스토그램 이퀄라이제이션

## 목표

OpenCV를 사용하여 <span style="color:red">히스토그램 이퀄라이제이션과 적응형 히스토그램 이퀄라이제이션</span>을 모두 수행하는 방법을 익히기

## 관련 사이트 

* [PyImageSearch](https://pyimagesearch.com)

## 개요

Histogram Equalization은 이미지 히스토그램의 픽셀 분포를 업데이트하여 이미지의 전체 대비를 조정하는 기본 이미지 처리 기술.이런 방법을 통해 대비가 낮은 영역이 출력 이미지에서 더 높은 대비를 얻을 수 있다.

히스토그램 이퀄라이제이션 적용은 입력 그레이 스케일 / 단일 채널 이미지에서 픽셀 강도의 히스토그램을 계산하는 것으로 시작한다.

![img](https://www.pyimagesearch.com/wp-content/uploads/2021/01/opencv_histogram_equalization_grayscale_histogram.png)

​                         [입력 그레이 스케일 이미지]                                             [해당 이미지의 히스토그램 계산]

히스토그램에 얼마나 많은 피크가 있는지 확인하여 해당 버킷에 비닝된 픽셀 수가 많음을 나타냅니다. 

<span style="color:red">히스토그램 이퀄라이제이션은 이런 픽셀을 상대적으로 픽셀이 덜  비닝된 버킷에 분산</span> 시키는 것입니다.

![img](https://www.pyimagesearch.com/wp-content/uploads/2021/01/opencv_histogram_equalization_histogram-e1610163352539.png)

수학적으로 이것이 의미하는 바는 위 이미지와 같이 누적 분포 함수(CDF)에 선형 추세를 적용하려고 한다는 것입니다.

![img](https://www.pyimagesearch.com/wp-content/uploads/2021/01/opencv_histogram_equalization_beach_input_vs_equalized-e1610163488329.png)

​                [히스토그램 이퀄라이제이션을 적용전 이미지]     [적용 후 이미지]

입력 이미지의 대비가 크게 향상되었지만, 이와 더불어 노이즈도 향상되었음을 알수있다.

여기서 문제를 제기한다면 " 동시에 노이즈가 증가되지 않고 이미지 대비를 향상 시키는 방법은?"

<span style="color:red">적응형 히스토그램 이퀄라이제이션</span>을 적용해 보는 방법이 있다.

## 히스토그램 이쿼라이제이션의 작동

* 이미지 픽셀강도의 히스토그램 계산
* 가장 빈번한 픽셀 값(예: 히스토그램에서 가장 빈도수가 높은 값)을 균등하게 분산 및 배포
* 누적 분포함수(Cumulative Distribution Function)에 선형추세(linear trend) 제공

CLAHE(Contrast Limited Adaptive Histogram Equalization)이라는 알고리즘을 적용하여 히스토그램 이퀄라이제이션을 더욱 개선하여 더 높은 품질의 출력 이미지를 얻을 수 있습니다.

히스토그램 이퀄라이제이션은 의료 분야 및 노출부족 혹은 과다 이미지를 보정하는 사진작업에서도 사용이되며,

의료분야의 경우는 방사전 사진의 대비를 개선하기 위해 X-레이 스캔 및 CT스캔에 적용된 히스토그램 등화를 볼 수 있습니다.(의사로 하여금 환자의 CT이미지 및 X레이  스캔 이미지) 징후를 더 잘 진단 가능)

## 적응형 히스토그램 이퀄라이제이션

입력 이미지를 M * N 그리드로 나누고, 그리드의 각 셀에 이퀄라이제이션을 적용하여 더 높은 품질의 출력 이미지를 얻습니다.

![img](https://www.pyimagesearch.com/wp-content/uploads/2021/01/opencv_histogram_equalization_beach_equalized_vs_clahe.png)



## 학습 이후 그대의 상태는?

이 학습 이후엔 기본 히스토그램 이퀄라이제이션과 적응형 히스토그램 이퀄라이제이션를 OpenCV로 이미지에 성공적으로 적응 가능해진다.

## 기본 히스토그램 이퀄라이제이션과 적응형 히스토그램 이퀄라이제이션

* `cv2.equalizeHist`
* `cv2.createCLAHE`