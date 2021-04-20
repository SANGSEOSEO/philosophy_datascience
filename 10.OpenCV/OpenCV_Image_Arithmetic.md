# OpenCV를 이용한 이미지 연산

OpenCV에서 이미지 연산하는 두가지 방법을 통해 이미지 연산이 무엇인지 알아보고자 한다.

- `cv2.add()`와 `cv2.substract()`
- 넘파이의 기본적인 더하기(addtion)와 빼기(substract)연산 

## 이미지 연산의 정의

학부때 배웠던 선형대수의 예를 들어보자.

아래와 같이 두 개의 행렬을 더하며 결과는?

![](https://www.pyimagesearch.com/wp-content/latex/6b5/6b58dade8ad980790b4dc671d28c02b0-ffffff-000000-0.png)

결과는 아래와 같이 행렬의 각 원소의 동일한 인덱스끼리 연산한다.

![](https://www.pyimagesearch.com/wp-content/latex/a5e/a5e4f6cccbd5138e71feac20addebbe7-ffffff-000000-0.png)

이미지로 작업할때는 <span style="color:red">색공간</span>과 <span style="color:red">데이터 유형</span>의 수치적 한계가 있다는 것을 알아야 한다. 

즉, RGB이미지는 픽셀값의 범위가 [0, 255]범위에 속해야 하며 250픽셀에 `10`을 더하게 되면 어떻게 될까?

일반적인 연산은 `260`이 되지만, 이미지 연산은 유효범위를 벗어나게 되므로 유효한 값이 아니므로,이미지 연산에서는 유효한 범위를 벗어나지 않기 위해서 검사를 수행하여 주어진 수치적 범위를 벗어나지 않기위한 작업을 수행합니다.(clipping이라고 하자)

그럼 어떤 방법이 이 경우엔 적용해야 하는가?

**대답은 "올바른 방법"이 없다는** 것입니다. 픽셀을 조작하는 방법과 원하는 결과가 무엇인지에 따라 달라집니다.

**그러나 OpenCV와 NumPy 추가에는 차이가 있음을 명심하십시오. NumPy는 모듈러스 산술과 "랩 어라운드"를 수행합니다. 반면에 OpenCV는 클리핑을 수행하고 픽셀 값이 \*[0, 255]\* 범위를 벗어나지 않도록합니다 .**

하지만 걱정하지 마세요! 아래 코드를 살펴보면 이러한 뉘앙스가 더욱 명확 해집니다.

### 이미지 연산의 적용 예

![](https://www.pyimagesearch.com/wp-content/uploads/2021/01/opencv_image_arithmetic_filters.jpg)

인스타그램에서와 같이 이미지에 필터효과를 주는데 사용(밝기(brightness), 대비(contrast))

이제 이미지 산술의 기초를 이해 했으므로 실제 세계에서 이미지 산술을 어디에 사용할지 궁금 할 것입니다.

기본 예는 다음과 같습니다.

- 설정된 양을 더하거나 빼서 **밝기 및 대비 조정** (예 : 이미지의 밝기를 높이기 위해 모든 픽셀 값에 *50* 을 더함 )

- **, 알파 블렌딩과 투명성 작업** 

  [튜토리얼](https://www.pyimagesearch.com/2018/11/05/creating-gifs-with-opencv/)

- **Instagram과 유사한 필터 만들기** -이 필터는 픽셀 강도에 적용되는 단순한 수학적 함수입니다.

직접 코드를 통해서 알아보도록 한다.

참조 - OpenCV_Image_Arithmetic.ipynb