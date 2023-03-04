# import numpy as np
# x=[1,2,3,4]
# y=np.array([1,2,3,4,5])
# print(y)
# print(type(y))
# print(y.ndim)


# import numpy as np
# ar2=np.array([[1,2,3,4],[1,2,3,4]])
# print(ar2)
# print(ar2.ndim)


# import numpy as np
# ar3=np.array([[[1,2,3],[1,2,3],[1,2,3]]])
# print(ar3)
# print(ar3.ndim)


# import numpy as np
# arn=np.array([1,2,3,4],ndmin=10)
# print(arn)
# print(arn.ndim)

# for i in range(20,30,2):
#     print(i)

# country='INDIA'
# for i in country:
#     print(i)

# i=0;sum=0
#   while i<9:
#     if i%4==0:
#      sum=sum+i
#     print(sum)

# import numpy as np
# ar_zero = np.zeros(4)
# print(ar_zero)
#
#
# import numpy as np
# ar_zero=np.zeros([3,4])
# print(ar_zero)

# import numpy as np
# ar_one=np.ones(4)
# print(ar_one)
#
# import numpy as np
# ar_emp=np.empty(4)
# print(ar_emp)

# import numpy as np
# ar_rn=np.arange(4)
# print(ar_rn)

# import numpy as np
# ar_dia=np.eye(3)
# print(ar_dia)

# import numpy as np
# ar_dia=np.eye(3,5)
# print(ar_dia)

# import numpy as np
# ar_lin=np.linspace(1,10,5)
# print(ar_lin)

# import numpy as np
# var=np.random.rand(4)
# print(var)
#
# import numpy as np
# var=np.random.randn(4)
# print(var)
#
# import numpy as np
# var=np.random.ranf(4)
# print(var)
#
# import numpy as np
# var=np.random.randint(5,20,5)
# print(var)
#
# import numpy as np
# var=np.array([1,2,3,4])
# print("data type: ",var.dtype)
#
# import numpy as np
# var=np.array([1.0,1.2,2.3])
# print("data type: ",var.dtype)
#
# import numpy as np
# var=np.array(["A","S","O","L"])
# print("data type: ",var.dtype)


# import numpy as np
# var=np.array([[1,2,3,4],[1,2,3,4]])
# print(var)
# print()
# print(var.shape)

# import numpy as np
# var=np.array([[1,2],[1,2]])
# print(var)
# print()
# print(var.shape)

# import numpy as np
# var=np.array([1,2,3,4,5,6])
# x=var.reshape(3,2)
# print(x)

# import numpy as np
# var=np.array([1,2,3,4,5,6])
# print(var)
# print(var.ndim)
# print()

# import numpy as np
# var=np.array([1,2,3,4,5,6])
# x=var.reshape(3,2)
# print(x)
# print(x.ndim)

# import numpy as np
# var=np.array([1,2,3,4])
# varadd=var+3
# print(varadd)
#
# import numpy as np
# var1=np.array([1,2,3,4])
# var2=np.array([1,2,3,4])
# varadd=var1+var2
# print(varadd)
#
# import numpy as np
# var1=np.array([1,2,3,4])
# var2=np.array([1,2,3,4])
# varadd=np.add(var1,var2)
# print(varadd)
#
# import numpy as np
# var1=np.array([1,2,3,4])
# var2=np.array([1,2,3,4])
# varadd=np.subtract(var1,var2)
# print(varadd)
#
# import numpy as np
# var1=np.array([[1,2,3,4],[1,2,3,4]])
# var2=np.array([[2,3,4,5],[1,2,3,4]])
# print(var1)
# print()
# print(var2)
# varadd=var1*var2
# print(varadd)

# import numpy as np
# var=np.array([1,1,1,2])
# varadd=np.reciprocal(var)
# print(varadd)

# import numpy as np
# var=np.array([1,2,3,4,5,3,2])
# print("min: ",np.min(var))
# print("max: ",np.max(var))

# import numpy as np
# var=np.array([1,2,3,4,5,3,2])
# print("min: ",np.min(var),np.argmin(var))
# print("max: ",np.max(var),np.argmax(var))

# name=input("enter your name: ")
# print(name)
#
# num=input("enter a number: ")
# print(num)

# p=input("enter the first number: ")
# q=input("enter the second number: ")
# r=p+q
# print("the sum of two number is: ")

# import numpy as np
# var=np.array([[2,1,3],[9,5,6]])
# print(np.min(var,0))
#
# import numpy as np
# var=np.array([[2,1,3],[9,5,6]])
# print(np.min(var,1))
#
# import numpy as np
# var=np.array([[10,6,7],[9,5,6]])
# print(np.min(var,0))
#
# import numpy as np
# var=np.array([1,2,3,4,5,3,2])
# print("sqrt: ",np.sqrt(var))
#
# import numpy as np
# var=np.array([1,2,3])
# print(np.sin(var))
#
# import numpy as np
# var=np.array([1,2,3])
# print(np.cos(var))
#
# import numpy as np
# var=np.array([1,2,3])
# print(np.cumsum(var))
#
# import numpy as np
# var=np.array([[1,2,3],[1,3,6]])
# print(np.cumsum(var))

# import numpy as np
# var=np.array([[9,8,7],[4,5,6]])
# print(var)
# print(var.ndim)
# print()
# print(var[0])


# import numpy as np
# var=np.array([1,2,3,4,5,6,7])
# print(var)
# print()
# print("2 to 5: ",var[1:5])

# import numpy as np
# var=np.array([9,8,7,6,5,4,3])
# print(var)
# print()
# print("stop: ",var[1:5:2])j

# import numpy as np
# var=np.array([9,8,7,6,5,4,3])
# print(var)
# print()
# print("8 to end: ",var[1:])

# import numpy as np
# var=np.array([9,8,7,6,5,4,3])
# print(var)
# print()
# print("2 to end: ",var[1:])

# import numpy as np
# var=np.array([9,8,7,6,5,4,3])
# print(var)
# print()
# print(var[:5])



