import re
defaultitem = []
titlestring=""
with open("out.CSV", "r") as f:
    lines = f.readlines()
    for idx,item in enumerate(lines):
        if idx == 0:
            #print(item)
            #put every attributes into an array
            idxs = item.split(",")
            #print(len(idxs))
            titlestring = item

        if idx == 1:
            each_item = item.split(",")
            #print(len(each_item))
            for nidx, nitem in enumerate(each_item):
                #print("{}:{}".format(idxs[nidx],nitem))
                if("Frequency" in idxs[nidx] or "DCS Encode"in idxs[nidx]):
                    defaultitem.append("0")
                else:
                    defaultitem.append(nitem)

# for idx, items in enumerate(defaultitem):
#     print("{}:{}".format(idxs[idx].strip(), items))


finallist = []

c_count = 1

with open("in.txt", "r") as f:
    lines = f.readlines()
    for idx,item in enumerate(lines):
        if "FM" in item and ("440" in item or "144" in item) \
            and ("Vanc" in item or "Langley" in item or "Bur"in item or "Sur" in item or "Del" in item or "Coq" in item or "Ric" in item or "Abb" in item or "Miss" in item or "Chill" in item or "Salt" in item):
            #print(item)
            eachattr = item.split("\t")
            print(eachattr)

            temp_item = defaultitem
            #"No.":"1"
            #"Channel Name":"Channel 1"
            #"Receive Frequency":0
            #"Transmit Frequency":0
            #"Channel Type":"A-Analog"
            #"Transmit Power":"Turbo"
            #"Band Width":"25K"
            #"CTCSS/DCS Decode":"Off"
            #"CTCSS/DCS Encode":0
            temp_item[0] = "\""+str(c_count)+"\""
            temp_item[1] = "\""+str(eachattr[3].strip("\""))+"\""
            temp_item[3] = "\""+str(eachattr[2])+"\""
            temp_item[2] = "\""+str(eachattr[1])+"\""
            if 'H' in eachattr[6]:
                temp_item[8] = "\""+str(re.sub('[^\d\.]', '', eachattr[6]))+"\""
            else:
                temp_item[8] = "\""+"\""
            tempstring = ','.join(map(str,temp_item))
            finallist.append(tempstring)
            c_count = c_count + 1
string1 = "\""+ r"""4001","Channel VFO A","140.00000","140.00000","A-Analog","Turbo","25K","Off","Off","Contact1","Group Call","12345678","My Radio","Off","Carrier","Off","1","1","1","Off","1","1","None","Group List 1","Off","Off","Off","Off","Normal Encryption","Off","Off","Off","Off","131.8","1","Off","Off","Off","Off","Off","Off","1","0","Off","0","1","1","0","0","0","0","0""" + "\""
string2 = "\""+ r"""4002","Channel VFO B","145.12500","145.12500","D-Digital","Turbo","25K","Off","Off","Contact1","Group Call","12345678","My Radio","Always","Carrier","Off","1","1","1","Off","1","1","None","Group List 1","Off","Off","Off","Off","Normal Encryption","Off","Off","Off","Off","131.8","1","Off","Off","Off","Off","Off","Off","1","0","Off","0","1","1","0","0","0","0","0""" + "\""
with  open("anytone878.csv", "w") as f:
    f.write(titlestring)
    for items in finallist:
        f.write(items)
        #f.write("\n")

    f.write(string1)
    f.write("\n")
    f.write(string2)






