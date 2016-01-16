# Simple implementation of a very simple sorting algorithm
# on avarage O(n^2)
# good when an array is almost sorted, yet remember that it's always better
#   to retain an sorted array by inserting in the proper position using bisect.insort(*args)


def insertion_sort(l):
    for i in range(1, len(l)):
        j = i - 1
        key = l[i]
        while (j >= 0) and (l[j] > key):
            l[j+1] = l[j]
            j -= 1
        l[j+1] = key
