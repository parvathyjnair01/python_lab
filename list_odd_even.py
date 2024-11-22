'''
Author:Parvathy J Nair
Description:Input two lists from the user.
Merge these two lists into a third list such that all even numbers occur in the first followed by odd numbers.
Both even numbers and odd numbers should be in sorted order
'''
list1=[1,2,3,4,5,6]
list2=[7,8,9,10,21.34,55]
list3=list1+list2
even_list=[]
odd_list=[]
for i in list3:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
even_list.sort()
print("List1:",even_list)
odd_list.sort()
print("List2:",odd_list)
print("Final list:")
merged_list=even_list+odd_list
print(merged_list)