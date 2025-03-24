#data are set in form of collection
#example list. dictionary, sets

scores =[78,45,54,78,98,23,46,56,76,12,96,36,86,67]

print(scores[0])
print(scores[1])

#how to add a score to my list u do
scores.append(51)
print(scores)

#to remove a score
scores.remove(12)
print(scores)

print( len(scores))#how many scores  have
print(scores.count(76))#to count how many ppl scored 12f;

scores.sort()#arranging in an ascending oder from smallest to largest
print(scores)

scores.sort(reverse=True)#sort descending manner from largest to smallest
print(scores)

#slice is cutting
top_5 = scores[1:5]#if put a number before the colon the numbers will arrange themselves from one upto four the fifth number will be executed
print(top_5)
top_5 = scores[-5:]#getting the last five
print(top_5)



#dictonary
person={"name":"Amina","age":19,"weight":58,"county":"New York"}
print(person["name"])
print(person["age"])
print(person["weight"])
print(person["county"])


#set
days ={"mon","tue","wed","thur","fri","sat","sun","mon"}
print(days)

for s in scores:#for each score in scores
    if s <50:
        pass
    print(s)

for d in days:
    print(d)
























