class Item:
    '''Предмет в инвентаре'''
    name = ''
    type = ''
    props = None

def make_item(name, type_, props):
    '''Создать предмет'''
    item = Item()
    item.name = name
    item.type = type_
    item.props = props
    return item

def item_str(item):
    '''Печать одного предмета строкой'''
    if not item.props:
        return item.name + ' [' + item.type + ']'
    parts = []
    for key in item.props:
        parts.append(key + '=' + str(item.props[key]))
    return item.name + ' [' + item.type + '] (' + ', '.join(parts) + ')'

def inventory_str(inv):
    '''Печать всего инвентаря одной строкой'''
    if not inv:
        return '[]'
    parts = []
    for item in inv:
        parts.append(item_str(item))
    return '[' + ', '.join(parts) + ']'
