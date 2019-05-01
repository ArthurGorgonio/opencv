import classifiers
import preprocessing


def __main__():
    acc = []
    data = preprocessing.readData()
    samples, targets = preprocessing.splitSamples(data)
    kfold = preprocessing.crossValidation(10)

    for train, test in kfold.split(samples, targets):
        X_train, X_test = samples[train], targets[test]
        y_train, y_test = samples[train], targets[test]

        for i in range(3):
            y_pred = classifiers.classify(X_train, y_train, X_test, i)
            acc.append(classifiers.mensureAcc(y_pred, y_test))
