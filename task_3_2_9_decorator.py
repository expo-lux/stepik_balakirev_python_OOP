class Handler:
    def __init__(self, methods=('GET',)):
        self.__static_methods = {"GET": self.get, "POST": self.post}
        self.__methods = methods

    @staticmethod
    def get(func, request, *args, **kwargs):
        return f"GET: {func(request)}"

    @staticmethod
    def post(func, request, *args, **kwargs):
        return f"POST: {func(request)}"

    def __call__(self, func):
        def wrapper(request: dict):
            method = request.get("method", "GET")
            if method in self.__methods:
                return self.__static_methods[method](func, request)
            else:
                return None

        return wrapper


@Handler(methods=('GET', 'POST'))  # по умолчанию methods = ('GET',)
def contact(request):
    return "Сергей Балакирев"


res = contact({"method": "POST", "url": "contact.html"})
print(res)
