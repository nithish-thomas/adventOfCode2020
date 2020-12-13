def find2NumbersThatAddTo(arr, expectedSum, lo, hi):
    while lo < hi:
        sum = arr[lo] + arr[hi]
        if sum == expectedSum:
            return lo, hi
        elif sum < expectedSum:
            lo = lo + 1
        else:
            hi = hi - 1


def find3NumbersThatAddTo(arr, expectedSum):
    lo = 0
    hi = len(arr) - 1
    found = None
    while arr[hi] > expectedSum:
        hi = hi - 1
    while found is None:
        found = find2NumbersThatAddTo(arr, expectedSum - arr[hi], lo, hi - 1)
        if found is not None:
            act_lo, mid = found
            return act_lo, mid, hi
        hi = hi - 1


def main():
    f = open("input1.txt", "r")
    inp = f.read().split('\n')
    inp = [int(numeric_string) for numeric_string in inp]
    inp.sort()
    lo, mid, hi = find3NumbersThatAddTo(inp, 2020)
    print(inp[lo])
    print(inp[mid])
    print(inp[hi])
    print(inp[lo] * inp[mid] * inp[hi])


if __name__ == '__main__':
    main()

# def find3NumbersThatAddTo(arr, expectedSum):
#     lo = 0
#     mid = int(len(arr) / 2)
#     hi = len(arr) - 1
#     while lo < hi:
#         sum = arr[lo] + arr[mid] + arr[hi]
#         if sum == expectedSum:
#             return lo, mid, hi
#         elif sum < expectedSum:
#             diff1 = arr[lo + 1] - arr[lo]
#             diff2 = arr[mid + 1] - arr[mid]
#             if diff1 > diff2:
#                 mid = mid + 1
#                 if mid == hi: hi = hi + 1
#             else:
#                 lo = lo + 1
#                 if mid == lo: mid = mid + 1
#                 if mid == hi: hi = hi + 1
#
#         else:
#             diff1 =  arr[hi] - arr[hi - 1]
#             diff2 =  arr[mid] - arr[mid - 1]
#
#             if diff1 > diff2:
#                 mid = mid - 1
#                 if mid == lo: lo = lo - 1
#             else:
#                 hi = hi - 1
#                 if mid == hi: mid = mid - 1
#                 if mid == lo: lo = lo - 1
