def Convert(mylist):
    length = len(mylist)
    mydict = []
    for i in range(1,length):
        h = dict(zip(mylist[0],mylist[i]))
        h1 = h.copy()
        mydict.append(h1)
    return mydict


inputlist=[
                     ['Sno', 'Partner Name', 'Release URL', 'Uniquevisitors'],
                     ['1', 'WN.Com', 'https://article.wn.com/', '1268148'],
                     ['2', 'New Delhi times', 'https://www.newdelhitimes.com/business', '1268148']
                ]

print("mydict=",Convert(inputlist))
