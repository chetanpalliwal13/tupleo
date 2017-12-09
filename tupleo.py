"""
tupleo1.0
Python Package which provide interface to do operation on tuple which not permitted in python to do.
e.g tuple modification, insert element in tuple, remove elemnt from tuple.
This package also provide converstion from tuple, list or tuple and tuple or tuple to list and dictionary format.
"""

def insert(index, value, tupleo):
    """
	insert(...) method of tupleo.tuple instance
    T.insert(index, object, tupleo)  -- insert object before index
	"""
    if type(tupleo) != tuple:
        raise TypeError("{} is not tuple".format(tupleo))
    convertlist = list(tupleo)
    convertlist.insert(index, value)
    return tuple(convertlist)
	
def append(value, tupleo):
    """
	append(...) method of tupleo.tuple instance
    T.append(object, tupleo) -> None -- append object to end of tupleo
	"""
    if type(tupleo) != tuple:
        raise TypeError("{} is not tuple".format(tupleo))
    convertlist = list(tupleo)
    convertlist.append(value)
    return tuple(convertlist)

def clear(tupleo):
    """
	clear(...) method of tupleo.tuple instance
    T.clear(tupleo) -> None -- Remove all elements from tupleo
	"""
    if type(tupleo) != tuple:
        raise TypeError("{} is not tuple".format(tupleo))
    convertlist = list(tupleo)
    convertlist.clear()
    return tuple(convertlist)
	
def copy(tupleo):
    """
	clear(...) method of tupleo.tuple instance
    T.copy(tupleo) -> Tuple -- a shallow copy of tupleo
	"""
    if type(tupleo) != tuple:
        raise TypeError("{} is not tuple".format(tupleo))
    convertlist = list(tupleo)
    return tuple(convertlist.copy())
	
def extend(value, tupleo):
    """
	extend(...) method of tupleo.tuple instance
    T.extend(iterable, tupleo) -> None -- extend tuple by appending elements from the iterable
	"""
    if type(tupleo) != tuple:
        raise TypeError("{} is not tuple".format(tupleo))
    if type(value) !=tuple:
	    raise TypeError("{} is not tuple".format(value))
    convertlist = list(tupleo)
    convertlist.extend(list(value))
    return convertlist
	
def pop(tupleo, *index):
    """
	pop(...) method of tupleo.tuple instance
    T.pop(tupleo, index) -> item -- remove and return item at index (default last).
	Raises IndexError if list is empty or index is out of range
	"""
    if type(tupleo) != tuple:
        raise TypeError("{} is not tuple".format(tupleo))
    convertlist = list(tupleo)
    if index:
        convertlist.pop(*index)
    else:
	    convertlist.pop(len(convertlist)-1)
    return tuple(convertlist)
	
def remove(value, tupleo):
    """
	remove(...) method of tupleo.tuple instance
    T.remove(value, tupleo) -> None -- remove first occurrence of value.
	Raises ValueError if the value is not present
	"""
    if type(tupleo) != tuple:
        raise TypeError("{} is not tuple".format(tupleo))
    convertlist = list(tupleo)
    convertlist.remove(value)
    return tuple(convertlist)
	
def reverse(tupleo):
    """
	reverse(...) method of tupleo.tuple instance
    T.reverse(tupleo) -- reverse *IN PLACE*
	"""
    if type(tupleo) != tuple:
        raise TypeError("{} is not tuple".format(tupleo))
    return tupleo[::-1]
	
def sort(tupleo, key=None, reverse=False):
    """
	sort(...) method of tupleo.tuple instance
    T.sort(tupleo, key=None, reverse=False) -> None -- stable sort *IN PLACE*
	"""
    if type(tupleo) != tuple:
        raise TypeError("{} is not tuple".format(tupleo))
    convertlist = list(tupleo)
    convertlist.sort(key=key, reverse=reverse)
    return tuple(convertlist)