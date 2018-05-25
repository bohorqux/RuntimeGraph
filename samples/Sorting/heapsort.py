#!/usr/bin/python3
#RAND_LIST

import heapq
def heap_sort(items):
        """ Implementation of heap sort """
        heapq.heapify(items)
        items[:] = [heapq.heappop(items) for i in range(len(items))]

heap_sort("TARGET")