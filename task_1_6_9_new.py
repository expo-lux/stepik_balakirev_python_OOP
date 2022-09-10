TYPE_OS = 1  # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:
    def __new__(cls, name):
        if TYPE_OS == 1:
            obj = DialogWindows()
        else:
            obj =  DialogLinux()
        obj.name = name
        return obj

    def __init__(self, name):
        self.name = name

TYPE_OS = 1
dlg_1 = Dialog("123")
TYPE_OS = 2
dlg_2 = Dialog("1234")
print(type(dlg_1))
print(dlg_1.name)