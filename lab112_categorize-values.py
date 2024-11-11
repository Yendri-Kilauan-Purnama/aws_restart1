# For Loop
print('\nFor Loop:')
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45", "True"]
for item in myMixedTypeList:
    #print("{} is of the data type {}".format(item,type(item)))
    
    #lebih mudah pakai ini untuk newbie :
    print(f"{item} is of the data type {type(item)}")
    
    #bisa juga seperti ini, tapi cape [print satu satu. makanya gunanya for loop
    print()
    print(f"{myMixedTypeList[0]} is of the data type {type(myMixedTypeList[0])}")
    print(f"{myMixedTypeList[1]} is of the data type {type(myMixedTypeList[1])}")
    print(f"{myMixedTypeList[2]} is of the data type {type(myMixedTypeList[2])}")
    print(f"{myMixedTypeList[3]} is of the data type {type(myMixedTypeList[3])}")
    print(f"{myMixedTypeList[4]} is of the data type {type(myMixedTypeList[4])}")
    print(f"{myMixedTypeList[5]} is of the data type {type(myMixedTypeList[5])}")
    print(f"{myMixedTypeList[6]} is of the data type {type(myMixedTypeList[6])}")

# 45 disimpan didalam variabel item, cetak angka 45 dan type datanya
# 290578 disimpan didalam variabel item, cetak angka 290578 dan type datanya". dst...
