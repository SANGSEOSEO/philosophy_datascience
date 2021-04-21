# OpenCV에서 RGB채널 엑세스

OpenCV에서 이미지는 내부적으로 numpy.ndarray배열 형태로 저장되어 지는데 각각의 RGB구성의 요소들인 채널에 접근방법에 대하여 다루고자 한다.

각 RGB채널에 접근하는 방법은 다양하지만, 대표적으로 두 가지를 여기서는 다룬다

* `cvs.split()`
* `cv2.merge()`

## RGB채널 접근방법 구현

1. 이미지 로드 
2. 이미지를 RGB채널로 분할
3. 분리할 각 채널를 화면에 표출
4. 원래의 이미지로 각 채널을 병합

이미지의 개별 RGB채널에 접근하고자 하는 이유는 ?

개별 RGB채널에 접근해봄으로써 각 채널이 전체 출력 이미지에 얼마나 기여하고있는지 시각화할 수 있습니다.

특히, 개별 채널에 접근해봄으로써, 임계치 혹은 이미지의 경계선 감지(Edge Detection)등을 적용해볼 때 유용하게 쓰일 수 있습니다.
