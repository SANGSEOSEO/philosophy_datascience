# mortgage.py
#
# Exercise 1.7
principal = 500000.00 # 대출금액
rate = 0.05 # 이자율
payment = 2684.11 # 매달 이자
total_paid = 0.0

while principal > 0:
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment
print("Total paid", np.round(total_paid,1))