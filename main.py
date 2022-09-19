# Адаптер
# Адаптер от старого телевизора к новому

class OldTV:
    def get_old_screen_resolution(self):
        return 180

    def use_internet(self):
        return 'No'

    def old_tv_kontrol(self):
        return 'Only with remote control'


class SmartTV:
    def get_new_screen_resolution(self):
        return '4K'

    def use_inretnet_services(self):
        return ['YouTube', 'HBO', 'Netflix', 'Кинопоиск']

    def new_tv_kontrol(self):
        return 'You can use remote contol and voice'


class SetTopBox(SmartTV):
    def get(self):
        return self.get_new_screen_resolution()

    def getInternet(self):
        return self.use_inretnet_services()

    def getControl(self):
        return self.new_tv_kontrol()


def new(obj):
    print(f"Стало:\nКачество: {obj.get()} \nДоступные интернет сервисы: {obj.use_inretnet_services()} \n"
          f"Способы управления: {obj.new_tv_kontrol()}")


def old(objj):
    print(
        f"Было: \nКачество: {objj.get_old_screen_resolution()} \nВозсожность использования интернета: {objj.use_internet()}\n"
        f"Способы управления: {objj.old_tv_kontrol()}")


if __name__ == '__main__':
    objj = OldTV()
    obj = SetTopBox()
    old(objj)
    print()
    new(obj)
