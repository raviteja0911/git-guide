x=int (input("enter the number a :"))
y=int (input("enter the number b :"))
z=int (input("enter the number c :"))
if x>y & x>z :
    print("largest num is :",x)
elif y>z :
    print("largest num is :",y)
else:
    print("largest  num is :",z)


print("Ravi")
print(type("Ravi"))
name =int("teja")
print(type(name),name)
str1="first prog"
ch=str1[-10:-1]
print(ch)

str1="first prog"
ch=str1[2:5]
print(ch)


marks=[1,2,3,5,4]
print(marks)
print(type(marks))
marks.insert(2,3)
print(marks)
print(marks.count(3))


list1=list(input("enter the number a :"))
copy_list1=list1.copy()
list1.reverse()


if (copy_list1==list1):
  print("number is palindromic")
else :
 print("number is not palindromic")
student={
    "name":"ravi",
    "marks" :{
        "phy":89,
        "che":87,
        "math":55
    }
}
A=(student)
B=(type(student))
d=(student.get("name"))
e=(type(student.get("marks")))
c = (len(student.keys()))
f=(list(student.keys()))
g=(list(student['marks']))
h=(student.get("marks"))
i=(len(student['marks']))
j=(student["marks"]["phy"])
k=(student["marks"]["che"])
l=(student["marks"]["math"])
print("the dict containing keys are :",c,"type of dict is ",B,"and their names are :",f,"first key containing value as :",d,"second key is nested dic it containing keys as :",g,"key values of the second dict are ",h,"and the length of the second dict is ",i)



print("this is for educational purposes :")
print("this is for educational purposes1 :")







