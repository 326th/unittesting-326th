def unique(lst):
    '''Return a list containing only the first occurence of each distint
       element in list.  That is, all duplicates are omitted.

    Arguments:
        list: a list of elements (not modified)
    Returns:
        a new list containing only distinct elements from list

    Examples:
    >>> unique([5])
    [5]
    >>> unique(['b','a','a','b','b','b','a','a'])
    ['b', 'a']
    >>> unique([])
    []
    '''
    if type(lst) is not list:
        raise ValueError(f"{lst} isn't a list")
    result = []
    while len(lst)>0:
        if lst[0] not in result:
            result.append(lst[0])
        lst.remove(lst[0])
    return result

if __name__ == '__main__':
    '''Run the doctests in all methods.'''
    import doctest
    doctest.testmod(verbose=True)
