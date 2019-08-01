# from sklearn.ensemble import RandomForestClassifier as rf
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.naive_bayes import GaussianNB as naive
from sklearn.neighbors import KNeighborsClassifier as knn
from sklearn.neural_network import MLPClassifier as mlp
from sklearn.tree import DecisionTreeClassifier as tree


def select_classify():
    return [
        naive(),
        tree(criterion="entropy"),
        knn(n_neighbors=8, weights='uniform', metric="manhattan"),
        mlp(hidden_layer_sizes=(128, ),
            alpha=0.01,
            activation='tanh',
            solver='sgd',
            max_iter=300,
            learning_rate='constant',
            learning_rate_init=0.001)
    ]


def len_classify():
    return len(select_classify())


def choose_model(number):
    classifier = select_classify()

    return classifier[number]


# Classify
def classify(X_train, y_train, X_test, num):
    model = choose_model(num)
    model.fit(X_train, y_train)

    return model.predict(X_test)


# Scoring
def mensureAcc(y_pred, y_test):
    cm = confusion_matrix(y_test, y_pred)

    return (cm, str(accuracy_score(y_test, y_pred)))
