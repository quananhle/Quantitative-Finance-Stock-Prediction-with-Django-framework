#!d:\projects\django\mysite\.venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'spyne==2.14.0','console_scripts','sort_wsdl'
__requires__ = 'spyne==2.14.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('spyne==2.14.0', 'console_scripts', 'sort_wsdl')()
    )
