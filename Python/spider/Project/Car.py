class Car:
    def __init__(self, YYRQ, XNSD, CNBH, SFSBB):
        self.SFSBB = SFSBB
        self.YYRQ = YYRQ
        self.XNSD = XNSD
        self.CNBH = CNBH

    def car2dict(std):
        return {
            'YYRQ': std.YYRQ,
            'XNSD': std.XNSD,
            'CNBH': std.CNBH,
            'SFSBB': std.SFSBB
        }
