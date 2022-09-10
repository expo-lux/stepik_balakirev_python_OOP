# здесь объявляются все необходимые классы
class Graph:
    def __init__(self, data):
        self.data = data.copy()
        self.is_show = True

    def set_data(self, data):
        self.data = data.copy

    def show_table(self):
        if self.is_show:
            print(*self.data)
        else:
            print("Отображение данных закрыто")

    def show_graph(self):
        if self.is_show:
            print("Графическое отображение данных:", *self.data)
        else:
            print("Отображение данных закрыто")

    def show_bar(self):
        if self.is_show:
            print("Столбчатая диаграмма:", *self.data)
        else:
            print("Отображение данных закрыто")

    def set_show(self, fl_show):
        self.is_show = fl_show

# считывание списка из входного потока (эту строку не менять)
data_graph = list(map(int, input().split()))
# здесь создаются объекты классов и вызываются нужные методы
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()
