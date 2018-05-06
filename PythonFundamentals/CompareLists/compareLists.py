# Compare Lists
def compare_lists(list_one, list_two):
    if list_one == list_two:
        print ("Same")
    else:
        print ("Different")

A = "A"
l1 = [A, "B", 1]
l2 = ["A", "B", 1]
compare_lists(l1, l2)
l1 = [42, 37, 99]
l2 = [1,2,3]
compare_lists(l1, l2)

