# mynie
Add your own parser to Genie Parser.

# Install

```
# pip3 setup.py install
```

```
$ python3
>>> from genie.libs.parser.utils.common import parser_data
>>> print(parser_data["date"])
{'linux': {'module_name': 'date', 'package': 'mynie.parser.linux', 'class': 'LinuxDate'}, 'myos': {'module_name': 'date', 'package': 'mynie.parser.myos', 'class': 'MyOsDate'}}
>>> print(parser_data["free"])
{'linux': {'module_name': 'free', 'package': 'mynie.parser.linux', 'class': 'LinuxFree'}, 'myos': {'module_name': 'free', 'package': 'mynie.parser.myos', 'class': 'MyOsFree'}}
```

# Example

test.py

```python
from genie.conf.base import Device
from genie.libs.parser.utils import get_parser
from pyats.datastructures import AttrDict
import pprint

device = Device("new_device", os="myos")
device.custom.setdefault("abstraction", {})
device.custom["abstraction"]["order"] = ["os"]
device.cli = AttrDict({"execute":None})

raw_output = "Sat Mar 28 16:01:19 JST 2020"

get_parser("date", device)
schema_output = device.parse("date", output=raw_output)

pprint.pprint(schema_output)
```

```
$ python3 test.py
{'day': '28',
 'dayofweek': 'Sat',
 'month': 'Mar',
 'time': '16:01:19',
 'timezone': 'JST',
 'year': '2020'}
```

