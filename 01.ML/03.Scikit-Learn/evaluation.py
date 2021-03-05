from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, f1_score, roc_auc_score
from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


def get_clf_eval(y_test, pred= None, pred_proba = None):
    """
    오차행렬, 정확도, 정밀도, 재현율을 리턴하는 함수
    정밀도와 재현율을 결합한 F1 스코어 추가
    ROC AUC커브 추가
    """
    confusion  = confusion_matrix(y_test, pred)
    accuracy = accuracy_score(y_test, pred)
    precision = precision_score(y_test, pred)
    recall = precision_score(y_test, pred)
    f1 = f1_score(y_test, pred)
    roc_score = roc_auc_score(y_test, pred_proba)
    print("오차 행렬")
    print(confusion)
    print("정확도 : {0:.4f}, 정밀도 : {1:.4f}, 재현율 : {2:.4f}, \
                F1 스코어 : {3:.4f}, FOC AUC값 : {4:.4f}".format(accuracy, precision, recall, f1, roc_score))



def precision_recall_curve_plot(y_test, pred_proba_c1):
    # threshold ndarray와 threshold에 따른 정밀도, 재현율 ndarray추출
    precisions, recalls, thresholds = precision_recall_curve(y_test, pred_proba_c1)

    # X축을 threshold값으로 ,Y축은 정밀도, 재현율값으로 각각 plot수행, 정밀도 점선으로 표시
    plt.figure(figsize = (8, 6))
    threshold_boundary = thresholds.shape[0]

    plt.plot(thresholds, precisions[0:threshold_boundary], linestyle = '-', label = '정밀도')
    plt.plot(thresholds, recalls[0:threshold_boundary], linestyle = 'dotted', label = '재현율')

    # threshold값 X축의 Scale을 0.1단위로 변경
    start, end = plt.xlim()
    plt.xticks(np.round(np.arange(start, end, 0.1), 2))
    plt.xlabel("Threshhold value")
    plt.ylabel("Precision and Recall value")
    plt.legend();plt.grid()
    plt.show()
