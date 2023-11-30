def eliminate_duplicate():
    test_list = [1, 2, 3, 2, 1, 6, 3, 4, 5, 2
]
    print ("The original list is : "+ str(test_list))

    test_list = list(set(test_list))

    print ("The list after removing duplicates : "+ str(test_list))
eliminate_duplicate()