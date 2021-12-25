from struct import *


class eZstruct:
    fmt = None
    all_items = []

    def __init__(self, fmt):
        self.fmt = fmt

        
    def _pack(self, *items):
        items = list(items)
        for a in range(0, len(items)):
            items[a] = bytes(items[a], 'utf-8')   
        items.insert(0, self.fmt)
        struct_item = pack(*(items))
        self.all_items.append(struct_item)
        return struct_item


    def _unpack(self, struct_item):
        items = list(unpack(self.fmt, struct_item))
        for a in range(0, len(items)):
            items[a] = items[a].decode('utf-8').replace("\x00"," ")
        return items   

    def _get(self):
        all_items = []
        for a in self.all_items:
            all_items.append(self._unpack(a))
        return all_items
    
    def _change_fmt(self, new_fmt):
        self.fmt = new_fmt
