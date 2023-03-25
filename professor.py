import random


def main():
    level = get_level()
    print(level)
    generate_integer(level)


def get_level():
    while True:
        try:
            x = int(input("Level: "))
            if x == 1 or x == 2 or x == 3:
                return x
            else:
                raise ValueError()
        except ValueError:
            continue


def generate_integer(level):
    countOfMistakes = 0
    task = 0
    score = 10
    while True:
        match level:
            case 1:
                x = random.randint(0, 9)
                y = random.randint(0, 9)

            case 2:
                x = random.randint(10, 99)
                y = random.randint(10, 99)

            case 3:
                x = random.randint(100, 999)
                y = random.randint(100, 999)
        realSum = x + y
        while True:
            try:
                print(x, " + ", y, " = ", end="")
                sum = int(input())
                if sum == realSum:
                    countOfMistakes = 0
                    task = task + 1
                    if task == 10:
                        break
                    else:
                        break
                else:
                    raise ValueError()
            except ValueError:
                print("EEE")
                countOfMistakes = countOfMistakes + 1
                if (countOfMistakes == 3):
                    print(x, " + ", y, " = ", realSum)
                    score = score - 1
                    task = task + 1
                    countOfMistakes = 0
                    break
                else:
                    continue
        if task == 10:
            print("Score: ", score)
            break


if __name__ == "__main__":
    main()
