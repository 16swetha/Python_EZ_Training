# with open("D:\\ck.txt",'a') as f: #appending
#     f.write("hello")
#     f.write(" my name is cks ")
#     f.write(" from ece bitm")
#     f.close()
#     print(f.read(5))
#     f.write('swetha is a gal')


# with open("D:\\ck.txt",'r') as f:
#     print(f.read())
#     f.close()


# with open("D:\\ck.txt",'r') as f:
#     s=f.read()
#     print(s)
#     f.close()
# s=s.replace("bitm","bellary")
# print(s)

# with open("D:\\ck.txt",'a') as f:
#     print(f.tell()) #to tell the position of the cursor in the file
#     f.close()

# with open("D:\\ck.txt",'rb') as f:
#     print(f.tell())#to tell the position of the cursor in the file
#     f.seek(-35,2) #to move the cursor in that position seek() only works in rb mode-read binary mode
#     print(f.read().decode('utf-8')) #we opened the file in binary mode so we convert it into readable mode
#     f.close()

# with open("D:\\ck.txt",'r+b') as f:
#     print(f.tell())
    
#     f.seek(-37,2) 
#     print(f.tell())
#     f.write(b"#") #to write new character on the cursor
#     print(f.read().decode('utf-8')) 
#     f.close()

# import os
# with open("file1.txt",'w') as d:
#     d.write("hi")
#     d.close()
# os.remove("file1.txt") #to remove file

# import os
# with open("file.txt",'wb') as f:
#     eid = 1
#     name="bat"
#     condition="good"
#     s=f"{eid},{name},{condition}\n"
#     f.write(s.encode())
#     s=f"{eid},{name},{condition}\n"
#     f.write(s.encode())
#     f.close()

# import os
# with open("file3.txt",'wb') as f:
#     eid1 = 1
#     name1="bat"
#     condition1="good"
#     eid2 = 2
#     name2="ball"
#     condition2="good"
#     eid3 = 3
#     name3="jersey"
#     condition3="bad"
#     s=f"{eid1},{name1},{condition1}\n"
#     f.write(s.encode())
#     s=f"{eid2},{name2},{condition2}\n"
#     f.write(s.encode())
#     s=f"{eid3},{name3},{condition3}\n"
#     f.write(s.encode())
#     f.close()




