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
    samples, targets = preprocessing.splitSamples(data)
    sil_values_ag = scoreSil(samples, targets)
    db_values_ag = scoreDB(samples, targets)
    cr_values_ag = scoreCR(samples, targets)
    # links = ['ward', 'complete', 'average', 'single']
    # sil_values_ag = [0] * 19
    # db_values_ag = [0] * 19
    # cr_values_ag = [0] * 19

    # for i in range(len(db_values_ag)):
    #     sil_values_ag[i] = [0] * 4
    #     db_values_ag[i] = [0] * 4
    #     cr_values_ag[i] = [0] * 4

    # sil_values_km_total = []
    # db_values_km_total = []
    # cr_values_km_total = []

    # sil_values_em_total = []
    # db_values_em_total = []
    # cr_values_em_total = []

    # for i in range(2, 21):
    #     sil_values_km = []
    #     db_values_km = []
    #     cr_values_km = []

    #     sil_values_em = []
    #     db_values_em = []
    #     cr_values_em = []

    #     for j in range(len(links)):
    #         hier = hierarchical(n_clusters=i, linkage=links[j]).fit(data)
    #         sil_values_ag[i - 2][j] = scoreSil(data, hier.labels_)
    #         db_values_ag[i - 2][j] = scoreDB(data, hier.labels_)
    #         cr_values_ag[i - 2][j] = scoreCR(targets, hier.labels_)

    #     for k in range(0, 5):
    #         seed(k)

    #         kmeans = KMeans(n_clusters=i, n_init=1).fit(data)
    #         sil_values_km.append(scoreSil(data, kmeans.labels_))
    #         db_values_km.append(scoreDB(data, kmeans.labels_))
    #         cr_values_km.append(scoreCR(targets, kmeans.labels_))

    #         expectationm = em(n_components=i, max_iter=300).fit_predict(data)
    #         sil_values_em.append(scoreSil(data, expectationm))
    #         db_values_em.append(scoreDB(data, expectationm))
    #         cr_values_em.append(scoreCR(targets, expectationm))

    #     sil_values_km_total.append(sil_values_km)
    #     db_values_km_total.append(db_values_km)
    #     cr_values_km_total.append(cr_values_km)

    #     sil_values_em_total.append(sil_values_em)
    #     db_values_em_total.append(db_values_em)
    #     cr_values_em_total.append(cr_values_em)

    # sil_values_km_avg = [statistics.mean(vec) for vec in sil_values_km_total]
    # db_values_km_avg = [statistics.mean(vec) for vec in db_values_km_total]
    # cr_values_km_avg = [statistics.mean(vec) for vec in cr_values_km_total]

    # sil_values_km_sd = [statistics.stdev(vec) for vec in sil_values_km_total]
    # db_values_km_sd = [statistics.stdev(vec) for vec in db_values_km_total]
    # cr_values_km_sd = [statistics.stdev(vec) for vec in cr_values_km_total]

    # sil_values_em_avg = [statistics.mean(vec) for vec in sil_values_em_total]
    # db_values_em_avg = [statistics.mean(vec) for vec in db_values_em_total]
    # cr_values_em_avg = [statistics.mean(vec) for vec in cr_values_em_total]

    # sil_values_em_sd = [statistics.stdev(vec) for vec in sil_values_em_total]
    # db_values_em_sd = [statistics.stdev(vec) for vec in db_values_em_total]
    # cr_values_em_sd = [statistics.stdev(vec) for vec in cr_values_em_total]

    # writeCSV("sil_kmeans.csv", sil_values_km_total)
    # writeCSV("db_kmeans.csv", db_values_km_total)
    # writeCSV("cr_kmeans.csv", cr_values_km_total)

    # writeCSV("sil_em.csv", sil_values_em_total)
    # writeCSV("db_em.csv", db_values_em_total)
    # writeCSV("cr_em.csv", cr_values_em_total)

    writeCSV("sil_all.csv", sil_values_ag)
    writeCSV("db_all.csv", db_values_ag)
    writeCSV("cr_all.csv", cr_values_ag)
