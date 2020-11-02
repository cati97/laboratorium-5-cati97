class Hamming:
    def distance(self, first, second):
        if len(first) > len(second):
            raise ValueError("First strand cannot be longer!")
        else:
            if first == "" and second == "":
                return 0
            elif first == second:
                return 0
            else:
                countDiff = 0
                for i in range(len(first)):
                    if first[i] != second[i]:
                        countDiff += 1
                    else:
                        continue
                return countDiff