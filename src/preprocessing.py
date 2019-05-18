import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.model_selection import RepeatedStratifiedKFold, StratifiedKFold

# from sklearn.preprocessing import StandardScaler


def readData(dataset="./base.csv"):
    """Read a csv file and load into a variable with pandas package

        Parameters
        ----------
            dataset: {string}
                the csv file which be readed
    """
    data = pd.read_csv(dataset)

    return data


# Split data into train and test
def splitSamples(data):
    samples = data.iloc[:, 0:4095].values
    target = data.iloc[:, 4096].values

    return samples, target


# Spliting train ans test data
def crossValidation(k):
    try:
        return StratifiedKFold(n_splits=k)
    except ValueError:
        print("Please put a number > 2")


def repeatCrossValidation(folds, repeats):
    try:
        return RepeatedStratifiedKFold(n_splits=folds, n_repeats=repeats)
    except ValueError:
        print("A least 2 folds and repeats!")


# # Feature Scaling
# sc = StandardScaler()
# X_train = sc.fit_transform(X_train)
# X_test = sc.transform(X_test)


# Perform LDA
def LDAProcessing(samples, target, n_components=2048):
    lda = LDA(n_components=n_components)

    return lda.fit_transform(samples, target)
