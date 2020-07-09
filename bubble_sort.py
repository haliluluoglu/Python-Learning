#Sort from descending to ascending
def bubble_sort(list):
    print("Unsorted list: ", list)
    for i in range(len(list)):
        for j in range(0,len(list)-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    print("Sorted list: ", list)

number_list=[4,1,3,5,2,7]
bubble_sort(number_list)