## Data Structures =================
## Lists ---------------------------
# mbti = ['INTJ', 'ENFP', 'ISTJ', 'ESTP']
# # get
# print(mbti)         # print the list
# print(mbti[0])      # print the value sitting on the index

# ## for python, can be assigned different data type but it should cause problems.
# my_list = [123, 'apple']
# print(my_list)

colors = ['red', 'blue', 'green']
# get
print(colors[0])
# modify
colors[0] = 'black'
print(colors[0])
# add
colors.append('white')
colors.insert(1, 'purple')  # position where you want to insert a new value, new value
print(colors)
# delete
del colors[0]
print(colors)
## pop = will return the value removed.
del_color = colors.pop()    # without index, the last value will be removed. 
print(colors)
del_color = colors.pop(0)
print(colors)

## ---------------------------



