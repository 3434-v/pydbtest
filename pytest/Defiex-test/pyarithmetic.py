def quickSort(alist: list):
    queickSortHelper(alist, 0, len(alist) - 1)


def queickSortHelper(alist: list, first, last):
    if first < last:
        splistpoint = partition(alist, first, last)
        queickSortHelper(alist, first, splistpoint - 1)
        queickSortHelper(alist, splistpoint + 1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

        temp = alist[first]
        alist[first] = alist[rightmark]
        alist[rightmark] = temp

        return rightmark

