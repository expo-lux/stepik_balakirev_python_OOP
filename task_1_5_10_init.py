import sys

class ListObject:
    def __init__(self, data):
        self.data = data
        self.next_obj = None

    def link(self, obj):
        self.next_obj = obj


lst_in = list(map(str.strip, sys.stdin.readlines()))
head_obj = ListObject(lst_in[0])
prev_obj = head_obj
for line in lst_in[1:]:
    obj = ListObject(line)
    prev_obj.link(obj)
    prev_obj = obj
