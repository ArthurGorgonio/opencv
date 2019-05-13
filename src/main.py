import classifiers
import preprocessing
import utils


def main():
    folds = 10
    n_classifiers = classifiers.len_classify()
    cm, acc = [], []
    result_cm, result_acc = [0] * folds, [0] * folds

    for i in range(folds):
        result_cm[i], result_acc[i] = [0] * n_classifiers, [0] * n_classifiers

    data = preprocessing.readData()
    samples, targets = preprocessing.splitSamples(data)
    kfold = preprocessing.crossValidation(folds)

    for train, test in kfold.split(samples, targets):
        X_train, X_test = samples[train], samples[test]
        y_train, y_test = targets[train], targets[test]

        for i in range(n_classifiers):
            y_pred = classifiers.classify(X_train, y_train, X_test, i)
            fold_cm, fold_acc = classifiers.mensureAcc(y_pred, y_test)
            cm.append(fold_cm)
            acc.append(fold_acc)

    for j in range(n_classifiers):
        for k in range(folds):
            result_cm[k][j] = cm[k * n_classifiers + j]
            result_acc[k][j] = acc[k * n_classifiers + j]
    utils.writeCSV("all_classifiers_confusion-matrix.csv", result_cm)
    utils.writeCSV("all_classifiers_accuracy.csv", result_acc)
    print("Finish!!\n")
