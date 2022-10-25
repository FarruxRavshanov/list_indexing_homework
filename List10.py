def main(list_num):
    """
    A list of numbers consisting of several elements is given. Return the largest between the first and last elements.
    Args:
        list_num (list): parameter
    Returns:
        int: return answer
    """
    a = list_num[0]
    b = list_num[-1]
    d = 0
    if a > b:
        d = a
    else:
        d = b
    return d