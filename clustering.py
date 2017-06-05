import random
import sys
import math
from statistics import mean

nums0 = [16, 15, 14, 13, 34, 23, 24, 25, 26, 28, 45, 34, 23, 29, 12, 23, 45, 67, 23, 12, 34, 45, 23, 67, 23, 67]
nums1 = [16, 15, 14, 13, 34, 23, 24, 25, 26, 28, 45, 34, 23, 29, 12, 23, 45, 67, 23, 12, 34, 45, 23, 67, 23, 670]
nums2 = [160, 15, 14, 13, 34, 23, 24, 25, 26, 28, 45, 34, 23, 29, 12, 23, 45, 67, 23, 12, 34, 45, 23, 67, 23, 670]
nums3 = [16, 15, 14, 13, 34, 23, 24, 25, 26, 28, 45, 34, 23, 29, 12, 23, 45, 67, 23, 12, 34, 45, 23, 67, 23, 67]
nums4 = [16, 15, 25, 28, 45, 15]
nums5 = [353, 556, 928, 291, 700, 580, 861, 355, 527, 122, 778, 737, 306, 516, 927, 649, 244, 505, 792, 198, 876, 751, 589, 595, 538, 706, 557, 542, 539, 964, 13, 762, 605, 462, 546, 842, 695, 454, 487, 905, 337, 249, 0, 339, 615]
nums6 = [478, 915, 167, 407, 254, 296, 696, 256, 406, 16, 23, 964, 667, 347, 392, 33]
nums7 = [-35, 7, 95, -12, -18, 83, 0, -15, 63, -14, 47, -28, -9, 7, 50, -12]
nums8 = [55, 71, 52, 66, 73, 50, 96, 28, 74, 79, 97, 68, 41, 95, 62, 59]
nums9 = [15, 15, 16, 13, 17, 12, 16, 11, 11, 11, 13, 19, 13, 11, 16, 16, 15, 13, 19, 19]


#receves a list of data and removes the duplicates
def uniques(nums):
    uni = []
    for n in nums:
        if(not(n in uni)):
            uni.append(n)
    return uni

#receves a list of numbers and a number x. calculates the closest number to x in l and returns a pair (closest number to x, index of that number in  l)
def minDist(l, x):
    dist = sys.maxsize
    ind = 0
    n = l[0]
    for i in range(len(l)):
        d = abs(x-l[i])
        if(d <= dist):
            dist = d
            ind = i
            n = l[i]
    return (n, ind)

#recebes 2 lists of numbers. returns a number from the first list, that has the greatest minimum distance to the numbers of the second list
def mostDistant(nums, centers):
    mins = []
    for n in nums:
        dists = []
        for c in centers:
            dists.append(abs(n-c))
        mins.append(min(dists))
    return nums[mins.index(max(mins))]

#initializes the k centers most distant as possible from eachother
def initCenters(nums, k):
    centers = []
    if(k>1):
        centers.append(min(nums))
        centers.append(max(nums))
    for i in range(k-2):
            centers.append(mostDistant(nums, centers))
    centers = orderCenters(centers, nums)
    return centers

#fills the clusters by the minimum distance from the centers
def fillClusters(nums, centers, k):
    new = []
    for i in range(k):
        new.append([])
    for n in nums:
        ind = minDist(centers, n)[1]
        new[ind].append(n)
    return new

#orders centers by the nums disposal
def orderCenters(centers, nums):
    newCenters = []
    for n in nums:
        if (n in centers):
            newCenters.append(n)
            centers.remove(n)
    return newCenters

#calculates the mean of each cluster and redifines the new centers by the closest to that mean
def redifineCenters(new, nums, k):
    centers = []
    for i in range(k):
        uni = uniques(new[i])
        me = int(mean(uni))
        x = minDist(uni, me)[0]
        centers.append(x)
    centers = orderCenters(centers, nums)
    return centers

#oders the clusters by the nums order
def orderByNums(cluster, nums, k):
    new = []
    firsts = []
    ind = []
    for i in range(k):
        new.append([])
        ind.append((i, nums.index(cluster[i][0])))
    ind.sort(key=lambda x: x[1])
    for i in range(len(ind)):
        new[i] = cluster[ind[i][0]]
    return new

#this is the main function trying to obtain a good Clustering by K-Means
def clusteringKMeans(nums, k):
    print("IN: ", nums)
    old = [[1]]
    new = []
    centers = initCenters(nums, k)
    while(not(new == old)):
        old = new
        new = fillClusters(nums, centers, k)
        centers = redifineCenters(new, nums, k)
    clusters = orderByNums(new, nums, k)
    print("OUT: ", clusters)


clusteringKMeans(nums0, 3)
clusteringKMeans(nums1, 3)
clusteringKMeans(nums2, 4)
clusteringKMeans(nums3, 5)
clusteringKMeans(nums4, 4)
clusteringKMeans(nums5, 6)
clusteringKMeans(nums6, 4)
clusteringKMeans(nums7, 10)
clusteringKMeans(nums8, 3)
clusteringKMeans(nums9, 4)


#generates examples
def genNums(n, start = 0, stop = 1000):
    nums = []
    for i in range(n):
        nums.append(random.randrange(start, stop))
    return nums
