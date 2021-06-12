# 분류알고리즘

분류는 학습데이터로 주어진 데이터의 피처와 레이블 값(결정 값, 클래스 값)을 머신러닝 알고리즘으로 학습해 모델을 생성하고, 이렇게 생성된 모델에 새로운 데이터 값이 주어졌을때 미지의 레이블 값을 예측하는 것.

## 대표적인 분류 알고리즘

* 베이즈통계와 생성 모델에 기반한 나이브 베이즈
* 독립변수와 종속 변수의 선형 관계성에 기반한 <span style="color:red">Logistic Regression</span>
* 데이터 균일도에 따른 규칙 기반의 결정트리
* 개별 클래스 간의 최대 분류 마진을 효과적으로 찾아주는 SVM(Support Vector Machine)
* 근접 거리를 기준으로 하는 최소 근접(Nearest Neighbor)알고리즘
* 심층 연결 기반의 신경망(Neural Network)
* 서로 다른 혹은 같은 머신러닝 알고리즘을 결합한 앙상블

### 결정트리와 앙상블

* 결정트리는 매우 쉽고 유연하게 적용될 수 있는 알고리즘.또한 데이터의 스케일링이나 정규화등의 사전 가공의 영향이 매우 적다. 하지만 예측 성능을 향상 시키지 위해 복잡한 규칙 구조를 가져야 하며, 이로 인한 과적합이 발생해 반대로 예측 성능이 저하될수도 있다는 단점이 있다.
* 앙상블은 이와 달리, 결정트리를 약한 학습기(예측 성능이 떨어지는 학습 알고리즘)로 여러개를 결합해 확률적 보완과 오류가 발생한 부분에 대한 가중치를 갱신하면서 예측 성능을 향상 시킨다.(GBM, XGBoost, LightGBM)

### 결정 트리

* 데이터에 있는 규칙을 학습을 통해 자동으로 찾아내 트리 기반의 분류 규칙을 만듦(If - Else기반 규칙)

* 따라서 데이터의 어떤 기준을 바탕으로 규칙을 만들어야 가장 효율적인 분류가 될 것인가가 알고리즘의 성능을 크게 좌우.

  ![의사결정트리](https://user-images.githubusercontent.com/70785000/120695618-8e120580-c4e6-11eb-8c65-1a3dd1274594.PNG)

* 규칙노드로 표시된 노드는 규칙조건이 되는것이고, 리프 노드로 표시된 노드는 결정된 클래스값.그리고 새로운 규칙 조건마다 서브트리가 생성됩니다. 데이터세트에 피처가 있고 이러한 피처가 결합해 규칙 조건을 만들 때마다 규칙노드가 만들어집니다.

* 트리의 깊이가 깊을 수록 결정 트리의 예측 성능이 저하될 가능성이 존재.

* 가능하다면 적은 결정 노드로 좋은 예측 정확도를 가지려면 데이터를 분류시 최대한 많은 데이터가 해당 분류에 속할 수 있도록 결정노드의 규칙이 정해져야 합니다.

* 리프노드로 결정된 노드는 정보 균일도가 높은 데이터가 모여있다고 이해하자.

* 정보 균일도 측정 계수 : 엔트로피를 이용한 정보 이득 지수와 지니계수가 있다.

### 데이터 균일도

* 균일도 기반 규칙 조건

  노란색 블록의 경우 모두 동그라미로 구성되고, 빨강과 파랑 블록의 경우는 동그라미, 네모 , 세모가 골고루 섞여 있다고 한다면 각 레고 블록을 분류하고자 할 때 가장 첫 번째로 만들어져야 하는 각 레코 블록을 분류하고자 할 때 가장 첫번째로 만들어져야 하는 규칙 조건은?

  ![균일도](https://user-images.githubusercontent.com/70785000/120695922-e34e1700-c4e6-11eb-9e33-9e845a125a80.PNG)

  **if 색깔 == '노란색'**  

#### 정보이득

* 정보이득은 <span style="color:red">엔트로피</span>라는 개념을 기반으로 함.<span style="color:red">주어진 데이터 집합의 혼잡도</span>를 의미함
* 서로 다른 값이 섞여 있으면 엔트로피가 높고, 같은 값이 섞여 있으면 엔트로피가 낮습니다. 정보이득 지수는 1에서 엔트로피지수를 뺀 값(1 - 엔트로피 지수)
* 정보 이득이 높은 속성을 기준으로 분할합니다.(즉, 엔트로피 지수가 낮은것)
* 정보이득은 데이터의 밀집도가 높은 속성을 기준으로 분할.

결정트리 알고리즘은 정보이득 지수가 높거나, 지니계수가 낮은 조건을 찾아서 자식 트리노드에 걸쳐 반복적으로 분할한 뒤, 데이터 모두 특정분류에 속하게 되면 분할을 멈추고 분류를 결정함

#### 지니계수

* 지니 계수는 원래 경제학에서 불평등 지수를 나타낼때 사용하는 계수. 경제학자인 코라도 지니의 이름에 딴 계수로서 0이 가장 평등하고 1로 갈수록 불평등합니다.머신러닝에 적용될 때는 지니계수가 낮을수록 데이터 균일도가 높은 것으로 해설되어 계수가 낮은 속성을 기준으로 분할.
* "상위 1퍼센트가 전체 국민소득의 99퍼센트를 번다''

### 결정트리 규칙 노드 생성 프로세스 

![의사결정트리_규칙](https://user-images.githubusercontent.com/70785000/120695886-d7625500-c4e6-11eb-9b40-7f88df0c64c4.PNG)

* 결정트리의 장점은, 쉽고 직관적이며, 피처의 스케일링이나 정규화등의 사전 가공 영향도가 크지 않다.
* 단점으로는, 과적합으로 알고리즘 성능이 떨어진다.이를 극복하기 위해 트리의 크기를 사전에 제한하는 튜닝 필요

#### 결정트리 주요 하이퍼파라미터

| 파라미터명        | 설명                                                         |
| ----------------- | ------------------------------------------------------------ |
| min_samples_split | * 노드를 분할하기 위한 최소한의 샘플 데이터 수로 과적합제어에 사용<br>* 디폴트는 2이고 작게 설정할 수록 분할되는 노드가 많아져 과적합 가능성이 커짐<br>*과적합을 제어,1로 설정할 경우 분할되는 노드가 많아져서 과적합 생김 |
| min_samples_leaf  | * 말단 노드(Leaf)가 되기 위한 최소한의 샘플 데이터 수 <br>* 과적합 제어용도.그러나 비대칭의 데이터의 경우 특정 클래스의 데이터가 극도로 작을 수 있으므로 이 경우는 작게 설정 필요. |
| max_features      | * 최적의 분할을 위해 고려할 최대 피처 갯수.디폴트는 None으로 데이터 세트의 모든 피처를 사용해 분할 수행.<br> * int형으로 지정하면 대상 피처의 개수, float형으로 지정하면 전체 피처 중 대상 피처의 퍼센트임.<br>* `sqrt`는 전체 피처 중 sqrt(전체 피처 개수)<br>* `auto`로 지정하면 `sqrt`와 동일 <br>* `log`는 전체 피처 중 log2(전체 피처갯수) 선정 <br>* `None`은 전체 피처 선정 |
| max_depth         | * 트리의 최대 깊이 <br>* 디폴트는 None.None으로 설정하면 완벽하게 클래스가 결정 값이 될때 까지 깊이를 계속 분할하거나 노드가 가지는 데이터 갯수가 min_samples_split보다 작아질때까지 계속 깊이를 증가시킴 <br>* 깊이가 깊어지면 min_samples_split설정대로 최대 분할하여 과적할 할 수 있으므로 적절한 값으로 제어 필요 |
| max_leaf_nodes    | * 말단 노드(Leaf)의 최대 갯수                                |

#### Graphviz패키지 설치

* [윈도우 버전 graphviz다운로드](https://graphviz.org/download/#windows)

* 파이썬 레퍼 설치 : pip install graphviz

* 아래 환경변수 설정은 버전에 따라 달라질 수 있음에 유의하자.

* 사용자 환경변수 Path에 값 : 설치경로\Graphviz2.38\bin추가

* 시스템환경변수 Path에 값 : 설치경로\Graphviz2.38\bin\dot.exe 추가 

* cmd >> dot -version 수행시 정상적으로 잡힌 경로가 보여야 한다.

  그렇지 않다면 dot -c로 수행후 다시 수행
  
  

## 앙상블 학습  - 앙상블 학습 개요

앙상블 학습(Ensemble Learning)을 통한 분류는 여러개의 분류기를 생성하고 그 예측을 결합함으로써 보다 정확한 예측을 도출하는 기법.

어려운 문제의 결론을 내기 위해 여러 명의 전문가로 위원회를 구성해 다양한 의견을 수렴하고 결정하듯이 양상블 학습의 목표는 다양한 분류기의 예측 결과를 결합함으로써 단일 분류기보다 신뢰성이 높은 예측값을 얻고자 하는데 있다.



### 앙상블 학습의 유형

* 앙상블의 유형은 일반적으로 Voting, Bagging, Boosting으로 구분하며, 이외에 Stacking등의 기법이 있다.
* <span style="color:red">대표적인 배깅은 랜덤 포레스트 알고리즘이 있으며, 부스팅은 에이다 부스팅, 그레디언트 부스팅, XGBoost, LightGBM등이 있다.</span> 정형 데이터의 분류나 회귀에서는 GBM부스팅 계열은 앙상블이 전반적으로 높은 예측 성능을 나타냅니다.
* 넓은 의미로는 서로 다른 모델을 결합한 것들을 앙상블로 지칭하기도 한다.



### 앙상블의 특징

* 단일 모델의 약점을 다수의 모델을 결합하여 보완
* 뛰어난 성능을 가진 모델들로만 구성하는 것보다 성능이 떨어지더라도 서로 다른 유형의 모델을 섞는 것이 오히려 전체 성능이 도움이 될 수 있음.
* 랜덤 포레스트 및 뛰어난 부스팅 알고리즘들은 모두 결정 트리 알고리즘을 기반 알고리즘으로 적용
* 결정트리의 단점이 과적합(오버 피팅)을 수십~ 수천개의 많은 분류기를 결합해 보완하고 장점인 직관적인 분류기준은 강화됨

### 보팅과 배깅 개요

* 보팅과 배깅은 여러 개의 분류기를 투포를 통해 최종 예측 결과를 결정하는 방식

* 보팅과 배깅의 다른 점은 보팅의 경우, 일반적으로 서로 다른 알고리즘을 가진 분류기를 결합하는 것이고, 배깅의 경우 각각의 분류기가 모두 같은 유형의 알고리즘 기반이지만, 데이터 샘플링을 서로 다르게 가져가면서 학습을 수행해 보팅을 수행하는 방식

  ![Voting](https://user-images.githubusercontent.com/70785000/120695994-fbbe3180-c4e6-11eb-91ff-de4963529059.PNG)

![bagging](https://user-images.githubusercontent.com/70785000/120695960-ee08ac00-c4e6-11eb-8d11-f16d8bdd9d42.PNG)

### 보팅유형 - 하드보팅(Hard Voring )과 소프트보팅(Soft Voting)

#### Hard Voting

Hard Voting은 다수의 classifier간 다수결로 최종 class결정 

![hard voting](https://user-images.githubusercontent.com/70785000/120695973-f19c3300-c4e6-11eb-8f6a-8cf0e2dc2183.PNG)

#### Soft Voting

다수의 Classifier들의 class확률을 평균하여 결정

predict_proba()메소드를 이용하여 class별 확률 결정.

![soft_voting](https://user-images.githubusercontent.com/70785000/120695982-f4972380-c4e6-11eb-9925-f6d6c9a368e4.PNG)

* 일반적으로 하드 보팅보다는 소프트 보팅이 예측 성능이 상대적으로 우수하여 주로 사용됨.

* 사이킷런은 VotingClassifier클래스를 통해 Voting을 지원




### 배깅(Bagging) - 랜덤 포레스트(Random Forest)

* 배깅의 대표적인 알고리즘은 렌덤 포레스트

* 랜덤 포레스트는  다재 다능한 알고리즘으로, 앙상블 알고리즘 중에서 비교적 빠른 수행속도를 가지고 있으며, 다양한 영역에서 높은 예측 성능을 보임

* 랜덤 포레스트는 여러 개의 결정 트리 분류기가 전체 데이터에서 배깅 방식으로 각자의 데이터를 샘플링해 개별적으로 학습을 수행한 뒤 최종적으로 모든 분류기가 보팅을 통해 예측 결정을 하게 된다.

  ![random_forest](https://user-images.githubusercontent.com/70785000/120705701-1f877480-c4f3-11eb-9fb5-f6c112d433fe.PNG)

### 랜덤 포레스트의 부트 스트래핑 분할

* 랜덤 포레스트는 개별적인 분류기의 기반 알고리즘은 결정 트리이지만 개별 트리가 학습하는 데이터세트는 전체 데이터에서 일부가 중첩되게 샘플링된 데이터세트. 이렇게 여러 개의 데이터 세트를 중첩되게 분리하는 것을 부트 스트래핑(bootstrapping)분할 방식이라고 합니다(그래서 배깅(Bagging)이 bootsrap aggregation의 줄임말입니다).

* 부트스트래핑 - 평균의 신뢰도를 구하기 위해 통계학에서 데이터를 샘플링하는 방식.

  평균이 실제값과 비교했을때 편차가 있기 때문에 평균의 신뢰도를 구하기 위해 데이터를 여러번 추출한 값들을 평균을 내게 되는데 결국의 이 평균의 분포는 정규분포를 가지게 된다. 그래서 신뢰도 구간을 구할수 있다.

* 원본 데이터의 건수가 10개인 학습 데이터 세트에 랜덤 포레스트를 3개의 결정 트리 기반으로 학습하려고 n_estimators=3으로 하이퍼 파라미터를 부여하면 다음과 같이 데이터 서브세트가 만들어집니다.(중복이 됨을 유의)

![bootstraping](https://user-images.githubusercontent.com/70785000/120709015-4a73c780-c4f7-11eb-9af3-8cdfd19e6d30.PNG)

### 사이킷런의 랜덤 포레스트 하이퍼 파라미터

 사이킷런은 랜덤 포레스트 분류를 위해 <span style="color:red">RandomForestClassifier클래스</span>를 제공

* n_estimators : 결정트리의 개수를 지정. 디폴트는 10

  많이 설정할 수록 좋은 성능을 기대할 수 있지만, 계속 증가시킨다고 해서 성능이 무조건 향상되는 것은 아니며 늘릴수록 학습수행시간이 오래 걸린다는 것을 유의.

* **`max_features`** : 결정트리에 사용되는 `max_features`파라미터와 동일. 하지만 RandomForestClassifier의 기본 `max_features`는 `None`이 아니라 `auto`, 즉 `sqrt`(제곱근)과 같다.

  따라서 랜덤포레스트의 트리를 분할하는 피처를 참조할때 전체 피처가 아니라 `sqrt(전체 피처개수)`만큼 참조합니다.(전체 피처가 16개라면 분할을 위해 4개를 참조)

* **`max_depth`**나 **`min_sample_leaf`**와 같이 결정 트리에서 과적합을 개선하기 위해 사용되는 파라미터가 랜덤 포레스트에도 똑같이 적용 될 수 있습니다.



### 부스팅(Boosting)

* 부스팅 알고리즘은 여러 개의 약한 학습기(weak learner)를 순차적으로 학습-예측하면서 잘못 예측한 데이터에 가중치 부여를 통해 오류를 개선해 나가면서 학습하는 방식
* 부스팅의 대표적인 구현은 AdaBoost(Adaptive Boosting)와 Gradient Boost가 있다.
* 성능은 좋지만, 수행시간이 오래걸린다. 왜냐하면 약한 학습기를 순차적으로 학습하는데 ,데이터를 읽고 데이터에 대해서 잘못 예측한 데이터에 대해서 가중치를 부여하고 그 다음에 다른 학습기가 또 그 데이터를 학습을 진행한다. 

아래 그림은 에이다 부스트 알고리즘의 학습방법을 도식화 한것이다.

![AdaBoost](https://user-images.githubusercontent.com/70785000/120868566-47e4a100-c5cf-11eb-911a-9a59e9d6c969.PNG)

* step1 - 첫번째 약한 학습기 분류기준1로 `+` 와 `-`로 분류한 결과 동그라미로 표시된 `+`데이터가 잘못 분류된 오류 데이터

* step2 - 이 오류 데이터에 대해 가중치 부여하여 다음 학습기가 잘 분류할 수 있도록 크기가 커짐

* step3 - 두번째 약한 학습분류기가 분류기준 2로 분류한 결과 동그라미로 표시된 `-`데이터가 잘못 분류된 오류 데이터

* step4 - 이 오류 데이터에 대해 가중치 부여하여 다음 학습기가 잘 분류할 수 있도록 크기가 커짐

* step5 - 세번째 약한 학습기가 분류기준3으로 분류한 결과 `+`와 `-`를 분류하고 오류 데이터를 찾습니다.이렇게 AdaBoost는 약한 학습기가 순차적으로 오류 값에 대해서 가중치를 부여한 예측 결정 기준을 모두 결합해 예측 을 수행

* 마지막은 개별 학습기를 모두 결합한 예측결과이며, 정확도가 높아졌음을 알수 있다.

  

### GBM(Gradient Boost Machine)개요

GBM도 Ada Boost와 유사하나, 가중치 업데이트를 경사 하강법(Gradient Boost)를 이용하는 것이 가장 큰 차이입니다. 오류값은 **`실제값 - 예측값`**입니다. 분류의 실제 결과값을 y, 피처를 X1,X2,...Xn 그리고 이 피처에 기반한 예측 함수를 F(x)함수라고 하면 오류식 `h(x) = y - F(x)`이 됩니다. 이 오류식 `h(x) = y - F(x)`를 최소화하는 방향성을 가지고 반복적으로 가중치 값을 업데이트 하는 것이 경사하강법.

#### 사이킷런 GBM주요 하이퍼 파라미터 및 튜닝

**사이킷런은 GBM분류를 위해 `GradientBoostingClassifier`클래스를 제공**

* loss - 경사하강법에 사용할 비용함수를 지정.특별한 이유가 없으면 기본값이 `deviance`를 사용

* learning_rate : GBM이 학습을 진행할 때 마다 적용하는 학습률입니다. Weak learner가 순차적으로 오류값을 보정해 나가는데 적용한느 계수. `0 ~ 1`사이의 값을 지정가능하며 기본값은 `0.1`이다.

  너무 작은 값을 적용하면, 업데이트 되는 값이 작아져서 최소 오류값을 찾을 가능성이 높아지지만, 많은 약한 학습기가 순차적으로 반복이 필요해서 수행시간이 오래 걸리고 , 또 너무 작게 설정하는 경우는 weak learner의 반복이 완료되도 최소 오류값을 찾지 못할 수 있다. 반대로 큰 값을 적용하면 최소 오류값을 찾지 못하고 그냥 지나쳐 버려 예측 성능이 떨어질 가능성이 높아지지만, 빠른 수행이 가능하다.

* `n_estimators`: 약한 학습기의 갯수. 약한 학습기(weak learner)가 순차적으로 비율을 보정하므로 개수가 많을수록 예측성능이 일정 수준까지는 좋아질 수 있지만, 갯수가 많을수록 수행 시간이 오래 걸린다.

  기본값은 `100`.

* `subsample` : weak learner가 학습에 사용하는 데이터의 샘플링 비율. 기본값은 `1`이며, 이는 전체 학습 데이터를 기반으로 학습한다는 의미(`0.5`이면 학습 데이터의 `50%`), 과적합이 염려되는 경우 subsample를 1보다 작은값으로 설정.

  

## XGBoost개요

* 규제(Regularization)기능은 오차 오류만을 지속적으로 줄여나가기만 하면 overfitting이 생기게 마련이기 때문에 이런 부분때문에 규제기능이 필요(일반 GBM에는 없음)
* 가지치기 : 일단 노드를 다 생성 후에 다시 한번 검증을 하는데 해당 트리들이 제대로 역할을 하는지 노드들로부터 검증을 하고 , 필요없으면 제거.
* 조기중단 : 원래 정해진 n_estimators갯수 만큼 루프를 수행하면서 오류를 감소해야 하는데, 더 이상 오류를 감소하는 것이 특정 인터벌 동안 나오지 않는다면  , 더 이상 오류를 감소하는 루프를 수행하지 않고 중단

![XGBoost](https://user-images.githubusercontent.com/70785000/120875360-6f933380-c5e6-11eb-9a71-43f5c5e199c0.PNG)

#### XGBBoost구현

![XGBoost_구현](https://user-images.githubusercontent.com/70785000/120875506-255e8200-c5e7-11eb-9cf0-675d14fa1dbb.PNG)

#### XGBoost파이썬 래퍼와 사이킷런 래버 API비교

| 항목                               | 파이썬 Wrapper                                               | 사이킷런 Wrapper                             |
| ---------------------------------- | ------------------------------------------------------------ | -------------------------------------------- |
| 사용모듈                           | `from xgboost as xgb`                                        | `from xgboost import XGBClassifer`           |
| 학습용과 테스트용 <br/>데이터 세트 | `DMatrix객체`를 별도 생성<br />`train=xgb.DMatrix(data=X_train, label=y_train)`<br />`DMatrix생성자`로 피처 데이터세트와 레이블 데이터세트를 입력 | 넘파이나 판다스를 이용                       |
| 학습 API                           | `xgb_model = xgb.train()`<br />`xgb_model `은 학습된 객체를 반환 받음 | XGBClassifier.fit()                          |
| 예측 API                           | `xgb.trian()`으로 학습된 객체에서 `predict()`호출.<br />즉 `xgb_model.predict() `이때 반환결과는 예측 결과가 아니라 예측결과를 추정하는 확률값 반환 | XGBClassifier.predict()<br />예측결과값 반환 |
| 피처 중요도 시각화                 | `plot_importance()`함수 이용                                 | `plot_importance()`함수 이용                 |

#### XGBoost파이썬 래퍼와 사이킷런 레퍼 하이퍼 파라미터 비교

| 파이썬 Wrapper     | 사이킷런 Wrapper   | 하이퍼 파라미터 설명                                         |
| ------------------ | ------------------ | ------------------------------------------------------------ |
| `eta`              | `learning_rate`    | GBM의 학습률(`learning rate`)과 같은 파라미터<br />`0`에서 `1`사이의 값을 지정하며 부스팅 스텝을 반복적으로 수행시 업데이트되는 학습률 값<br />파이썬 래퍼 기반의 `xgboost`를 이용할 경우 디폴트는 `0.3`<br />사이킷런 래퍼 클래스를 이용할 경우 `eta`는 `learning rate`파라미터로 대체되며, 디폴트는 `0.1`이다.<br />과적합 제어를 위애 `eta`값을 낮출 경우, `num_rounds`혹은 `n_estimators`높여주어야 함. |
| `num_boost_rounds` | `n_estimators`     | 사이킷런 앙상블의 `n_estimators`와 동일.약한 학습기의 개수(반복 수행 횟수) |
| `min_child_weight` | `min_child_weight` | 결정 트리의 `min_child_leaf`와 유사.과적합 조절용<br />`min_child_weight`값이 특정값을 넘으면 `child`를 만들지 여부<br />해당 값을 높힘으로써 과적합 제어 가능 |
| `max_depth`        | `max_depth`        | 결정트리의 `max_depth`와 동일.트리의 최대 깊이               |
| `sub_sample`       | `subsample`        | `GBM`의 `subsample`과 동일. 트리가 커져서 과적합되는 것을 제어하기 위해 데이터를 샘플링하는 비율을 지정<br />`sub_sample=0.5`로 지정하면 전체 데이터의 절반을 트리 생성하는데 사용<br />`0`에서 `1`사이의 값이 가능하나 일반적으로 `0.5 ~ 1`사이의 값을 사용 |
| `lambda`           | `reg_lambda`       | 오차를 줄이기 위해 계속 학습을 하다보면,학습에만 몰두해서 실제로 검증 및 테스트 데이터세트에 사용될때 오류가 발생할 가능성이 많다.<br />그래서 오차에 집중하지 않기 위해 제약을 줄 파라미터가 필요.<br /> - `L2규제` .기본값은 1이고 값이 클수록 규제 값이 커짐(과적합제어) |
| `alpha`            | `reg_alpha`        | `L1규제`.기본값이 0이고 값이 클수록 규제값이 커집(과적합 제어) |
| `colsample_bytree` | `colsample_bytree` | 트리 생성시 필요한 피처(컬럼)을 어느 정도의 비율로 샘플링하는 할 것인가?<br />매우 많은 피처가 있는 경우, 과적합을 조정하는데 사용<br />`GBM`의 `max_features`와 유사. |
| `scale_pos_weight` | `scale_pos_weight` | 특정값으로 치우친 비대칭한 클래스로 구성된 데이터세트의 균형을 유지 하기 위한 파라미터.기본값은 1<br />eg) 신용카드 사용금액의 정상 및 사기 판별 |
| `gamma`            | `gamma`            | 트리의 리프노드를 추가적으로 나눌지를 결정하는 최소 손실 값<br />손실을 계속 줄여야 하는데 어느 정도 이상으로 손실이 줄지 않으면 tree의 leafnode를 추가적으로 분할하지 않는것.<br />`gamma`값을 높힘으로써 과적합을 제어. |

사이킷런 Wrapper의 경우 GBM에 동일한 하이퍼 파라미터가 있다면 이를 사용하고 그렇지 않다면 파이썬 Wrapper의 하이퍼 파라미터를 사용

####  XGBoost하이퍼 파라미터 (학습태스크)

| 항목          | 학습 태스크 파라미터 설명                                    |
| ------------- | ------------------------------------------------------------ |
| `objective`   | 최솟값을 가져야 할 손실 함수를 정의합니다. `XGBoost`는 많은 유형의 손실함수를 사용 할 수 있는데 주로 사용되는 손실함수는 이진분류인지 다중 분류인지에 따라 달라짐.<br />* `bianry : logstic`이진분류일때 사용<br />* `multi:softmax` : 다중 분류일때 적용하며, 레이블 클래스의 갯수인 `num_class`파라미터를 지정해야 함.<br />- `multi:softprob` : `multi:softmax`와 유사하나 개별 레이블 클래스의 해다오디는 예측 확률을 반환 |
| `eval_metric` | 검증에 사용되는 함수를 정의.<br />기본값이 회귀인 경우는 `mse(mean squared error)`<br />분류인 경우엔 `error`<br />- `rsme - Root Mean Squared Error`<br />- `logloss` :  `Negative log-likelihood`<br />-`error` : `Binary classification error rate`<br />- `merror`: `Multiclass classification error rate`<br />- `mlogloss : Multiclass logloss`<br />- `AUC - Area under the curve` |



#### `XGBoost` 조기 중단(`Early Stopping`)

* XGBoost는 특정 반복 횟수만큼 더 이상 비용함수가 감소하지 않으면 지정된 반복 횟수를 다 완료하지 않고 수행을 종료할 수 있음.
* 학습을 위한 시간을 단축 시킬수있음 (최적화 튜닝단계에 적절히 사용가능)
* 너무 반복횟수를 단축시, 예측 성능 최적화가 안된 상태에서 학습이 종료될 수 있음에 유의
* 조기 중단을 위하 주요 파라미터
  - `early_stopping_rounds` : 더 이상 비용 평가 지표가 감소하지 않는 최대 반복 횟수
  - `eval_metric` : 반복 수행시 사용하는 비용 평가지표
  - `eval_set`:평가를 수행하는 별도의 검증 데이터 세트.일반적으로 검증 데이터세트에서 반복적으로 비용 감소 성능 평가

![earlystopping](https://user-images.githubusercontent.com/70785000/120884525-99684c80-c61e-11eb-956c-19b89d9745fe.PNG)

### XGBoost설치

`아나콘다 환경`에서 설치가 가능.

- `windows`환경 - `conda install -c anaconda py-xgboost
- `linux환경` - ` conda install -c conda-forge xgboost

### LightGBM개요

* 기존 XGBoost의 단점을 개선하여 더 빠른 학습과 예측 수행시간
* 더 작은 메모리 사용량(GPU지원)
* 카테고리형 피처의 자동 변환과 최적 분할(원-핫 인코딩 등을 사용하지 않고도 카테고리형 피처를 최종적으로 변환하고 이에 따른 노드 분할 수행)

#### LightGBM 트리 분할 방식 - 리프 중심

![node_split](https://user-images.githubusercontent.com/70785000/121548747-3fb1b900-ca48-11eb-8142-2908da0ab399.PNG)

#### LightGBM파이썬 구현

![LGBM](https://user-images.githubusercontent.com/70785000/121548998-6f60c100-ca48-11eb-850d-5672250ebbbb.PNG)

#### LightGBM 하이퍼 파라미터 

| 유형       | 파이썬 래퍼 LightGBM      | 사이킷런 래퍼 LightGBM |                                                              |
| ---------- | ------------------------- | ---------------------- | ------------------------------------------------------------ |
| 파라미터명 | `num_iterations`          | `n_estimators`         | 약한 학습기의 갯수(반복 수행 횟수)                           |
|            | `learning_rate`           | `learning_rate`        | 학습률(`learning_rate`).<br />`0`에서 `1`사이의 값을 기정하여 부스팅 스텝을 반복적으로 수행할 때 업데이트되는 학습률 값 |
|            | `max_depth`               | `max_depth`            | 결정트리의 `max_depth`와 동일.트리의 최대 깊이               |
|            | `min_data_in_leaf`        | `min_child_samples`    | 리프노드가 될 수 있는 최소 데이터 건수(`Sample수`)           |
|            | `bagging_fraction`        | `subsample`            | 트리가 커져서 과적합되는 것을 제어하기 위해 데이터를 샘플링하는 비율을 지정합니다. <br />`sub_sample=0.5`로 지정하면 전체 데이터의 절반을 트리를 생성하는데 사용합니다. |
|            | `feature_fraction`        | `colsample_bytree`     | `GBM`의 `max_features`와 유사합니다. 트리 생성에 필요한 피처(컬럼)을 임의로 샘플링하는데 사용됩니다.<br />매우 많은 피처가 있는 경우 과적합을 조정하는데 적용. |
|            | `lambda_l2`               | `reg_lambda`           | `L2규제(Regulation)`적용 값. 기본값은 `1`<br />값이 클수록 규제값이 커짐(과적합 제어) |
|            | `lambda_l1`               | `reg_alpha`            | `L1규제(Regulation)`적용 값. 기본값은 `0`<br />값이 클수록 규제값이 커짐(과적합 제어) |
|            | `early_stopping_round`    | `early_stopping_round` | 학습 조기 종료을 위한 `early stopping interval`값            |
|            | `num_leaves`              | `num_leaves`           | 최대 리프 노드 갯수                                          |
|            | `min_sum_hessian_in_leaf` | `min_child_weight`     | 결정트리의 `min_child_leaf`와 유사.<br />과적합 조절용       |

* `LightGBM사이킷런 래퍼`는 `XGBoost 사이킷런 래퍼`에 해당 하이터 파라미터가 있으면 이를 그대로 사용하고, 그렇지 않으면 `파이썬 래퍼 LightGBM 하이퍼 파라미터`를 사용.
* `num_leaves`의 갯수를 중심으로 `min_child_samples(min_data_in_leaf), max_depth`를 함께 조정하면서 모델의 복잡도를 줄이는 것이 기본 튜닝 방안

#### 파이썬 래퍼와 사이킷런 래퍼 하이퍼 파라미터 비교

사이킷런 래퍼 XGBoost를 기준으로 다른 결정분류기가 파라미터를 따라간다는 것을 유념.

| 유형       | 파이썬 래퍼 LightGBM      | 사이킷런 래퍼 LightGBM  | 사이킷런 래퍼 XGBoost   |
| ---------- | ------------------------- | ----------------------- | ----------------------- |
| 파라미터명 | `num_iterations`          | `n_estimators`          | `n_estimators`          |
|            | `learning_rate`           | `learning_rate`         | `learning_rate`         |
|            | `max_depth`               | `max_depth`             | `max_depth`             |
|            | `min_data_in_leaf`        | `min_child_samples`     | `N/A`                   |
|            | `bagging_fraction`        | `subsample`             | `subsample`             |
|            | `feature_fraction`        | `colsample_bytree`      | `colsample_bytree`      |
|            | `lambda_l2`               | `reg_lambda`            | `reg_lambda`            |
|            | `lambda_l1`               | `reg_alpha`             | `reg_alpha`             |
|            | `early_stopping_round`    | `early_stopping_rounds` | `early_stopping_rounds` |
|            | `num_leaves`              | `num_leaves`            | `N/A`                   |
|            | `min_sum_hessian_in_leaf` | `min_child_weight`      | `min_child_weight`      |

### Feature Engineering 

#### Log변환

- Log변환은 왜곡된 분포도를 가진 데이터세트를 비교적 정규분포에 가깝게 변환해주는 훌륭한 `Feature Engineering`방식

#### IQR(Inter Quantile Range)를 이용한 Outlier Removal

![iqr](https://user-images.githubusercontent.com/70785000/121657596-80a6dd80-cadb-11eb-8a29-d25d87d54ab2.PNG)

![boxplot](https://user-images.githubusercontent.com/70785000/121657585-7e448380-cadb-11eb-9acd-32ca67b6872a.PNG)

#### 언더샘플링과 오버 샘플링

- 레이블이 뷸균형한 분포를 가진 데이터 세트를 학습 시, 이상 레이블을 가지는 데이터 건수가 매우 적어 제대로 된 유형의 학습이 어려움.

- 반면에 정상 레이블을 가지는 데이터 건수는 매우 많아 일방적으로 정상 레이블로 치우친 학습을 수행하며, 제대로 된 이상 데이터 검출이 어려움

- 대표적으로 오버샘플링과 언더 샘플링 방법을 통해 적절한 학습 데이터를 확보함

- 짙은 회색의 사각형 (이상 데이터) , 옅은 회색의 사각형(정상 데이터)

  ![under_sampling](https://user-images.githubusercontent.com/70785000/121748493-0d858180-cb44-11eb-9b07-d4c93f3a891f.PNG)

![over_sampling](https://user-images.githubusercontent.com/70785000/121748535-1e35f780-cb44-11eb-9469-67762db62f2d.PNG)

#### SMOTE

![smote](https://user-images.githubusercontent.com/70785000/121750037-943b5e00-cb46-11eb-86c3-7d054deedc97.PNG)

1)원본데이터의 `이상 데이터(녹색의 원)`를 2) KNN최근접 기법을이용해 이웃을 정하고 이웃과 이웃 사이에 있는 공간에 무작위 값(여기서는 빨간색의 원) 데이터를 증식시켜 3)오버 샘플링을 완성시키는 방법

* [관련 이미지 참조](https://john-analyst.medium.com/)
* [imbalanced learn](https://imbalanced-learn.org/stable/)
* 설치 : `conda install -c conda-forge imbalanced-learn`



