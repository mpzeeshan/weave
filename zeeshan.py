

t, y, urlh_t, urlh_y, categories_t, categories_y, subcat_t, subcat_y = [],[],[],[],[],[],[],[]

try:

    with open('/home/zeeshan/Desktop/dataweave/today.json','r') as f:
        for line in f:
            t.append(eval(line))

    with open('/home/zeeshan/Desktop/dataweave/yesterday.json','r') as d:
        for line in d:
            y.append(eval(line))

except NameError as name:
    pass 

for line in t:
    urlh_t.append(line['urlh'])
    categories_t.append(line['category'])
    subcat_t.append(line['subcategory'])

for lin in y:
    urlh_y.append(lin['urlh'])
    categories_y.append(lin['category'])
    subcat_y.append(lin['subcategory'])

count = 0

for a in urlh_t and for b in urlh_y:
    print(a)
    print(b)
    break

print(count)
        
           
        
        
        # if x==y:
        #     count=count+1
        # else:
        #     continue








