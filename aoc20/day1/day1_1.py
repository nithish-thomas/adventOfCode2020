def findNumbersThatAddTo(arr, expectedSum):
    lo = 0
    hi = len(arr) - 1
    while lo < hi:
        sum = arr[lo] + arr[hi]
        if (sum == expectedSum):
            return (lo, hi)
        elif sum < expectedSum:
            lo = lo + 1
        else:
            hi = hi - 1




def main():
    f = open("input1.txt", "r");
    inp = f.read().split('\n');
    inp = [int(numeric_string) for numeric_string in inp]
    inp.sort()
    lo, hi = findNumbersThatAddTo(inp, 2020)
    print(inp[lo])
    print(inp[hi])
    print (inp[lo]*inp[hi])

if __name__ == '__main__':
    main()
