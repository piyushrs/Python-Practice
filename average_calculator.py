a = float(input("Input current price of stock: "))
q1 = float(input("Input current quantity: "))
b = float(input("Input new price of stock: "))
q2 = float(input("Input new quantity: "))
print("Your new average = ", ((a*q1)+(b*q2))/(q1+q2))
print("Current investment = ", a*q1)
print("New investment = ", b*q2)
print("Total investment = ", ((a*q1)+(b*q2)))
# import os
# path = "/media/piyushraisinghani/Piyush/Practice/"
# result = [os.path.join(dp, f) for dp, dn, filenames in os.walk(path) for f in filenames]
# for r in result:
#     print(r)

# print(len(r))

# IDEA:
# 1. machine learning for types of gifts to give someone - enter habits and the type of things the person likes, AI would suggest the gift