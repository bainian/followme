import json

from Project.Car import Car

str = '[  {    "YYRQ": "20170316",    "XNSD": "2001",    "CNBH": "05153",    "SFSBB": "0"  },' \
      '{    "YYRQ": "20170316",    "XNSD": "2002",    "CNBH": "05154",    "SFSBB": "0"  }]_0'
str = str[0:len(str) - 2]
print(str)

dump = json.dumps(str)
print(dump)

load = json.load(dump, object_hook=Car.car2dict)
print(load)
