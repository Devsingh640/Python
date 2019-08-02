no_of_testcase = int(input())

for loop in range(1, (no_of_testcase + 1)):
    given_string = input()
    a = True
    all_non_repeating_palindrome_sub_strings = list()
    previous_element = given_string[0]

    def check_palindrome(check_this_string):
        counter = 0
        recieved_sub_string_length = len(check_this_string)
        if ((recieved_sub_string_length % 2 == 0) or (recieved_sub_string_length / 2)):
            full = recieved_sub_string_length
            half = int((recieved_sub_string_length / 2))
            for pointer in range(0, half):
                full = full - 1
                if ((check_this_string[pointer]) == (check_this_string[full])):
                    counter = counter + 1
                else:
                    a = False
                    break
        if (counter >= (half)):
            a = True
        else:
            a = False
        return a


    for now_incriment_from_here in range(0, (len(given_string))):  
        for incriment in range(now_incriment_from_here, (len(given_string) + 1)):
            incriment_sub_string = incriment + 1
            if (incriment_sub_string <= (len(given_string))):
                check_this_string = given_string[now_incriment_from_here:(incriment_sub_string)]
                get = check_palindrome(check_this_string)
                if not get:
                    pass
                else:
                    print(" Palindrome String : ", check_this_string, 
                    " ( Starting index : ", now_incriment_from_here, ")",
                    " ( ending index : ", (incriment_sub_string - 1), ")"
                    )
                    print(" ")
                    all_non_repeating_palindrome_sub_strings.append(check_this_string)

    for elements in (all_non_repeating_palindrome_sub_strings):
        this_element_length = len(elements)
        previous_element_length = len(previous_element)
        if (previous_element_length < this_element_length):
            print("element is : ", elements,
            " and element length is : ", this_element_length,
            " previous element is : ", previous_element,
            " and previous element length is : ", previous_element_length
            )
            this_is_greatest_palindrome = elements
            previous_element = this_is_greatest_palindrome
        else:
            this_is_greatest_palindrome = previous_element
            previous_element = this_is_greatest_palindrome
            
    print(all_non_repeating_palindrome_sub_strings," and its length is : ",len(all_non_repeating_palindrome_sub_strings))
    print(" ")        
    print(this_is_greatest_palindrome)

    all_non_repeating_palindrome_sub_strings.clear()