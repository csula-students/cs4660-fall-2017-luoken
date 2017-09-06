"""Lists defines simple list related operations"""

def get_first_item(li):
    """Return the first item from the list"""
    return li[0]
    pass

def get_last_item(li):
    """Return the last item from the list"""
    return li[-1]
    pass

def get_second_and_third_items(li):
    """Return second and third item from the list"""
    return li[1:3]
    pass

def get_sum(li):
    """Return the sum of the list items"""
    holder = 0
    for i in li:
        holder = holder + i
    return holder
    pass

def get_avg(li):
    """Returns the average of the list items"""
    holder = 0
    for i in li:
        holder = holder + i
    answer = holder / len(li)
    return answer
    pass
