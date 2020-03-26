import preprocessing
from numpy.random import seed
from sklearn.cluster import AgglomerativeClustering as hierarchical
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score as cr
from sklearn.metrics import davies_bouldin_score as db
from sklearn.metrics import silhouette_score
from sklearn.mixture import GaussianMixture as em
from utils import writeCSV


def scoreSil(X_test, cluster_labels):
    return silhouette_score(X_test, cluster_labels)


def scoreDB(X_test, cluster_labels):
    return db(X_test, cluster_labels)


def scoreCR(y_test, cluster_labels):
    return cr(cluster_labels, y_test)


def main():
    data = preprocessing.readData()
    sil_values_ag1 = []
    db_values_ag2 = []
    cr_values_ag3 = []

    for i in range(2, 22):
        # Hierarquico
        hier = hierarchical(n_clusters=i, linkage='complete').fit(data)
        sil_values_ag1.append(scoreSil(data, hier.labels_))
        db_values_ag2.append(scoreDB(data, hier.labels_))
        # cr_values_ag3.append(scoreCR(targets, hier.labels_))
    writeCSV("sil_all.csv", sil_values_ag)
    writeCSV("db_all.csv", db_values_ag)
    writeCSV("cr_all.csv", cr_values_ag)
