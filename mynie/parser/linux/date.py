"""
output = Sat Mar 28 13:11:17 JST 2020

schema_output = "{dayofweek:Sat, month:Mar, day:28, time:13:11:17, timezone:JST, year:2020}"
"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

__all__ = ['LinuxDate']

class LinuxDateSchema(MetaParser):
    schema = {
        Any(): {
            'dayofweek': str,
            'month': str,
            'day': str,
            'time': str,
            'timezone': str,
            'year': str,
        }
    }

    cli_command = ["date"]

class LinuxDate(LinuxDateSchema):

    def cli(self, output=None, **kwargs):
        if output is None:
            cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        schema_output = dict()

        p = re.compile(r'^(?P<dayofweek>\S+) +(?P<month>\S+) +(?P<day>\S+) '
                        '+(?P<time>\S+) +(?P<timezone>\S+) +(?P<year>\S+)')
        m = p.match(out)

        schema_output.update(m.groupdict())

        return schema_output
