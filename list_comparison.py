


list1 = ['aaa',111,(4,5),2.01]
list2 = ['bbb',333,111,3.14,(4,5)]


#方案1
print('方案1')
for list1_info in list1:
    if list1_info in list2:
            print(str(list1_info)+' in List1 and List2')
    elif list1_info not in  list2:
            print(str(list1_info)+' only in list1')

#方案2
print('方案2：')
list_all = list(set(list1) & set(list2))
for list1_info in list1:
    if list1_info in list_all:
        print(str(list1_info)+' in list1 and list2')
    else:print(str(list1_info)+ ' only in list1')








