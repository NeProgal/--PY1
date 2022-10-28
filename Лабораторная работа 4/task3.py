def delete(list_, index=None):
    list_[index] = "del_"
    list_.remove("del_")
    return list_[:-1]


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4], index=4))  # [0, 1, 2, 3]
