# OpenCV Bitwise Operation



## 학습목표

- OpenCV에서 AND, OR, XOR 및 NOT을 적용하는 방법

이 튜토리얼에서는 OpenCV에서 비트 AND, OR, XOR 및 NOT을 적용하는 방법을 배웁니다.

Cropping에서는 이미지에서 관심 영역 (ROI)을 자르고 추출하는 방법을 배웠습니다.

특정 예에서 ROI는 *직사각형* 이어야했습니다 . . . 하지만 *직사각형* 이 *아닌* 영역 을 자르려면 어떻게해야 합니까?

How?

대답은 비트 연산과 마스킹을 모두 적용하는 것 .

이미지 마스킹은 [ OpenCV를 사용한 이미지 마스킹](https://www.pyimagesearch.com/2021/01/19/image-masking-with-opencv/] )가이드에서이를 수행하는 방법에 대해 설명합니다 .



## **AND, OR, XOR 및 NOT**

이 튜토리얼에 너무 깊이 들어가기 전에 네 가지 기본 비트 연산자를 이해하고 있다고 가정하겠습니다.

1. AND
2. OR
3. XOR (Exclusive OR)
4. NOT

이전에 비트 연산자로 작업 한 적이 없다면 [Real Python 상세 가이드](https://realpython.com/python-bitwise-operators/) .

