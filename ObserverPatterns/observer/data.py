
from collections import namedtuple
from itertools import starmap

data = (('new', 10), ('open', 20), ('closed', 20))

nt = namedtuple('KPI', 'name value')
KPI_DATA = starmap(nt, data)