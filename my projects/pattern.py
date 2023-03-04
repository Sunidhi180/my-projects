# n = 3
# for i in range(1,n+1):
#     sp = (n-i)*" "
#     sym = (2*i-1)*"*"
#     print(sp,sym)
# for j in range(n-1,0,-1):
#     sp = (n-j)*" "
#     sym = (2*j-1)*"*"
#     print(sp,sym)
#
# num=5
# for i in range(1,num+1):
#    sp = (num-i)*"  "
#    print(sp,end=" ")
#    for k in range(i,1,-1):
#        print(k,end=" ")
#    for j in range(1,i+1):
#       print(j,end=" ")
#    print()


# str = "123456"
# for i in (str):
#    print(" "*int(i)+str[0:len(str)-int(i)])
#
#
# num = 5
# for i in range(num,0,-1):
#     sp=(num-i)*" "
#     print(sp,end=" ")
#     for k in range(1,i+1):
#         print(k,end=" ")
#     print()
#
#
# num=3
# k=0
# for i in range(1,num+1):
#     sp=(num-i)*" "
#     print(sp,end=' ')
#     while(k!=(2*i-1)):
#         if(k==0 or k== 2*i-2):
#           print("*",end="")
#         else:
#          print(" ",end="")
#         k=k+1
#     k=0
#     print()
# for j in range(num-1,0,-1):
#     sp=(num-j)*" "
#     print(sp,end=" ")
#     k=(2*j-1)
#     while(k>0):
#         if(k==1 or k==2*j-1):
#             print("*",end="")
#         else:
#          print(" ",end="")
#         k=k-1
#     print()