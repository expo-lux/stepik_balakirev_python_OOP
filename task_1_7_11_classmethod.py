class Application:
    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked

class AppStore:
    apps = set()

    def add_application(self, app):
        self.apps.add(app)

    def remove_application(self, app):
        self.apps.remove(app)

    def block_application(self, app):
        app.blocked = True

    def total_apps(self):
        return len(self.apps)


x = AppStore()
a1 = Application("Telegram")
a2 = Application("AlfaBank")
a3 = Application("AlfaBank")
x.add_application(a1)
x.add_application(a2)
print(x.total_apps())
x.remove_application(a2)
print(x.total_apps())
