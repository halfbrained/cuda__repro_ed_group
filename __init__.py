import os
from cudatext import *

"""
on CudaText startup, if have several tabs opened, `group_ed()` result is always first tab's Editor
"""

class Command:
    
    def on_open(self, ed_self):
        group_ed = ed_group(0)
        print(f'on_open: ed_self:{ed_self};   group_ed:{group_ed}')
