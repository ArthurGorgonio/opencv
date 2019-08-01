from classifiers import choose_model
from sklearn.ensemble import AdaBoostClassifier as boosting
from sklearn.ensemble import BaggingClassifier as bagging


def runBagging(X_train, y_train, X_test, num, n_estimator):
    model = choose_model(num)
    bg = bagging(model, n_estimators=n_estimator)
    bg.fit(X_train, y_train)

    return bg.predict(X_test)


def score(X_test, y_test):
    return bagging.score(X_test, y_test)
