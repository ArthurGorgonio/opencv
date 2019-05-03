import classifiers
import preprocessing
import utils


def main():
    acc = sd = []
    data = preprocessing.readData()
    samples, targets = preprocessing.splitSamples(data)
    kfold = preprocessing.crossValidation(10)

    for train, test in kfold.split(samples, targets):
        X_train, X_test = samples[train], samples[test]
        y_train, y_test = targets[train], targets[test]

        for i in range(88):
            y_pred = classifiers.classify(X_train, y_train, X_test, i)
            fold_acc, fold_sd = classifiers.mensureAcc(y_pred, y_test)
            acc.append(fold_acc)
            sd.append(fold_sd)

    result_acc = result_sd = [[0 for x in range(10)] for x in range(88)]

    for j in range(88):
        for k in range(10):
            result_acc[j][k] = acc[j * 10 + k]
            result_sd[j][k] = sd[j * 10 + k]
    utils.writeCSV("accuracy.csv", result_acc)
    utils.writeCSV("sd.csv", result_sd)
    print("Finish!!\n")
