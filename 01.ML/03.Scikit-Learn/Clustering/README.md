## 군집화(Clustering)

### 군집화의 이해

데이터 포인트들을 별개의 군집으로 그룹화 하는 것을 의미합니다.

유사성이 높은 데이터들을 동일한 그룹으로 분류하고 서로 다른 군집들이 상이성을 가지도록 그룹화합니다.

<img width="478" alt="cluster_img" src="https://user-images.githubusercontent.com/70785000/134755470-357e881d-5f5f-4d56-8f5e-baa6e9de1b58.png">

### 군집화 활용 분야

* 고객, 마켓, 브랜드 및 사회 경제 활동 등 전분야에 걸쳐서 세분화(Segmentation)
* Image검출, 세분화, 트랙킹
* 이상 검출(Abnormaly detection)

어떻게 유사성을 적용할 것인가?

### 군집화 알고리즘

* K-Means - Centroid기반의 알고리즘 가장 많이 활용
* Mean Shift - Centroid기반
* Gaussian Mixture Model - 데이터가 여러 개의 정규분포로 되어있고 가정하고, 이 데이터세트가 어느 정규분포에 속하는지에 따라 클러스터링 수행
* DBSCAN - 데이터의 밀도에 따라서 군집화를 수행하는 알고리즘

#### K-Means Clustering

군집중심점(Centroid)기반 클러스터링

![K평균군집_동작시각화](https://user-images.githubusercontent.com/70785000/133865224-74a2f128-ce8b-42f9-9709-cfb5b9ebbd9b.png)

#### 장점

* 일반적인 군집화에서 가장 많이 활용되는 알고리즘
* 알고리즘이 쉽고 간결
* 대용량 데이터에도 활용이 가능

#### 단점

* 거리 기반 알고리즘으로 속성의 갯수가 매우 많을 경우 군집화 정확도가 떨어집니다.(이를 위해 PCA로 차원 축소를 적용해야 할수도있음), 가까운 거리에 있는 데이터는 군집화가 되는 거리기반 알고리즘.
* 반복을 수행하는데, 반복 횟수가 많을 경우 수행 시간이 느려짐
* 이상치 데이터에 취약

### 사이킷런 KMean클래스

사이킷런 패키지는 K-평균을 구현하기 위해 KMeans클래스를 제공합니다. KMeans클래스는 다음과 같은 초기화 파라미터를 가지고있습니다.

> class sklearn.cluster.KMeans(n_clusters=8, init='k-means++', n_init=10, max_iter=300, tol=0.0001, precompute_distances='auto', verbose=0, random_state=None, copy_x=True, n_jobs=1, algorithm='auto')

`n_clusters` - 중심점갯수를 설정, 

#### 주요 파라미터

* KMeans초기화 파라미터 중 가장 중요한 파라미터는 `n_cluster`이며, 이는 군집화 개수 , 즉 준집 중심점 갯수를 의미
* `init`는 초기에 군집 중심점의 좌표를 설정할 방식을 말하며 보통은 임의로 중심을 설정하지 않고 일반적으로 `k-means++`방식으로 최초 설정
* `max_iter`는 최대 반복 횟수이며, 이 횟수 이전에 모든 데이터의 중심점이 이동이 없으면 종료합니다.

#### 주요 속성

* `labels_` : 각 데이터 포인트가 속한 군집 중심점 레이블
* `cluster_centers_`: 각 군집 중심점 좌표(Shape)는  `군집 갯수, 피처갯수` . 이를 이용하면 군집 중심점 좌표가 어디인지 시각화가 가능
