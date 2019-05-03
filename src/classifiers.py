# from sklearn.ensemble import RandomForestClassifier as rf
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.naive_bayes import BernoulliNB as naive
from sklearn.naive_bayes import GaussianNB as gaussian_naive
from sklearn.neighbors import KNeighborsClassifier as knn_vote
from sklearn.tree import DecisionTreeClassifier as tree


def classifiers(number):
    classify = [
        knn_vote(n_neighbors=1, weights='distance', p=1, metric="euclidean"),
        knn_vote(n_neighbors=2, weights='distance', p=1, metric="euclidean"),
        knn_vote(n_neighbors=3, weights='distance', p=1, metric="euclidean"),
        knn_vote(n_neighbors=4, weights='distance', p=1, metric="euclidean"),
        knn_vote(n_neighbors=5, weights='distance', p=1, metric="euclidean"),
        knn_vote(n_neighbors=6, weights='distance', p=1, metric="euclidean"),
        knn_vote(n_neighbors=7, weights='distance', p=1, metric="euclidean"),
        knn_vote(n_neighbors=1, weights='uniform', p=1, metric="euclidean"),
        knn_vote(n_neighbors=2, weights='uniform', p=1, metric="euclidean"),
        knn_vote(n_neighbors=3, weights='uniform', p=1, metric="euclidean"),
        knn_vote(n_neighbors=4, weights='uniform', p=1, metric="euclidean"),
        knn_vote(n_neighbors=5, weights='uniform', p=1, metric="euclidean"),
        knn_vote(n_neighbors=6, weights='uniform', p=1, metric="euclidean"),
        knn_vote(n_neighbors=7, weights='uniform', p=1, metric="euclidean"),
        knn_vote(n_neighbors=1, weights='distance', p=2, metric="euclidean"),
        knn_vote(n_neighbors=2, weights='distance', p=2, metric="euclidean"),
        knn_vote(n_neighbors=3, weights='distance', p=2, metric="euclidean"),
        knn_vote(n_neighbors=4, weights='distance', p=2, metric="euclidean"),
        knn_vote(n_neighbors=5, weights='distance', p=2, metric="euclidean"),
        knn_vote(n_neighbors=6, weights='distance', p=2, metric="euclidean"),
        knn_vote(n_neighbors=7, weights='distance', p=2, metric="euclidean"),
        knn_vote(n_neighbors=1, weights='uniform', p=2, metric="euclidean"),
        knn_vote(n_neighbors=2, weights='uniform', p=2, metric="euclidean"),
        knn_vote(n_neighbors=3, weights='uniform', p=2, metric="euclidean"),
        knn_vote(n_neighbors=4, weights='uniform', p=2, metric="euclidean"),
        knn_vote(n_neighbors=5, weights='uniform', p=2, metric="euclidean"),
        knn_vote(n_neighbors=6, weights='uniform', p=2, metric="euclidean"),
        knn_vote(n_neighbors=7, weights='uniform', p=2, metric="euclidean"),
        knn_vote(n_neighbors=1, weights='distance', p=1, metric="chebyshev"),
        knn_vote(n_neighbors=2, weights='distance', p=1, metric="chebyshev"),
        knn_vote(n_neighbors=3, weights='distance', p=1, metric="chebyshev"),
        knn_vote(n_neighbors=4, weights='distance', p=1, metric="chebyshev"),
        knn_vote(n_neighbors=5, weights='distance', p=1, metric="chebyshev"),
        knn_vote(n_neighbors=6, weights='distance', p=1, metric="chebyshev"),
        knn_vote(n_neighbors=7, weights='distance', p=1, metric="chebyshev"),
        knn_vote(n_neighbors=1, weights='uniform', p=1, metric="chebyshev"),
        knn_vote(n_neighbors=2, weights='uniform', p=1, metric="chebyshev"),
        knn_vote(n_neighbors=3, weights='uniform', p=1, metric="chebyshev"),
        knn_vote(n_neighbors=4, weights='uniform', p=1, metric="chebyshev"),
        knn_vote(n_neighbors=5, weights='uniform', p=1, metric="chebyshev"),
        knn_vote(n_neighbors=6, weights='uniform', p=1, metric="chebyshev"),
        knn_vote(n_neighbors=7, weights='uniform', p=1, metric="chebyshev"),
        knn_vote(n_neighbors=1, weights='distance', p=2, metric="chebyshev"),
        knn_vote(n_neighbors=2, weights='distance', p=2, metric="chebyshev"),
        knn_vote(n_neighbors=3, weights='distance', p=2, metric="chebyshev"),
        knn_vote(n_neighbors=4, weights='distance', p=2, metric="chebyshev"),
        knn_vote(n_neighbors=5, weights='distance', p=2, metric="chebyshev"),
        knn_vote(n_neighbors=6, weights='distance', p=2, metric="chebyshev"),
        knn_vote(n_neighbors=7, weights='distance', p=2, metric="chebyshev"),
        knn_vote(n_neighbors=1, weights='uniform', p=2, metric="chebyshev"),
        knn_vote(n_neighbors=2, weights='uniform', p=2, metric="chebyshev"),
        knn_vote(n_neighbors=3, weights='uniform', p=2, metric="chebyshev"),
        knn_vote(n_neighbors=4, weights='uniform', p=2, metric="chebyshev"),
        knn_vote(n_neighbors=5, weights='uniform', p=2, metric="chebyshev"),
        knn_vote(n_neighbors=6, weights='uniform', p=2, metric="chebyshev"),
        knn_vote(n_neighbors=7, weights='uniform', p=2, metric="chebyshev"),
        knn_vote(n_neighbors=1, weights='distance', p=1, metric="manhattan"),
        knn_vote(n_neighbors=2, weights='distance', p=1, metric="manhattan"),
        knn_vote(n_neighbors=3, weights='distance', p=1, metric="manhattan"),
        knn_vote(n_neighbors=4, weights='distance', p=1, metric="manhattan"),
        knn_vote(n_neighbors=5, weights='distance', p=1, metric="manhattan"),
        knn_vote(n_neighbors=6, weights='distance', p=1, metric="manhattan"),
        knn_vote(n_neighbors=7, weights='distance', p=1, metric="manhattan"),
        knn_vote(n_neighbors=1, weights='uniform', p=1, metric="manhattan"),
        knn_vote(n_neighbors=2, weights='uniform', p=1, metric="manhattan"),
        knn_vote(n_neighbors=3, weights='uniform', p=1, metric="manhattan"),
        knn_vote(n_neighbors=4, weights='uniform', p=1, metric="manhattan"),
        knn_vote(n_neighbors=5, weights='uniform', p=1, metric="manhattan"),
        knn_vote(n_neighbors=6, weights='uniform', p=1, metric="manhattan"),
        knn_vote(n_neighbors=7, weights='uniform', p=1, metric="manhattan"),
        knn_vote(n_neighbors=1, weights='distance', p=2, metric="manhattan"),
        knn_vote(n_neighbors=2, weights='distance', p=2, metric="manhattan"),
        knn_vote(n_neighbors=3, weights='distance', p=2, metric="manhattan"),
        knn_vote(n_neighbors=4, weights='distance', p=2, metric="manhattan"),
        knn_vote(n_neighbors=5, weights='distance', p=2, metric="manhattan"),
        knn_vote(n_neighbors=6, weights='distance', p=2, metric="manhattan"),
        knn_vote(n_neighbors=7, weights='distance', p=2, metric="manhattan"),
        knn_vote(n_neighbors=1, weights='uniform', p=2, metric="manhattan"),
        knn_vote(n_neighbors=2, weights='uniform', p=2, metric="manhattan"),
        knn_vote(n_neighbors=3, weights='uniform', p=2, metric="manhattan"),
        knn_vote(n_neighbors=4, weights='uniform', p=2, metric="manhattan"),
        knn_vote(n_neighbors=5, weights='uniform', p=2, metric="manhattan"),
        knn_vote(n_neighbors=6, weights='uniform', p=2, metric="manhattan"),
        knn_vote(n_neighbors=7, weights='uniform', p=2, metric="manhattan"),
        naive(),
        gaussian_naive(),
        tree(criterion="gini"),
        tree(criterion="entropy")
    ]

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
