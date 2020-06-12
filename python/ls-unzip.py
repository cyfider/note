import glob
import re
import os

for f in os.listdir('.'):
	m = re.search(r'(.*)\.zip', f)
	if (m):
		print('unzip {} -d {}'.format(m.group(), m.group(1)))
		os.system('unzip {} -d {} >> /dev/null'.format(m.group(), m.group(1)))
