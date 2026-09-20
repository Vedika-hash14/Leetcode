import heapq

class MedianFinder:

    def __init__(self):
        self.small = []   # max heap
        self.large = []   # min heap

    def addNum(self, num):

        heapq.heappush(self.small, -num)

        if self.small and self.large:
            if -self.small[0] > self.large[0]:

                value = -heapq.heappop(self.small)

                heapq.heappush(self.large, value)

        if len(self.small) > len(self.large) + 1:

            value = -heapq.heappop(self.small)

            heapq.heappush(self.large, value)

        elif len(self.large) > len(self.small) + 1:

            value = heapq.heappop(self.large)

            heapq.heappush(self.small, -value)

    def findMedian(self):

        if len(self.small) > len(self.large):
            return -self.small[0]

        if len(self.large) > len(self.small):
            return self.large[0]

        return (-self.small[0] + self.large[0]) / 2