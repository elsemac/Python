school = [
    {'school_class': '4a', 'scores': [4,5,4,5,5]}, 
    {'school_class': '4b', 'scores': [3,4,4,5,4]}, 
    {'school_class': '4c', 'scores': [2,3,3,4,2]},
]

# allschool = sum([sum(item['scores']) for item in school])
# number_children = sum([len(item['scores']) for item in school])
# school_overall = allschool / number_children
# print(school_overall)

classes_scores = dict() 

for item in school:
    # print(sum(item["scores"]))
    classes_scores[item["school_class"]] = sum(item["scores"]) / len(item["scores"])     

print(classes_scores)

for item in classes_scores.items():
    print(item[0], item[1])

