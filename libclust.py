class SingleLinkage:

    def __init__(self, data, k):
        self.k = k
        self.data = data
        self.fit()

    def fit(self):
        n = len(self.data)
        self.clusters = {}

        for i in range(n):
          self.clusters[i] = []
          self.clusters[i].append(i)

        self.dist = np.sqrt((np.square(self.data[:,np.newaxis]-self.data).sum(axis=2)))

        for i in range(n-self.k):
            merge = self.merging()
            self.clusters[merge[0]] = self.clusters[merge[0]] + self.clusters[merge[1]]
            self.clusters.pop(merge[1])

        for i in range(self.k):
            while not i in self.clusters:
                for j in [x for x in list(map(int, self.clusters.keys())) if x >= i+1]:
                    self.clusters[j-1] = self.clusters.pop(j)

        for i in self.clusters.keys():
            self.clusters[i].sort()

    def merging(self):
        mini = 1e99
        merge = (None, None)

        for i in list(map(int, self.clusters.keys())):
            for j in [x for x in list(map(int, self.clusters.keys())) if x >= i+1]:
                if self.dist[i][j] < mini:
                    mini = self.dist[i][j]
                    merge = (i, j)
                    
        return merge