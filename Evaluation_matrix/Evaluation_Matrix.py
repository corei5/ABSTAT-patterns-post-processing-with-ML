from sklearn import metrics

def evaluation_matrix(y_test, y_pred, target_names):
    print(metrics.classification_report(y_test, y_pred, target_names=target_names))
