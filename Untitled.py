# numList = List of integers, k = number of highest integers in the list


def gottaGetAJob(numList, k):
    highest = []

    for currentNumber in numList:
        if highest == []:
            highest.append(currentNumber)
        else:
            for currentHighest in highest:
                index = 5

                if currentHighest < currentNumber:
                    index = highest.index()

            if index != 5:
                highest[index] = currentNumber

    return highest

if __name__ == "__main__":
    list1 = [1, 10, 65, 76, 90, 14]

    array = gottaGetAJob(list1, 2)

    print(array)
