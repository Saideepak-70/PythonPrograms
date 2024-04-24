def anagram(string1, string2):
    my_list1 = list(string1)
    my_list2 = list(string2)
    my_list1.sort()
    my_list2.sort()
    new_string1 = ''.join(my_list1)
    new_string2 = ''.join(my_list2)
    if new_string1 == new_string2:
        flag = 1
    else:
        flag = 0

    return flag
string1 = input("Enter a string : ")
string2 = input("Enter another string : ")
flag = anagram(string1, string2)
if flag == 1:
    print("Anagrams")
else:
    print("Not Anagrams")