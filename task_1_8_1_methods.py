def debug(*dec_args):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(*dec_args)
            func(*args, **kwargs)
        return wrapper
    return decorator


class Data:
    def __init__(self, data: str, ip: int):
        self.data = data
        self.ip = ip

class Server:
    IP = 0

    @classmethod
    def request_IP(cls):
        cls.IP = cls.IP + 1
        return cls.IP

    def __init__(self):
        self.IP = self.request_IP()
        self.buffer = []
        self.router = None

    def send_data(self, data: Data):
        """Отправляет информационный пакет data с указанным IP-адресом получателя роутеру"""
        if self.router:
            self.router.receive_data(data)

    def receive_data(self, data: Data):
        self.buffer.append(data)

    def get_data(self) -> list:
        """Возвращает список принятых пакетов и очищает входной буфер"""
        temp = self.buffer.copy()
        self.buffer.clear()
        return temp

    def get_ip(self):
        """Возвращает IP сервера"""
        return self.IP


class Router:
    def __init__(self):
        self.buffer = []
        self.servers = {}

    def link(self, server: Server):
        """Присоединяет сервер к роутеру"""
        server.router = self
        self.servers[server.get_ip()] = server

    def unlink(self, server: Server):
        """Отсоединяет сервер от роутера"""
        server.router = None
        self.servers.pop(server.get_ip())

    def receive_data(self, data: Data):
        """Принять пакет data - положить его в буфер"""
        self.buffer.append(data)

    def send_data(self):
        """Отправка всех пакетов серверам и очистка буфера"""
        while self.buffer:
            packet = self.buffer.pop()
            if packet.ip in self.servers:
                self.servers[packet.ip].receive_data(packet)


router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data(f"Hello from {sv_from.get_ip()}", sv_to.get_ip()))
sv_from2.send_data(Data(f"Hello from {sv_from2.get_ip()}", sv_to.get_ip()))
sv_to.send_data(Data(f"Hi from {sv_to.get_ip()}", sv_from.get_ip()))
router.send_data()
print(f"{sv_from.get_ip()} received ", sv_from.get_data())
print(f"{sv_to.get_ip()} received ", sv_to.get_data())