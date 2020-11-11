from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min

def summarize(answers):
    """
    Performs summarization of answers
    """
    n_answers = len(answers)
    summary = [None] * n_answers
    print('Starting to encode...')
    enc_answers = skipthought_encode(answers)
    print('Encoding Finished')
    for i in range(n_answers):
        enc_answer = enc_answers[i]
        n_clusters = int(np.ceil(len(enc_answer)**0.5))
        kmeans = KMeans(n_clusters=n_clusters, random_state=0)
        kmeans = kmeans.fit(enc_answer)
        avg = []
        closest = []
        for j in range(n_clusters):
            idx = np.where(kmeans.labels_ == j)[0]
            avg.append(np.mean(idx))
        closest, _ = pairwise_distances_argmin_min(kmeans.cluster_centers_,\
                                                   enc_answer)
        ordering = sorted(range(n_clusters), key=lambda k: avg[k])
        summary[i] = ' '.join([answers[i][closest[idx]] for idx in ordering])
    print('Clustering Finished')
    return summary
