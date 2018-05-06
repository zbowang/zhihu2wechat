import os
from settings import CHECK_URLNAME, CHECK_TOKENNAME, CHECK_INFONAME

json_files = [CHECK_URLNAME, CHECK_TOKENNAME, CHECK_INFONAME]
for file in json_files:
	if os.path.isfile(file):
		os.remove(file)