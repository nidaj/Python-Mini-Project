# --------------
##File path for the file 
file_path 


#Code starts here
def read_file(path):
    #path=file_path
    file=open(path,mode='r')
    #for i in file.read():
    sentence=file.read()
    file.close()
    return sentence
sample_message = read_file(file_path)
print(sample_message)



# --------------
#Code starts here
#file_path_1
#file_path_2
message_1 = read_file(file_path_1)
message_2 = read_file(file_path_2)
print(message_1)
print(message_2)
def fuse_msg(message_a,message_b):
    quotient = int(message_b)//int(message_a)
    return str(quotient)
secret_msg_1 = fuse_msg(message_1,message_2)
print(secret_msg_1)





# --------------
#Code starts here
message_3 = read_file(file_path_3)
print(message_3)
def substitute_msg(message_c):
    if message_c == 'Red':
        sub = 'Army General'
    elif message_c == 'Green':
        sub = 'Data Scientist'
    elif message_c == 'Blue':
        sub = 'Marine Biologist'
    return sub
secret_msg_2=substitute_msg(message_3)
print(secret_msg_2)




# --------------
# File path for message 4  and message 5
file_path_4
file_path_5

#Code starts here
message_4=read_file(file_path_4)
message_5=read_file(file_path_5)
print(message_4)
print(message_5)
def compare_msg(message_d,message_e):
    a_list = message_4.split()
    b_list = message_5.split()
    c_list=[]
    for i in a_list:
        flag=1
        for j in b_list:
            if (i==j):
                flag=0
        if flag==1:
            c_list.append(i)
    final_msg=" ".join(c_list)
    return final_msg
secret_msg_3=compare_msg(message_4,message_5)
print(secret_msg_3)







# --------------
#Code starts here
message_6 = read_file(file_path_6)
print(message_6)
def extract_msg(message_f):
    a_list=message_f.split()
    #return a_list
    even_word = lambda x:len(x)%2==0
    b_list = list(filter(even_word,a_list))
    final_msg = " ".join(b_list)
    return final_msg
secret_msg_4=extract_msg(message_6)


# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]
final_path= user_data_dir + '/secret_message.txt'

#Code starts here
secret_msg=" ".join(message_parts)
print(secret_msg)
def write_file(secret_msg, path):
    file=open(path,mode='a+')
    file.write(secret_msg)
    file.close()
write_file(secret_msg,final_path)



