# QUESTION: Write a complete Python program to do the following:
# (i) Read an integer X
# (ii) Determine the number of digits n in X
# (iii) form an integer Y that has the number of digits n at tens place and most significant digit of X at ones place
# (iv) Output Y
import math
user_inp=int(input("Enter an integer :"))
user_inp_str=str(user_inp)
lst=[]
for a in user_inp_str:
    lst.append(a)
len_user_inp=len(lst)
power=math.pow(10,len_user_inp-1)
num_tens=user_inp//power
list_1=[]
list_1.append(len_user_inp)
list_1.append(power)
print(len_user_inp,int(num_tens),sep='')
