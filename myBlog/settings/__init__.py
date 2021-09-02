import os

if os.environ.get('ENV') == 'PROD':
   from .prod import *
else:
   from .local import *