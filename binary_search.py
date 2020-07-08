number_array=[1,2,3,4,5,6,7,8,9,10]


def binary_search(list,searching_element):
    lower=0
    upper=len(list)-1
    while(lower<=upper):
        middle = int((lower + upper) / 2)
        if list[middle]==searching_element:
            return middle
        elif list[middle]<searching_element:
            lower=middle+1
        elif list[middle]>searching_element:
            upper=middle+1
        else:
            return False
    return False
index=binary_search(number_array,10)

if index!=False:
    print("The index of element: {}".format(index))
else:
    print("The element not found!")