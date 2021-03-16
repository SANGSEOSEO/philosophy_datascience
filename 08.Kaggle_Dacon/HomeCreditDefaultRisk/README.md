# 데이터 설명

* application_{trian|test}.csv
  * 현 대출정보로 부모테이블임(타겟정보는 없음)
  * 한 레코드가 하나의 대출신청에 대한 정보

* bureau.csv
  * 다른 금융기관으로 대출받은 정보
  * 하나의 SK_ID_CURR에 대해 여러개의 레코드가 존재
* bureau_balance.csv
  * 신청일 기준 잔액 정보
  * bureau.csv의 자식 테이블이라고 이해하는 것이 이해에 용이함.
* **POS_CASH_balance.csv**
  * 대출금 납부 현황

* **credit_card_balance.csv**
  * 신용카드 대출 정보
* **previous_application.csv**
  * 과거 대출 정보
* **installments_payments.csv**
  * 대출금 납입 정보

### 테이블 구조

![](https://storage.googleapis.com/kaggle-media/competitions/home-credit/home_credit.png)

