# #stacking

# class Stack:
#     def __init__(self):
#         self.items=[]
#     def push(self,data):
#         self.items.append(data)      #for top[-1]
#     def pop(self):
#         self.items.pop()
#     def size(self):
#         return len(self.items)
# s=Stack()
# s.push(10)
# s.push(20)
# s.push(30)
# s.push(40)
# print(s.items)
# print(s.items.pop())
# print(s.items)
# print(s.size())

# #parenthesis checker
# class Stack:
#     def __init__(self):
#         self.items=[]
#     def push(self,data):
#         self.items.append(data)
#     def pop(self):
#         self.items.pop()
#     def size(self):
#         return len(self.items)
    
# e="[3+7{52/11(3+5)}]"
# S=Stack()
# ob="[{("
# cb=")}]"
# flag=0
# for i in e:
#     if i in ob:
#         S.push(i)
#     if i in cb:
#         x=S.pop()
#         if x=="(" and i==")":
#             pass
#         elif x=="{" and i=="}":
#             pass
#         elif x=="[" and i=="]":
#             pass
#         else:
#             flag=1
#             break
# if flag==0 and S.size()== 0:
#     print("valid")
# else:
#     print("invalid")

#     # if empty=-1
# # if smaller -remove
# #if bigger- result
# # add current to stack
# class Stack:
#     def __init__(self):
#         self.items=[]
#     def push(self,data):
#         self.items.append(data)      
#     def pop(self):
#         self.items.pop()
#     def size(self):
#         return len(self.items)
#     def top(self):
#         return self.items[-1]
    
# l=[3,5,2,14,5,3,7,9,4,6,9,4,2,5,3]
# o=[0]*len(l)
# s=Stack()
# for i in range(len(l)-1,-1,-1):
#     if s.size()!=0:
#         while s.size() !=0 and s.top()<=l[i]:
#             if s.top() <= l[i]:
#                 s.pop()
#     if s.size() == 0:
#         o[i]=-1
#     else:
#         o[i]=s.top()
    
#     s.push(l[i])
            
# print(o)

# #LIFO(best example songs playlist,downloading,searching,youtube playlist)
# class Queue:
#     def __init__(self):
#         self.items=[]
#     def push(self,data):
#         self.items.append(data)
#     def pop(self):
#         self.items.pop(0)
#     def size(self):
#         return len(self.items)
# s=Queue()
# s.push(10)
# s.push(20)
# s.push(30)
# s.push(40)
# print(s.items)
# s.pop() 
# print(s.items)
# print(s.size())

# # link lists
# class Node:
#     def __init__(self,data):
#         self.value=data
#         self.next=None
        
# head=Node(10)
# head.next=Node(20)
# head.next.next=Node(30)

# class Node:
#     def __init__(self,data):
#         self.value=data
#         self.next=None
        
# Head=Tail=Node(10)

# Tail.next=Node(20)
# Tail=Tail.next

# Tail.next=Node(30)
# Tail=Tail.next

# Tail.next=Node(40)
# Tail=Tail.next

# print(Head)
# print(Tail)
# print(Head.next.next.next)

# print(Head.value)

# def print_link_list(Head):
#     if Head==None:
#         print('list is empty')
#         return
#     curr=Head

#     while curr!=None:
#         print(curr.value)
#         curr=curr.next
        
# print_link_list(Head)

# #Basic Calculator 

# s=input()
# OP=['+','-','*','/']
# for i in s:
#     if i in OP:
#         x=i
#         s=s.replace(x," ")

# l=list(map(float,s.split()))

# match x:
#     case '+': print(l[0]+l[1])
#     case '-': print(l[0]-l[1])
#     case '*': print(l[0]*l[1])
#     case '/': print(l[0]/l[1])
#     case _ : print("Invalid Operator")
