import sys
import json
from collections import Counter

catcount = 0
catlist = []
sublist = []
i = 0
count = 0

my_dict = {}

print(my_dict.values())

today_json_file =  open("C:/Users/Parvez/Desktop/dataweave/today.json", "r")
# # data = json.load(today_json_file)
# # today_json_file.close()

# # print(data)

try:
    for line in today_json_file:
        # while i < 100:
        #     i += 1
        st = eval(line)
        cat = st["category"]
        subcat = st["subcategory"]
        if not cat in catlist: 
            catlist.append(cat)
        if not subcat in sublist: 
            sublist.append(subcat)
except NameError as x:
    pass

# print (catlist)
# print (sublist) 

# subcat_dict = Counter(sublist)

# print(subcat_dict)


# resultobj = open('result.txt','w')
# try:
#     for line in today_json_file:
#         st = eval(line)
#         if st['category'] in catlist and st['subcategory'] in sublist:
#             count=count+1
#             result = st['category'] + ' > ' + st['subcategory'] + ' : ' + str(subcat_dict[st['subcategory']])
#             resultobj.write(result)

# except NameError as x:
#     pass

# resultobj.close()


# fileobj=open('log.txt','w')
# fileobj.write(str(catlist))
# fileobj.write('\n')
# fileobj.write(str(sublist))
# fileobj.close()

        

        
        
        
    #print("household:",catcount)



#print(type(st))
        #print(st["category"])
        #s = string(st["category"])
        #st=eval(line)
        #print(st)
        #print(type(st))
        #v=str(st["category"])
        #if v == 'Household':
         #   catcount= catcount+1

        # if "category" in st.values():
        #     catcount= catcount+1