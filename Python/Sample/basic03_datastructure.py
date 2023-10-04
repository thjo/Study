## Data Structures =================
## Lists ---------------------------
# mbti = ['INTJ', 'ENFP', 'ISTJ', 'ESTP']
# # get
# print(mbti)         # print the list
# print(mbti[0])      # print the value sitting on the index

# ## for python, can be assigned different data type but it should cause problems.
# my_list = [123, 'apple']
# print(my_list)

# colors = ['red', 'blue', 'green']
# # get
# print(colors[0])
# # modify
# colors[0] = 'black'
# print(colors[0])
# # add
# colors.append('white')
# colors.insert(1, 'purple')  # position where you want to insert a new value, new value
# print(colors)
# # delete
# del colors[0]
# print(colors)
# ## pop = will return the value removed.
# del_color = colors.pop()    # without index, the last value will be removed. 
# print(colors)
# del_color = colors.pop(0)
# print(colors)
# colors.remove('blue')   # by a value to remove an item
# print(colors)
# ## ---------------------------

# ## sort - list
# colors = ['blue','red','gray','black','white','yellow']
# colors.sort()   ## 오름차순 원본 데이터 변경
# colors.sort(reverse=True)   ##내림차순
# print(colors)
# sorted_colors = sorted(colors)  ##정렬한 결과 반환

# ## length 
# print(len(colors))

# ## 맨 마지막 index에 존재하는 값은 -1로 접근할 수 있음
# print(colors[-1])


# ## extract data from list ----------------
# colors = ['blue','red','gray','black','white','yellow']
# print(colors[1:5])  ## inclusive the first index, exclusive the last index
# print(colors[:4])   ## from the 0 index until 4 index
# print(colors[2:])   ## start the value sitting on index 2 until in the end.
# print(colors[-1])   ## 맨 마지막 인덱스의 값
# print(colors[-5])   ## -1이 맨 마지막이고 앞으로 한칸씩 이동 시 -1씩하면됨

# ## copy
# colors2 = colors[:] ## 전체 값을 선택하여 반환 - copy 
# print(colors2)


## access each item
scores = [88, 100, 96, 43, 65, 77, 45]
scores.sort(reverse=True)
#print(scores)
# for score in scores:
#     if score >= 80:
#         print(score)
#     else:
#         print("Fail")

# ## max, min, average
# max_val = max(scores)
# min_val = min(scores)
# sum_val = sum(scores)
# avg_val = sum(scores) / len(scores)


# ## Tuples ==========================
# ## 각각의 값 변경 불가 
# tup = (1, 20, 40, "asdf")
# # print(tup[0])
# # tup[0] = 100
# for x in tup:
#     print(x)

# ## 리스트로 변환 - 1
# list_1 = list(tup)
# ## 리스트로 변환 - 2
# list_2 = [x for x in tup]
# ## 리스트로 변환 - 3
# list_3 = []
# for x in tup:
#     list_2.append(x)



## Dictionaries ======================
# student = {
#     "student_no" : "1",
#     "major": "English",
#     "grade": 1
# }
## add - student["<new key>"] = <value>
## get - student["<key>"]
## modify - student["<key>"] = <value>
## delete - del student["<key>"]
# student["gpa"] = 4.5
# student["student_no"] = "2001321993"
# del student["grade"]
# print(student);

## functions ------
## 1) access a value - get("<key>", ["default_value"])
##   - if the key doesn't exist, None will be return 
#print(student.get("new_grade", "default"))
## 2) return all keys - keys()
##   - convert the return value to list 
##         list(student.keys())
#print(list(student.keys()))
## 3) return all values - values()
#print(list(student.values()))
## 4) return all keys and values - items()
# for key, value in student.items():
#     print(f'{key} - {value}')
## 5) Nesting 
## 5-1) List - Dictionary
# student_1 = {
#     "s_no" : 1
#     ,"name": "John"
#     ,"gpa" : 4.3
# }
# student_2 = {
#     "s_no" : 2
#     ,"name": "Jessica"
#     ,"gpa" : 4.5
# }
# students = [student_1, student_2]
# print(students)
# for student in students:
#     student["graduated"] = False
#     print(student)
## 5-1) Dictionary - List
student = {
    'subjects': ["Math", "English", "Computer Science"]
    ,'name': "John"
}
print(student)
for sub in student["subjects"]:
    print(sub)




