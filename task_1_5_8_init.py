class CPU:
    def __init__(self, name, frequency):
        self.name = name
        self.fr = frequency


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, *memory):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = list(memory[:4])

    def get_config(self):
        s_mb = f"Материнская плата: {self.name}"
        s_cpu = f"Центральный процессор: {self.cpu.title}, {self.cpu.fr}"
        s_slots = f"Слотов памяти: {self.total_mem_slots}"
        s_mem = 'Память: ' + '; '.join([f"{i.title} - {i.volume}" for i in self.mem_slots])
        return [s_mb, s_cpu, s_slots, s_mem]

cpu = CPU('AMD 7900', 5000)
mem1, mem2 = Memory('Kingstone', 16384), Memory('Kingstone', 16384)
mb = MotherBoard('Asus', cpu, mem1, mem2)
print(mb.get_config())