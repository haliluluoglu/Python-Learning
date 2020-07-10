#Selection sort from descending to ascending
def selection_sort(list):
    print("Unsorted list->", list)
    for i in range(0,len(list)):
        j=i+1
        min_value=list[i]
        min_index=i
        while(j<len(list)):
            if list[min_index]>list[j]:
                min_value=list[j]
                min_index=j
            j+=1
        list[i],list[min_index]=list[min_index],list[i]
    print("Sorted list->", list)

number_list=[4,5,1,3,2,0]
selection_sort(number_list)