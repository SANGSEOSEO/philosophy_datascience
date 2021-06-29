### 회귀 알고리즘

회귀는 현대 통계학을 이루는 큰 축이며 유전적 특성을 연구한 영국의 통계학자 갈톤(Galton)이 수행한 연구에서 유래했다는 것이 일반적이다.

데이터분석가들은 분류보다는 회귀를 지도 학습 분야에서 가장 많이 활용한다.

"부모의 키가 크더라도 자식의 키가 대를 이어 무한정  커지지 않으며 , 부모의 키가 작더라도 대를 이어 자식의 키가 무한정 작아지지 않는다"

#### 회귀 개요

* 회귀는 여러 개의 독립변수와 한 개의 종속변수 간의 상관관계를 모델링하는 기법을 통칭하며, 결정값이 주어지는 지도학습이라고 할 수 있다.

회귀분석은 이처럼 데이터 값이 평균과 같은 일정값으로 돌아가려는 경향을 이용한 통계학 기법

아파트 가격의 결정은 방 개수, 아파트 크기, 주변 학군, 근처 지하철 역 갯수등 다양한 독립변수로의 결합으로 이루어진다고 가정해보자.

그럼, 아래와 같은 수식을 생각해본다면,
$$
Y = W_1 * X_1 + W_2 * X_2 + W_3 * X_3 + .... + W_n * X_n
$$
`Y는 종속변수, 즉 아파트 가격`
$$
X_1, X_2, X_3, ....X_n 은 방 개수, 아파트 크기, 주변 학군등의 독립변수
$$

$$
W_1, W_2, W_3, ....W_n은 이 독립변수의 값에 영향을 미치는 회귀계수
$$

<span style="color:red"><b>`머신러닝 회귀 예측`의 핵심은 주어진 피처와 결정 값 데이터 기반에서 학습을 통해 최적의 회귀 계수를 찾아내는 것</b></span>

#### 회귀의 유형

* 회귀는 회귀 계수의 선형/비선형 여부, 독립변수의 개수, 종속변수의 개수에 따라 여러가지 유형으로 나눌 수 있습니다. 회귀에서 가장 중요한 것은 바로 회귀계수(`coefficient`)입니다. 이 회귀계수가 `선형이냐 비선형`에 따라 선형 회귀와 비선형 회귀로 나눌 수 있습니다. 그리고 독립 변수의 갯수가 한 개인지 여러 개인지에 따라 단일회귀, 다중 회귀로 나뉩니다.

  | 독립변수 갯수      | 회귀 계수의 결합    |
  | ------------------ | ------------------- |
  | 1개 : 단일 회귀    | 선형 : 선형 회귀    |
  | 여러 개: 다중 회귀 | 비선형: 비선형 회귀 |


#### 분류와 회귀

| 분류(Classification)                                         | 회귀(Regression)                             |
| ------------------------------------------------------------ | -------------------------------------------- |
| 결과값 : category값(이산값)으로 0, 1, 2,3과 같이 불연속적인 값<br />예) 등급, 고양이 혹은 개 판정 | 숫자값으로 연속적인 값<br />예) 비율, 점유울 |

#### 선형회귀의 종류

* 일반 선형 회귀 : 예측값과 실제 값의 `RSS(Residual Sum of Squares)`를 최소화 할 수 있도록 회귀 계수를 최적화하며, 규제(Regulation)를 적용하지 않은 모델

* `릿지(Ridge)`: 릿지 회귀는 선형 회귀에 `L2규제`를 추가한 회귀 모델

* `라쏘(Lasso)` : 라쏘 회귀는 선형 회귀에 `L1규제`를 적용한 방식

* `엘라스틱넷(ElasticNet)` : `L2, L1규제`를 함께 결합한 모델

* `로지스틱 회귀(Logistic Regression)` : 로지스틱 회귀는 회귀라는 이름이 붙어 있지만, 사실은 분류에 사용되는 선형모델

  예) `0, 1`의 값을 예측(이산) - 바이너리 분류에 효과적

  

#### 단순 선형 회귀(Simple Regression)를 통한 회귀의 이해

주택 가격이 단순히 주택의 크기로만 결정되는 단순 선형 회귀로 가정하면 다음과 같이 주택가격은 주택 크기에 대해 선형(직선 형태)의 관계로 표현 할 수 있다.

회귀는 우측의 이미지처럼 `실제값과 모델 사이의 오류값의 차이를 최소화 하는 것`을 목표로 하며, 점선형태의  `빨간색 ` 회귀선처럼 오류차이가 많이 나면 좋지 않다고 할 수 있다.

| <img src="https://user-images.githubusercontent.com/70785000/122632039-07c30980-d10b-11eb-950c-e0106cba710a.PNG" alt="regression_1" style="zoom:80%;" /> | <img src="https://user-images.githubusercontent.com/70785000/122632286-d0edf300-d10c-11eb-853d-5805356da673.PNG" alt="regression_2" style="zoom:80%;" /> |
| ------------------------------------------------------------ | ------------------------------------------------------------ |

<span style="color:red">`최적의 회귀 모델을 만든다는 것은 바로 전체 데이터의 잔차(오류 값)합이 최소가 되는 모델을 만든다는 의미이며, 동시에 오류 값이 최소가 될 수 있는 최적의 회귀계수를 찾는다는 의미도 된다.`</span>

#### RSS기반의 회귀 오류 측정

RSS란?

오류 값의 제곱을 구해서 더하는 방식. 일반적으로 미분 등의 계산을 편리하게 하기 위해서 RSS방식으로 오류 합을 구합니다. 
$$
Error_2 = RSS
$$
![rss](https://user-images.githubusercontent.com/70785000/122643155-3233b780-d149-11eb-9f75-f6f70c286b62.PNG)

#### RSS의 이해

- RSS는 이제 변수가 w0,w1인 식으로 표현할 수 있으며, 이 RSS를 최소로 하는 w0, w1, 즉 회귀 계수를 학습을 통해서 찾는 것이 머신러닝 기반 회귀의 핵심사항

- RSS는 <span style="color:red">회귀식의 독립변수 X, 종속변수 Y가 중심 변수가 아니라, w변수(회귀계수)가 중심 변수 임을 인지하는 것이 매우 중요합니다.</span>(학습 데이터로 입력되는 독립변수와 종속변수는 RSS에서 모두 상수로 간주합니다)

- 일반적으로 RSS는 학습 데이터의 건수로 나누어서 다음과 같이 정규화된 식으로 표현됩니다.(i는 1부터 학습 데이터의 총 건수 N까지)

  ![rss_math](https://user-images.githubusercontent.com/70785000/122643808-df5bff00-d14c-11eb-9b97-fbee12369caf.PNG)

#### RSS - 회귀의 비용 함수

![rss_math](https://user-images.githubusercontent.com/70785000/122643808-df5bff00-d14c-11eb-9b97-fbee12369caf.PNG)

회귀에서 이 `RSS는 비용(Cost)`이며 `w변수(회귀계수)`로 구성되는 RSS를 <span style="color:red">비용함수</span>라고 합니다. 머신 러닝 회귀 알고리즘은 데이터를 계속 학습하면서 이 비용 맘수가 반환하는 값(즉, 오류 값)을 지속적으로 감소시키고 최종적으로는 더 이상 감소하지 않는 최소의 오류 값을 구하는 것입니다. 비용함수를 손실함수(loss function)라고도 합니다.



#### 비용 최소화하기  - 경사하강법(Gradient Descent)

W파라미터의 갯수가 적다면 고차원 방정식으로 비용 함수가 최소가 되는 w 변숫값을 도출할 수 있겠지만, w파라미터가 많으면 고차원 방정식을 동원하더라도 해결하기가 어렵습니다.

경사하강법은 이러한 고차원 방정식에 대한 문제를 해결해 주면서 비용 함수 RSS를 최소화하는 방법을 직관적으로 제공하는 뛰어난 방식입니다.

![gradient_descent](https://user-images.githubusercontent.com/70785000/122644851-3f08d900-d152-11eb-8a2a-e59e876694f0.PNG)

경사하강법의 사전적 의미인 `점진적인 하강`이라는 뜻에서도 알수 있듯이, `점진적으로 반복적인 계산을 통해서 W파라미터 값을 업데이트하면서 오류값이 최소가 되는 W파라미터를 구하는 방식`.

* 경사하강법은 반복적으로 비용 함수의 반환 값, 즉 예측값과 실제 값의 차이가 작아지는 방향성을 가지고 W파라미터를 지속해서 보정해 나갑니다.
* 최초 오류 값이 `100`이었다면 두 번째 오류값은`100`보다 작은 `90`, 세 번째는 `80`과 같은 방식으로 지속해서 오류를 감소시키는 방향으로 `W값`을 계속 업데이트 해 나갑니다.
* 그리고 오류 값이 더 이상 작아지지 않으면 그 오류 값을 최소 비용으로 판단하고 그때의 `W값`을 최적 파라미터로 반환합니다

#### 미분을 통해 비용 함수의 최소값을 찾기

어떻게 하면 오류가 작아지는 방향으로 W값을 보정할 수 있을까?

​                                            <span style="color:red">미분은 증가 또는 감소의 방향성을 의미</span>

![gradient_descent](https://user-images.githubusercontent.com/70785000/122644851-3f08d900-d152-11eb-8a2a-e59e876694f0.PNG)

비용함수가 다음 같은 포물선 형태의 2차 함수라면 경사하강법은 최조 w에서부터 미분을 적용한 뒤 이 미분 값이 계속 감소하는 방향으로 순차적으로 w를 업데이트합니다.

마침내 더 이상 미분된 1차 함수의 기울기가 감소하지 않는 지점을 비용 함수가 최소인 지점으로 간주하고 그때의 w를 반환합니다.

#### RSS의 편미분

R(w)는 변수가 w 파라미터로 이뤄진 함수이며, 
$$
R(w) = \frac {1}{N}\sum_{i=1}^N (y_i - (w_0 + w_1 * x_i))^2
$$
입니다. R(w)를 미분해 미분함수의 최솟값을 구해야 하는데, R(w)는 두개의 w파라미터인 w0와 w1을 각각 가지고 있기 때문에 일반적인 미분을 적용할 수가 없고, w0, w1 각 변수에 편미분을 적용해야 합니ㅏㄷ.

R(w)를 최소화하는 w0와 w1 값은 각각 r(w)를 w0, w1으로 순차적으로 편미분을 수행해 얻을 수 있습니다.

![rss_편미분](https://user-images.githubusercontent.com/70785000/122647666-5353d280-d160-11eb-8ced-749a0470ff98.PNG)

###### RSS의 편미분 - W1으로 편미분



###### RSS의 편미분 - W0으로 편미분

![편미분풀어헤치기_1](https://user-images.githubusercontent.com/70785000/122697075-82ad3100-d27f-11eb-8782-c2adf1dbb2d7.PNG)

식을 풀어헤치면

![편미분풀어헤치기](https://user-images.githubusercontent.com/70785000/122697115-9d7fa580-d27f-11eb-8ee7-f0e408d9e9ed.PNG)

위와 같이 w1, w0의 편미분 결과값인 최종 결과값을 반복적으로 보정하면서 w1, w0값을 업데이트 하면 비용함수 r(w)가 최소가 되는 w1, w0값을 구할 수 있습니다. 

하지만 실제로는 위 편미분 값이 너무 클 수 있기 때문에 보정 계수 &eta;를 곱하는데 , 이를 `학습률`이라고 한다.

**경사하강법은 아래와 같은 새로운 w1, 새로운 w0를 반복적으로 업데이트 하면서 비용 함수가 최소가 되는 값을 찾습니다.**

![최종공식](https://user-images.githubusercontent.com/70785000/122697190-c6079f80-d27f-11eb-8d8d-0cc722596e71.PNG)

#### 경사하강법 수행 프로세스

* `Step1` - `w1, w0`를 임의의 값으로 설정하고 첫 비용 함수의 값을 계산
* `Step2` -` w1과 w0`의 값을 위의 비용함수의 계산식으로 업데이트 한 후 다시 비용 함수의 값을 계산
* `Step3` - 비용 함수의 값이 감소했으면 다시 `Step2`를 반복합니다.  더 이상의 비용 함수의 값이 감소하지 않으면 그때의 `w1, w0`를 구하고 반복을 중지합니다.

#### 사이킷런 `LinearRegression`클래스

##### LinearRegression클래스

`class sklearn.linear_model.LinearRegression(fit_intercept=True, normalize=False, copy_X = True, n_jobs=1)`

* `linearRegressoin`클래스는 예측값과 실제 값의 `RSS(Residual Sum of Squares)`를 최소화해 `OLS(Ordinary Least Squares)추정 방식`으로 구현한 클래스

* `LinearRegression`클래스는 `fit()`메소드로 X, y 배열을 입력받으면 회귀 계수(`coefficients)인  W`를 `coef_`속성에 저장

  | 입력 파라미터 | `fit_intercept` : 불린 값으로 디폴트는 True<br />`Intercept(절편)`값을 계산할 것인지 말지를 지정<br />만일 False로 지정하면 `intercept`가 사용되지 않고 `0`으로 지정된다.<br /><br />normalize : 불린값으로 디폴트는 False.`fit_intercept`파라미터가 False인 경우는 이 파라미터가 무시됩니다. 만일 True이면 회귀를 수행하기 전에 입력 데이터세트를 정규화한다.<br />![fit_intercept_true](https://user-images.githubusercontent.com/70785000/122735569-1e5b9300-d2ba-11eb-948e-bfb74c977c6d.PNG) |
  | ------------- | ------------------------------------------------------------ |
  | 속성          | coef_`: fit()`메소드를 수행했을 때 회귀 계수가 배열 형태로 저장하는 속성.<br />`Shape는 (Target값 개수, 피처갯수)`<br />`intercept_ : intercept값` |

##### 선형회귀의 다중 공선성 문제

* 일반적으로 선형 회귀는 입력 피처의 독립성에 많은 영향을 받습니다. 피처간의 상관관계가 매우 높은 경우 분산이 매우 커져서 오류에 매우 민감해집니다. 이러한 현상을 다중 공선성(`multi-collinearity`)문제하고 합니다. 일반적으로 상관관계가 높은 피처가 많은 경우 독립적인 중요한 피처만 남기고 제거하거나 규제를 적용합니다.

  예) `A`라는 피처가 방의 크기인데 평이고, 어떤 피처는 제곱미터(m^2)가 되어있는 예

##### 회귀평가지표

| 평가지표 | 설명                                                         | 수식                                                         |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `MAE`    | `Mean Absolute Error(MAE)`이며 실제 값과 예측값의 차이를 절대값으로 변환해 평균한 것. | ![MAE](https://user-images.githubusercontent.com/70785000/122759351-cc743680-d2d4-11eb-895c-9c069dc28127.PNG) |
| `MSE`    | `Mean Squared Error(MSE)`이며 실제 값과 예측값의 차이를 제곱해 평균한 것 | ![MSE](https://user-images.githubusercontent.com/70785000/122759669-2bd24680-d2d5-11eb-8aa5-486592971274.PNG) |
| `MSLE`   | `MSE`에 로그를 적용한 것. 결정값이 클수록 오류값도 커지기 때문에 일부 큰 오류값들로 인해 전체 오류값이 커지는 것을 막아줍니다.<br />예) 매출금액과 같이 금액이 큰 경우. | `Log(MSE)`                                                   |
| `RMSE`   | `MSE`값은 오류의 제곱을 구하므로 실제 오류 평균보다 더 커지는 특성이 있으므로 `MSE`에 루트를 씌운 것이 `RMSE(Root Mean Squared Error)`입니다. | ![RMSE](https://user-images.githubusercontent.com/70785000/122760009-984d4580-d2d5-11eb-8924-7a531521ac7a.PNG) |
| `RMSLE`  | `RMSE`에 로그를 적용한 것입니다. 결정값이 클수록 오류값도 커지기 때문에 일부 큰 오류값들로 인해 전체 오류값이 커지는 것을 막아줍니다. | `Log(RMSE)`                                                  |
| `R^2`    | 분산 기반으로 예측 성능을 평가합니다.실제 값의 분산 대비 예측값의 분산 비율을 지표로 하며, 1에 가까울수록 예측 정확도가 높습니다. | ![R2](https://user-images.githubusercontent.com/70785000/122760221-d9ddf080-d2d5-11eb-877f-1d1cbf091c93.PNG) |

##### 사이킷런 회귀 평가 API

* 사이킷런은 아쉽게도 RMSE를 제공하지 않습니다. RMSE를 구하기 위해서는 MSE에 제곱근을 씌우서 계산하는 함수를 직접 만들어야 합니다.
* 다음은 각 평가 방법에 사이킷런의 API및 `cross_val_score`나 `GridSearchCV`에서 평가 시 사용되는 `scoring파라미터의 적용 값`입니다.

| 평가방법 | 사이킷런 평가지표 API         | Scoring 함수 적용 값        |
| -------- | ----------------------------- | --------------------------- |
| MAE      | `metrics.mean_absolute_error` | `'neg_mean_absolute_error'` |
| MSE      | `metrics.mean_squared_error`  | `'neg_mean_squared_error'`  |
| R^2      | `metrics.r2_score`            | `'r^2'`                     |

###### 사이킷런 Scoring함수에 회귀 평가 적용시 유의 사항

**`cross_val_score, GridSearchCV와 같은 Scoring함수에 평가지표를 적용시 유의사항`**

* `MAE`의 사이킷런 scoring파라미터 값은 `'neg_mean_absolute_error'`입니다. 이는 `Negative(음수)값`을 가진다는 의미인데, MAE는 절댓값의 합이기 때문에 음수가 될 수 없습니다.
* Scoring함수에 `'neg_mean_absolute_error'`를 적용해 음수값을 반환하는 이유는 사이킷런의 `Scoring함수가 score값`이 클수록 좋은  평가결과로 자동 평가하기 때문입니다. 따라서 `-1`을 원래의 평가지표 값에 곱해서 음수(`negative`)를 만들어 작은 오류 값이 더 큰 숫자로 인식하게 됩니다. 예를 들어 `10 > 1`이지만 음수를 곱하면 `-1 > -10`이 됩니다.(오류값이 작을 수록 좋은 지표이기 때문에 원래의 평가지표에 `-1`을 곱함)
* `metrics.mean_absolute_error()`와 같은 사이킷런 평가 지표 API는 정상적으로 양수의 값을 반환합니다. 하지만 `Scoring함수`의 `scoring파라미터 값` `'neg_mean_absolute_error'`가 의미하는 것은 `-1 * metrics.mean_absolute_error()`이니 주의가 필요합니다.

#### 다항회귀 개요(Polynomial Regression)

다항회귀는 아래와 같이 회귀식이 독립변수의 단항식이 아닌 2차, 3차 방정식과 같은 다항식으로 표현되는 것을 지칭합니다.

![다항식](https://user-images.githubusercontent.com/70785000/122888410-d05b9380-d37c-11eb-9b46-05375c206ea8.PNG)

다음 그림을 보면,단항 회귀보다 다항 회귀 곡선으로 표현되는 더 예측 성능이 좋음을 알 수 있습니다.

![단항_vs 다항](https://user-images.githubusercontent.com/70785000/123013823-e5c5d180-d3ff-11eb-8101-c71a35962737.PNG)

##### 선형회귀와 비선형회귀의 구분

###### 선형회귀

$$
Y = w0 + w_1x_1 + w_2x_2 + w_3x_1x_2 + w_4x_1^2 + w_5x_2^2
$$

새로운 변수인 Z를 z = [x1, x2, x1 * x2, x1^2, x2^2]로 한다면?
$$
Y = w_0 + w_1z_1 + w_2z_2 + w_3z_3 + w_4z_4 + w_5z_5
$$

```
다항회귀는 선형 회귀입니다. 회귀에서 선형회귀 / 비선형 회귀를 나누는 기준을 회귀계수가 선형/비선형인지에 따른 것이지 독립변수의 선형/비선형 여부와는 무관합니다.
```

###### 비선형회귀

$$
Y = w_1cos(X + w_4 + w_2cos(2X + w_4) + w_3)
$$

$$
Y = w_1 + X^w_2
$$



##### 사이킷런에서의 다항 회귀

사이킷런은 다항 회귀를 바로 API로 제공하지 않음.

대신 PolynomialFeatures클래스로 원본 단항 피처들을 다항 피처들로 변환한 데이터 세트에 `LinearRegression`객체를 적용하여 다항 회귀 기능을 제공함

###### PolynomialFeatures

* 원본 피처 데이터 세트를 기반으로 `degree차수`에 따른 다항식을 적용하여 새로운 피처들을 생성하는 클래스 피처 엔지니어링의 기법중의 하나.

* 단항 피처 `[x1, x2]`를 `Degree=2`, 즉 다항 피처로 변환한다면?

  `(x1 + x2)^2`의 식 전개에 대응되는 변환된 다항피처의 모습은 다음과 같다.

![다항피처](https://user-images.githubusercontent.com/70785000/123220483-fa41c100-d508-11eb-9d6b-d097fc4f77f8.PNG)

* 1차 단항 피처들의 값이 [x1, x2] = [0, 1] 일 경우, 2차 다항 피처들의 값은 [1, x1 = 0, x2 = 1, x1 * x2 = 0, x1^2 = 0, x2^2 = 1]형태인 [1, 0 , 1, 0, 0, 1]로 변환

* 단항 피처 [x1, x2]를 Degree=3, 즉 3차 다항 피처로 변환한다면?

  (x1 + x2)^3의 시 전개에 대응되는 아래와 같은 다항 피처로 변환

  ![3차 다항식](https://user-images.githubusercontent.com/70785000/123221745-36295600-d50a-11eb-8879-d00b1dca5854.PNG)

```
사이킷런에서는 일반적으로 Pipeline클래스를 이용하여 PolynomialFeatures변환과 LinearRegression 학습 / 예측을 결합하여 다항 회귀를 구현합니다.
```

#### 편향-분산 트레이드 오프(`Bias-Variance Trade off`)

* [Understanding the Bias-Variance Trade off](http://scott.fortmann-roe.com/docs/BiasVariance.html)

  `Bias가 크다`는 의미는 타겟 값과의 떨어져 있다는 의미.

  ![understanding bias_variance](https://user-images.githubusercontent.com/70785000/123395318-08601200-d5db-11eb-9ab7-07f1db883634.PNG)

* `과소적합 v.s well-fit v.s Overfitting`

  `Degree 1` - 1차 회귀 직선형(과소적합) - 편향이 큰것임

  `Degree 4` - 회귀선 (잘 학습됨): well-fit된 회귀 곡선, 오류가 있음에도 불구하고 학습이 잘되어있고, MSE값도 작음

  `Degree 15` - 복잡한 곡선(과대적합) - 모든 학습 데이터를 정확히 예측하기 위해 굉장히 복잡한 곡선이 만들어짐. `Mean Squared Error`이 터무니없이 커짐.(소위 팔랑귀로서 모든 데이터를 만족해야함. 분산이 굉장히 높아짐)

| ![과소적합](https://user-images.githubusercontent.com/70785000/123394844-896ad980-d5da-11eb-9764-c9f36af7b7c0.PNG) | ![well_fit](https://user-images.githubusercontent.com/70785000/123395097-c8009400-d5da-11eb-9c9c-c5888d653669.PNG) | ![overfitt](https://user-images.githubusercontent.com/70785000/123395145-d3ec5600-d5da-11eb-88a8-210e19a25493.PNG) |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |

* 편향- 분산 트레이드 오프의 관계에 대한 고찰

  * 편향이 높으면 분산은 낮아지고
  * 분산이 높으면 편향이 낮아짐

  ![total_error](https://user-images.githubusercontent.com/70785000/123449735-eab09e00-d616-11eb-981a-ca7ba16c7438.PNG)

#### 규제 선형 회귀 개요

위의 다항식의 차수를 변경함에 있어 `degree=15`인 경우의 다항 회귀는 지나치게 모든 데이터에 적합한 회귀식을 만들기 위해서 다항식이 복잡해지고 회귀 계수가 매우 크게 설정이 되면서 과대적합이 되고 평가 데이터 세트에 대해서 형편없는 예측 성능을 보임.

따라서 회귀 모델은 적절히 데이터에 적합하면서도 회귀 계수가 기하급수적으로 커지는 것을 제어 할 수 있어야 함.

![비용함수목표](https://user-images.githubusercontent.com/70785000/123507553-0a8ea300-d6a5-11eb-84f5-0fe34fcda30e.PNG)

이로 인해 , 비용함수의 목표가 `학습데이터 잔차오류(RSS)`도 줄이면서 회귀계수도 크기도 적절하게 제거가 되어야 할 필요성이 대두됨.

아래는 비용함수의 목표를 수식으로 기술한 것으로 ,`alpha`는 학습 데이터 적합 정도와 회귀 계수 값의 크기 제어를 수행하는 튜닝 파라미터.

![비용함수](https://user-images.githubusercontent.com/70785000/123507796-6f96c880-d6a6-11eb-9b43-eb25942e4010.PNG)

##### 규제선형 모델에서의 alpha의 역할

* `alpha`가 0(또는 매우 작은 값)이라면 비용 함수 식은 기존과 동일한 `Min(RSS(W) + 0)`이 될 것입니다.
* 반면에 `alpha`가 무한대 (또는 매우 큰 값)라면 비용 함수 식은 `RSS(W)`에 비해` alpha * ||W||_2^2 값`이 너무 커지게 되므로 `W값`을 `0`(또는 매우 작게)으로 만들어야` Cost`가 최소화되는 비용 함수 목표를 달성 할 수 있습니다.
* 즉, `alpha값`을 크게 하면 비용 함수는 `회귀 계수 W`의 값을 작게 해 과적합을 개선할 수 있으며 `alpha값`을 작게 하면 `회귀 계수 W의 값`이 커져도 어느 정도 상쇄가 가능하므로 학습 데이터 적합을 더 개선할 수 있습니다.

* 비용함수의 목표

  ![비용함수](https://user-images.githubusercontent.com/70785000/123507796-6f96c880-d6a6-11eb-9b43-eb25942e4010.PNG)

##### 규제 선형 회귀의 유형

* 이처럼 비용 함수에 `alpha값`으로 <span style="color:red">페널티</span>를 부여해 회귀 계수 값의 크기를 감소시켜 과적합을 개선하는 방식을 규제(`Regulation`)라고 부릅니다.
* 규제는 크개 `L2방식`과 `L1방식`으로 구분합니다. `L2규제`는 위에서 설명한 바와 같이 `alpha * ||W||_2^2` 와 같이 <span style="color:red">`W의 제곱`에 대해 `페널티`를 부여하는 방식</span>을 말합니다. `L2규제`를 적용한 회귀를 릿지 회귀라고 함
* 라쏘회귀는 `L1규제`를 적용한 회귀입니다. `L1`규제는 `alpha * ||W||_1`와 같이 <span style="color:red">`W`의 절댓값에 대해 페널티를 부여</span>합니다. **`L1규제`를 적용하면 영향력이 크지 않은 회귀 계수값을 `0`으로 변환**합니다.
* `ElasticNet:L2, L1`규제를 함께 결합한 모델입니다. 주로 피처가 많은 데이터 세트에서 적용되며, `L1`규제로 피처의 갯수를 줄임과 동시에 L2규제로 계수 값의 크기를 조정합니다.

##### Ridge회귀

* 사이킷런은 릿지 회귀를 위해 `sklearn.linear_model import Ridge`클래스를 제공

##### Lasso회귀

W의 절댓값에 페널티를 부여하는 L1규제를 선형회귀에 적용 한 것이 라쏘회귀.

즉, L1규제는 `alpha * ||W||_1` 를 의미하며, 라쏘 회귀 비용함수의 목표는 RSS(W) + `alpha * ||W||_1`식을 최소화하는 W를 찾는것.

L2규제가 회귀 계수의 크기를 감소시키는데 반해, <span style="color:red">L1규제는 불필요한 회귀 계수글 급격하게 감소시켜 0으로 만들고 제거합니다.</span> 이러한 측면에서 L1규제는 적절한 피처만 회귀에 포함시키는 피처 셀렉션의 특성을 가짐.

사이킷런은 Lasso클래스를 통해 라쏘 회귀를 구현.

##### 엘라스틱넷 회귀

* 엘라스틱넷 회귀는 L2규제와 L1규제를 결합한 회귀.따라서 엘라스틱넷 회귀 비용함수의 목표는 아래식을 최소하는 W값 찾는 것

![elastic_lossfunc](https://user-images.githubusercontent.com/70785000/123537838-90295600-d76c-11eb-8927-1ad9c2010241.PNG)

* 엘라스틱넷은 라쏘 회귀가 서로 상관관계가 높은 피처들의 경우,이들 피처중에서 중요 피처만을 선택하고 다른 피처들은 모두 회귀 계수를 0으로 만드는 성향이 있어, alpha값에 따라 회귀 계수의 값이 급격히 변동 할 수 도 있는데, 엘라스틱 넷 회귀는 이를 완화하기 위해 L2규제를 라쏘 회귀에 추가한 것.
* 구현클래스 : `sklearn.linear_model import ElasticNet`
* 주요 생성 파라미터  : `alpha`와 `l1_ratio`이며, `ElasticNet클래스의 alpha`는 `Ridge`와 `Lasso`클래스의 `alpha`값과는 다름에 유의.
* **엘라스틱넷의 규제는 a L1규제 + b L2 규제로 정의될 수 있습니다. **

| `ElasticNet alpha`파라미터                                   | `ElasticNet l1_ratio`파라미터                                |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 이때 `a`는 L1규제의 `alpha`값, b는 L2규제의 `alpha`값<br />따라서 `ElasticNet클래스의 alpha파라미터 값은 a + b` | `ElasticNet클래스`의 `l1_ratio파라미터 값`은 `a / (a + b)`입니다.<br />`l1_ratio`가 `0`이면 `a`가 `0`이므로 `L2규제`와 동일<br />`l1_ratio`가 `1`이면 `b가 0이므로 L1규제와 동일`<br /> `0 < l1_ratio < 1`이면 `L1과 L2`규제를 함께 적절히 적용합니다. |

```
만일, 엘라스틱넷의 alpha가 10, l1_ratio가 0.7이면 
L1_ratio = 0.7 = a / a + b = 7/10이므로 a = 7이고 L1 alpha값은 7이고 , L2 alpha값은 3입니다.
```

##### 선형 회귀 모델을 위한 데이터 변환

회귀모델과 같은 선형 모델은 일반적으로 피처와 타겟값 간에 선형의 관계가 있다고 가정하고, 이러한 최적으로 선형함수를 찾아내 결과값을 예측합니다.

또한 선형 회귀 모델은 피처값과 타깃값의 분포가 정규 분포( 즉 평균을 중심으로 종 모양으로 데이터 값이 분포된 형태) 형태를 매우 선호합니다.

| ![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTncyhuNRuk7f5W52BSZcHcONFMGjrY69MbPQ&usqp=CAU) | ![](data:image/png;base64,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) |
| ------------------------------------------------------------ | ------------------------------------------------------------ |

* 선형회귀 모델은 종모양의 정규분포 형태를 선호하고 그런 형태로 바꾼 다음에 학습 및 예측 평가를 해야 함

###### 회귀를 위한 데이터 변환 방법

| 변환 대상   | 설명                                                         |
| ----------- | ------------------------------------------------------------ |
| 타겟값 변환 | 회귀에서 타겟값은 반드시 정규 분포를 가져야 함. <br />이를 위해 주로 `로그변환을 적용` |
| 피처값 변환 | 1)`StandardScaler클래스`를 이용해 `평균이 0, 분산이 1인 표준 정규 분포를 가진 데이터 세트로 변환`하거나 `MinMaxScaler클래스`를 이용해 `최솟값이 0이고 최댓값이 1인 값으로 정규화`를 수행 |
|             | 2)스케일링/정규화를 수행한 데이터 세트에 다시 다항특성을 적용하여 변환하는 방법<br />1)번 방법을 통해 예측 성능 향상이 없을 경우 적용 |
|             | 원래 값에` log함수`를 적용하면 보다 정규 분포에 가까운 형태로 값이 분포된다.<br />로그변환은 매우 우용한 변환이며, 실제로 선형 회귀에서는 앞에서 소개한 1, 2번 방법보다 로그 변환이 훨씬 많이 사용되는 변환방법<br />그 이유는 , 1번 방법은 크게 예측 성능향상의 기대가 어려운 경우가 많고, 2번 방법의 경우 피처의 갯수가 매우 많은 경우엔 다항변환으로 생성되는 피처의 갯수가 기하급수적으로 늘어나 과적합이 발생할 수 있기 때문 |

###### 인코딩

선형회귀의 데이터 인코딩은 일반적으로 레이블 인코딩이 아니라 <span style="color:red">원-핫 인코딩</span>을 적용합니다

###### 선형회귀 모델에 대한 예측 성능 비교

* 로그변환을 하고 제어값(alpha)이 일정 수준으로 변경시 RMSE값이 줄어듦을 확인

#### 로지스틱 회귀 개요

* 로지스틱 회귀는 선형 회귀방식을 분류에 적용한 알고리즘.즉, 로지스틱 회귀는 분류에 사용
* 선형회귀와 다른 점은 학습을 통해 선형 함수의 회귀 최적선을 찾는 것이 아니라 시그모이드 함수 최적선을 찾고 이 시그모이드 함수의 반환 값을 확률로 간주해 확률에 따라 분류를 결정한다는 것.
* 좌측의 그림은 `선형회귀의 선형 함수` 이고 우측의 그림은 `로지스틱회귀의 시그모이드함수`

| <img src="https://user-images.githubusercontent.com/70785000/122632286-d0edf300-d10c-11eb-853d-5805356da673.PNG" alt="regression_2" style="zoom:80%;" /> | ![sigmoid](https://user-images.githubusercontent.com/70785000/123725421-05aa3900-d8c9-11eb-9381-b15eacf97589.PNG) |
| ------------------------------------------------------------ | ------------------------------------------------------------ |

##### 로지스틱회귀 예측

* 로지스틱 회귀는 주로 이진분류(0과 1)에 사용(물론 다중 클래스분류에도 사용).로지스틱 회귀에서 예측값은 예측 확률을 의미하며, 예측 값 즉, 예측 확률이 0.5이상이면 1로, 0.5이하이면 0으로 예측.
* 로지스틱 회귀의 예측 확률은 시그모이드 함수의 출력값으로 계산

```
def logistic(x):
	"""
	시그모이드 함수 정의
	"""
    return 1 / (1 + np.exp(-x))
    
xx = np.linspace(-8, 8, 100)
plt.plot(xx, logistic(xx))
plt.axvline(0, c = 'r', ls = '--')
plt.axhline(0.5, c = 'r', ls = '--')
plt.plot(0, 0.5, marker = 'o', ms = 10)
plt.title("로지스틱 함수")
plt.xlabel("$x$")
plt.ylabel("$sigmoid(x)$")
plt.grid(True)
plt.show()
```

![sigmoid1](https://user-images.githubusercontent.com/70785000/123726271-a9481900-d8ca-11eb-97d9-170bfed03be1.PNG)

단순 선형회귀 : y = w1x + w0가 있다고 가정할때 

로지스틱 회귀는 0과 1을 예측하기에 단순 회귀식은 큰 의미가 없습니다. 

하지만 `Odss(성공확률 /  실패확률)`을 통해 선형 회귀식에 확률을 적용할 수 있습니다.

```
p - 성공확률 , 1-p : 실패확률
Odds(p) = p / (1- p)
```

하지만 `확률 p의 범위가 (0, 1)`이므로 선형 회귀의 반환값은 (-무한대, + 무한대)에 대응하기 위하여 로그 변환을 수행하고 이 값에 대한 선형회귀를 적용합니다.

```
Log(Odds(p)) = w1x + w0
```

해당 식을 데이터 값 `x의 확률 p로 정리`하면 아래와 같습니다.

```
p(x) = 1 / (1 + e-(w1x + w0))
```

<span style="color:red">정리하면...</span>

```
로지스틱 회귀는 학습을 통해 시그모이드 함수의 W를 최적화하여 예측하는 것
```

##### 시그모이드를 이용한 로지스틱 회귀 예측

![sigmoid2](https://user-images.githubusercontent.com/70785000/123737556-1fa24680-d8de-11eb-9425-98c7b586a8aa.PNG)

##### 로지스틱 회귀 특징과 사이킷런 로지스틱 회귀 클래스

* 로지스틱 회귀는 가볍고 빠르지만, 이진 분류 예측 성능도 뛰어납니다. 이때문에 로지스틱 회귀를 이진 분류의 기본 모델로 사용하는 경우가 많습니다. 또한 로지스틱 회귀는 희소 데이터 세트 분류에도 뛰어난 성능을 보여서 텍스트 분류에서 자주 사용합니다.
* 사이킷런은 LogisticRegression클래스로 로지스틱 회귀를 구현합니다. 주요 하이퍼 파라미터로 `penalty`와 `C`가 있습니다. `Penalty` 는 규제의 유형을 설정하며 `l2`로 설정시 `L2규제`를, `l1`으로 설정시 `L1규제`를 의미함. 
  `default값`은 `l2`입니다. `C`는 규제 강도를 조절하는 `alpha`값의 역수입니다. 즉 `C=1/alpha` 입니다.
  `C`값 이 작을 수록 규제강도가 큽니다.

