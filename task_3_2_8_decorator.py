class HandlerGET:
    def __init__(self, func):
        self.__f = func

    @staticmethod
    def get(func, request, *args, **kwargs):
        res = func(request)
        if "method" not in request:
            return f"GET: {res}"
        else:
            if request["method"] == "GET":
                return f"GET: {res}"
            else:
                return None

    def __call__(self, request):
        return self.get(self.__f, request)


@HandlerGET
def contact(request):
    return "Сергей Балакирев"


print(type(contact))
print(dir(contact))
res = contact({"method": "GET", "url": "contact.html"})
res = contact({"method": "POST", "url": "contact.html"})
print(res)
