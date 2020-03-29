import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

__all__ = ['LinuxFree']

class LinuxFreeSchema(MetaParser):
    schema = {
        Any(): {
            'mem': {
                'total': int,
                'used': int,
                'free': int,
                'shared': int,
                'buffcache': int,
                'available': int,
            },
            'swap': {
                'total': int,
                'used': int,
                'free': int,
            },
        }
    }

    cli_command = ["free"]

class LinuxFree(LinuxFreeSchema):

    def cli(self, output=None, **kwargs):

        if output is None:
            cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        result_dict = dict()

        p1 = re.compile(r'^(?P<kind>Mem): +(?P<total>\d+) +(?P<used>\d+) +'
                         '(?P<free>\d+) +(?P<shared>\d+) +(?P<buffcache>\d+) +'
                         '(?P<available>\d+)')
        
        p2 = re.compile(r'^(?P<kind>Swap): +(?P<total>\d+) +(?P<used>\d+) +'
                         '(?P<free>\d+)')
        
        for line in out.splitlines():
            line = line.replace('\t', '    ')
            line = line.strip()
        
            if not line:
               continue
        
            m = p1.match(line)
            if m:
                group = m.groupdict()
                mem = group['kind']
                mem_dict = result_dict.setdefault(mem, {})   
                mem_dict.update({k: (int(v) if v.isdigit() else v) for k, v in group.items()})
            
            m = p2.match(line)
            if m:
                group = m.groupdict()
                swap = group['kind']
                swap_dict = result_dict.setdefault(swap, {})   
                swap_dict.update({k: (int(v) if v.isdigit() else v) for k, v in group.items()})
        
                return result_dict 
