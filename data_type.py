# print(type(5/2))  #output: float
# print(type(2.5))  #output: float
# print(type(4/2))  #output: float
import copy

# value1 = 4.5
# value2 = 3.2
# print(value1 + value2)  # Output: 7.7
# print(value1 - value2)  # Output: 1.2999999999999998
# print(value1 / value2)  # Output: 1.40625
# print(value1 % value2)  # Output: 1.2999999999999998
#
# ## to calculate a simple interest
# def calculate_simple_interest(principal,interest,duration):
#     # total_amount =[]
#     total_amount = principal+(principal*interest*0.01*duration)
#     return total_amount
# print(calculate_simple_interest(10000,5,5))

# print(pow(5,2))
#
# a = lambda x,y: x+y
# print(a(2,3))

# list= [1,2,3]
# v = iter(list)
# res = next(v)
# print(res)

# def vasa():
#     yield 5
# v = iter(vasa())
# res = next(v)
# print(res)

# set ={3,4,5,6,0,3}
# print(set)
#
# d = {'ka':'kavi','k':'jjj'}
# print(d['k'])

#
# import copy
# a = [[1,2],[2,3]]
# b = copy.deepcopy(a)
# a[0][1]=0
# print(b)


for i in range(1,6):
    for j in range(i):
        print("*")

