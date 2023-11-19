users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
dict_ = {
    "Общее количество": "",
    "Уникальные посещения": ""
}
total = len(users)
dict_["Общее количество"] = total
users_unik = set(users)
count = len(users_unik)
dict_["Уникальные посещения"] = count

print(dict_)
