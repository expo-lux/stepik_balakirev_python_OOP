class Router:
    app = {}

    @classmethod
    def get(cls, path):
        return cls.app.get(path)

    @classmethod
    def add_callback(cls, path, func):
        cls.app[path] = func

# здесь объявляйте декоратор Callback
class Callback:
    def __init__(self, path: str, router: Router):
        self.__path = path
        self.__router = router

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            self.__router.add_callback(self.__path, func)
        return wrapper()

@Callback('/', Router)
def index():
    return '<h1>Главная</h1>'


route = Router.get('/')
if route:
    ret = route()
    print(ret)