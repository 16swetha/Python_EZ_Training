# #logical for the below code

# s=input()
# dic={'A':0,'E':0,'I':0,'O':0,'U':0}
# for i in s:
#     if i=='a' or i=='A':
#         dic['A']+=1
#     elif i=='e' or i=='E':
#         dic['E']+=1
#     elif i=='i' or i=='I':
#         dic['I']+=1
#     elif i=='o' or i=='O':
#         dic['O']+=1
#     elif i=='u' or i=='U':
#         dic['U']+=1
# print(dic)

# x=max(dic.values())
# print(x)
# result=[]
# for i,j in dic.items():
#     if j==x:
#         print(i)
#         result.append(i)
# print(result)

# #the actual code for the problem statement OCCURANCE OF VOWELS

# def count_vowel(s):
#     dic={'A':0,'E':0,'I':0,'O':0,'U':0}
#     for i in s:
#         if i=='a' or i=='A':
#             dic['A']+=1
#         elif i=='e' or i=='E':
#             dic['E']+=1
#         elif i=='i' or i=='I':
#             dic['I']+=1
#         elif i=='o' or i=='O':
#             dic['O']+=1
#         elif i=='u' or i=='U':
#             dic['U']+=1

#     x=max(dic.values())
#     result=[]
#     for i,j in dic.items():
#         if j==x:
#             result.append(i)
#     return result


# i_p=[["alex","im going out"],
#      ["sam","i love playing"],
#      ["ani","i like playing basketball"]]

# o_p={}

# for i in i_p:
#     o_p[i[0]]=count_vowel(i[1])

# print(o_p)

# #given an integer array your task is to find the k continious digits which gives you the maximum sum
# n=[2,4,3,5,6,3,4,6,7,1,2,5]
# sum=max=0
# for i in range(0,len(n)-2):
#     sum =n[i]+n[i+1]+n[i+2]
#     if max<=sum:
#         max=sum
#         p=i
# print(max,n[p],n[p+1],n[p+2])

# #given an integer array your task is to find the k continious digits which gives you the maximum sum.where k is entered by user

# n=[2,4,3,5,6,3,4,6,7,1,2,5]
# k=int(input("enter the no of continious digit"))
# sum=max=0
# for i in range(0,len(n)-(k-1)):
#     sum=0
#     for j in range(0,k):
#         sum+=n[i+j]
#     if max<sum:
#         max=sum
#         p=i
# print(max)
# for j in range(0,k):
#     print(n[p+j])

#     #"sliding window" time complexity

# n=[2,4,3,5,6,3,4,6,7,1,2,5,9,9,9]
# window = max = 0
# k=int(input("enter the no of continious digit"))

# for j in range(0,k):
#     window+=n[j]
    
# n.append(0)
# for i in range(0,len(n)-k):
#     if max<=window:
#         max=window
#         p=i
#     window = window+n[i+k]-n[i]
       
# print(max)
# for j in range(0,k):
#     print(n[p+j])