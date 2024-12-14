#create  a new file 
file=open('new_file.txt','x')
file.close()


#check if file exists 
import os
if os.path.exists('mahi.txt'):
    print("file exists")

else:
    print("file does not exists ")

file1=open("mahi.txt","w")
file1.write("hello i am mahi ")
file1.close()


os.remove('mahis.txt')
  