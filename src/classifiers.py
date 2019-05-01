from sklearn.ensemble import RandomForestClassifier as rf
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.naive_bayes import BernoulliNB as naive
from sklearn.neighbors import KNeighborsClassifier as knn_vote
from sklearn.neighbors import RadiusNeighborsClassifier as knn_radius
from sklearn.neural_network import MLPClassifier as mlp
from sklearn.tree import DecisionTreeClassifier as tree


def classifiers(number):
    classify = [naive(), mlp(alpha=1.0), rf(max_depth=4, random_state=0)]

    return classify[number]


# Classify
def classify(X_train, y_train, X_test, num):
    model = classifiers(num)
    model.fit(X_train, y_train)

    return model.predict(X_test)


# Scoring
def mensureAcc(y_pred, y_test):
    cm = confusion_matrix(y_test, y_pred)

    return (cm, str(accuracy_score(y_test, y_pred)))
