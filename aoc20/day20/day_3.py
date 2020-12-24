
def main():
    f = open("input3.txt", "r")
    expression = f.read().split('\n')


    sum = 0
    for row in expression:
        for char in row:
            if char =="#":
                sum+=1

    print(sum)

if __name__ == "__main__":
    main()
