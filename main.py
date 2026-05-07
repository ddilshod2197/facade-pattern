# Adapter pattern
class Avto:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def start(self):
        return f"{self.marka} {self.model} boshlandi"

    def stop(self):
        return f"{self.marka} {self.model} to'xtadi"


class Toyota:
    def __init__(self):
        pass

    def start(self):
        return "Toyota boshlandi"

    def stop(self):
        return "Toyota to'xtadi"


class AvtoAdapter:
    def __init__(self, toyota):
        self.toyota = toyota

    def start(self):
        return self.toyota.start()

    def stop(self):
        return self.toyota.stop()


class ToyotaAdapter:
    def __init__(self, avto):
        self.avto = avto

    def start(self):
        return self.avto.start()

    def stop(self):
        return self.avto.stop()


avto = Avto("Toyota", "Camry")
toyota = Toyota()

avto_adapter = AvtoAdapter(toyota)
toyota_adapter = ToyotaAdapter(avto)

print(avto_adapter.start())  # Toyota boshlandi
print(avto_adapter.stop())   # Toyota to'xtadi

print(toyota_adapter.start())  # Toyota boshlandi
print(toyota_adapter.stop())   # Toyota to'xtadi
