
'''
This is a program written to perform analytics on two different .json files

normalise_mrp() - this function loads json data and checks if the value of a key
is in a particular format if not amends it and dumps the data to a new json file
where the mrp will be found normalised.

taxanomies() - this function checks for repeated occurences of all the combination of
category and subcaterogy it finds in both the .json files,it basically returns the count of it. 

'''
import json

today, yesterday = [],[]
i = 0

def normalise_mrp(newjson,oldjson):
    newlist= ''
    i=0
    mrp = 0
    fileob=open(newjson,'w')
    fileob.close()
    fileobj=open(newjson,'a') 

    with open(oldjson,'r+') as file:
        for line in file:
            newlist = json.loads(line)
            try:
                mrp = float(newlist['mrp'])
            except TypeError as ty:
                pass
            i=i+1
            if mrp == 0 or isinstance(mrp,float) == False or 'mrp' not in newlist.keys():
                newlist['mrp'] = 'NA'
            
            fileobj.write(json.dumps(newlist))
            fileobj.write('\n')
    fileobj.close()


def Taxnomies(day,pday):
    list1=[]
    last_cat = 'bla'
    last_subcat = 'bla'
    s=0
    f.write('\n')
    f.write('5. Repeated Categories and subcategories count: '+pday)
    f.write('\n')

    for x in range(len(day)):
        if day[x]['category'] != last_cat and day[x]['subcategory'] != last_subcat:
            s=0
            for y in range(len(day)):
                if day[x]['category'] == day[y]['category'] and day[x]['subcategory'] == day[y]['subcategory']:
                    s = s+1
            if(s>0):
                list1.append(str((day[x]['category']+' > '+day[x]['subcategory']+': '+str(s))))
                
        try:    
            last_cat = day[x]['category']
            last_subcat = day[x]['subcategory']
        except IndexError as ind:
            pass

    list1 = list(set(list1))
    list1.sort()
    f.write('\n')
    
    for item in list1:    
        f.write(item)
        f.write('\n')


###################### Execution Starts Here ###########################################################

todayy=open('t.json')
yesterdayy=open('yesterday.json')

for line in todayy:
    today.append(json.loads(line))

for line in yesterdayy:
    yesterday.append(json.loads(line))

finalfile = open('output.txt','w')
finalfile.close()

######################## 1. overlapping urlh and price difference ##############################
url_today = []
url_yesterday = []
over_lap = 0

f = open('output.txt','a')

for line in today:
    url_today.append(line['urlh'])

for line in yesterday:
    url_yesterday.append(line['urlh'])

overlapped_urlh = list(set(url_today).intersection(url_yesterday))
f.write('\n')
f.write('-----------------------------------------------------------------')
f.write('\n')
f.write(str("1. No. of overlapped urlh: "+str(len(overlapped_urlh))))
f.write('\n')
f.write('\n')
f.write("2. Price Difference of urlh")
f.write('\n')
f.write('\n')

for i in range(5000):
    try:
        urlt=today[i]['urlh']
        for y in range(5000):
            if urlt == yesterday[y]['urlh'] and urlt in overlapped_urlh:
                if today[i]['http_status'] == '200' and yesterday[y]['http_status'] == '200':
                    try:
                        if abs(float(today[i]['available_price'])-float(yesterday[y]['available_price'])) > 0:
                            f.write(str("Price Difference for URLH: "+urlt))
                            f.write('\n')
                            f.write(str(abs(float(today[i]['available_price'])-float(yesterday[y]['available_price']))))
                            f.write('\n')
                    except TypeError as ty:
                        pass
                    overlapped_urlh.remove(today[i]['urlh']) 
    except IndexError as ind:
        pass

f.write('\n')        
f.write('-------------------------------------------------------------------')
    
############################# 3,4. no of unique categories and list of categories which are not overlapping ############################################

list1 = []
list2 = []
list3 = []

for x in range(len(today)):
    if today[x]['category'] not in list1:
        list1.append(today[x]['category'])

for x in range(len(yesterday)):
    if yesterday[x]['category'] not in list2:
        list2.append(yesterday[x]['category'])

f.write('-----------------------------------------------------------------------')
f.write('\n')
f.write('3. No of unique categories in both files:'+str(len(set(list1+list2))))
f.write('\n')
for x in range(len(list1)):
    if list1[x] not in list2:
        list3.append(list1[x])

f.write('\n')
f.write('4 List of catergories which are not overlapping')
f.write('\n')
f.write(str(list3))
f.write('\n')

Taxnomies(today,'Today')
Taxnomies(yesterday,'Yesterday')

normalise_mrp('newtoday.json','t.json')
normalise_mrp('newyesterday.json','yesterday.json')

f.close()
