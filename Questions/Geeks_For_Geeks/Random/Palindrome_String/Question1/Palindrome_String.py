no_of_testcase = int(input())

for loop in range(1, (no_of_testcase + 1)):
    counter = 0
    string_length = int(input())
    string_is = input()
    if ((string_length % 2 == 0) or (string_length / 2)):
        full = string_length
        half = int((string_length / 2))
        for pointer in range(0, half):
            full = full - 1
            if ((string_is[pointer]) == (string_is[full])):
                counter = counter + 1
            else:
                break

    if (counter >= (half)):
        print("Yes")
    else:
        print("No")