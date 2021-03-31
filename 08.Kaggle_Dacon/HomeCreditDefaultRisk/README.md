# 데이터세트 설명

* application_{trian|test}.csv
  * 현 대출정보로 부모테이블임(타겟정보는 없음)
  * 고객정보와 현 대출정보를 가지고있음
* PK: #SK_ID_CURR
  
* bureau.csv
  * 현 대출정보 이전, 타 금융기관으로 받은 대출정보
  * #SK_ID_CURR + #SK_ID_BUREAU
* bureau_balance.csv(타금융기관 대출 월별 잔액)
  * 타사 대출의 월별 채무 이행 이력
  * #SK_ID_BUREAU + #MONTHS_BALANCE
* **POS_CASH_balance.csv**
  * 월별 현금 대출현황, POS(Consumer loadn, 자동차 할부)

* **credit_card_balance.csv**
  * 신용카드 대출 정보
* **previous_application.csv**
  * 고객의 현재 대출이전 과거 대출정보 
  * #SK_ID_CURR + #SK_ID_PREV
* **installments_payments.csv**
  * 대출 채무 이행 이력

### 테이블 구조

![](https://storage.googleapis.com/kaggle-media/competitions/home-credit/home_credit.png)

