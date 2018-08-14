def add_memberwise(list_1, list_2):
    """Merges 2 lists together by adding each of their respective indexes together"""
    new_list = []
    for x in range(min(len(list_1), len(list_2))):
        new_list.append(list_1[x] + list_2[x])
    if len(list_1) > len(list_2):
        for x in range(len(list_2), len(list_1)):
            new_list.append(list_1[x])
    else:
        for x in range(len(list_1), len(list_2)):
            new_list.append(list_2[x])
    return new_list
