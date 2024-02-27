def remove_item(item,container,multi = True):
#---------------------------------------
    if type(container) == list:
        if multi:
            while item in container:
                container.remove(item)
        else:
            container.remove(item)
        return container
#---------------------------------------
    elif type(container) == dict:
        if multi:
            while item in container:
                del container[item]
        else:
            del container[item]
        return container
#---------------------------------------
    elif type(container) == set:
        if multi:
            while item in container:
                container.remove(item)
        else:
            container.remove(item)
        return container
#---------------------------------------
    elif type(container) == tuple:
        container = list(container)
        if multi:
            while item in container:
                container.remove(item)
        else:
            container.remove(item)
        container = tuple(container)
        return container
