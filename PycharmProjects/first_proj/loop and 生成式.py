accusation={"room":"ballroom","weapon":"lead pipe",
            "person":"Cal. Mustard"}
days=["monday","tuesday","wensday","thrsday"]
color=["Red","Green","Blue","Black"]
drink=["Coffee","Tea","Cola","Wind"]

for days,colors,drinks in zip(days,color,drink):
    print("Day: ",days,"color: ",colors,"drink: ",drinks)


#list
odd_list=[(row,col) for row in range(1,4) for col in range(1,3)]
for odd_lists in odd_list:
    print(odd_lists)
for row,col in odd_list:
    print(row,col)

#set
word="More And More"
letter_count={letter:word.count(letter) for letter in set(word) if letter!=' '}
print(letter_count)
word2=set(word)
print(word2)

#tuple 產生器生成式（動態產生 只可使用一次）
number_list=(number for number in range(1,10))
print(number_list)

#num_list=list(number_list)
#print(num_list)

for number in number_list:
    print(number)


