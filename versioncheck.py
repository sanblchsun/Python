import sys, warnings

if sys.version_info[0] < 3:
	warnings.warn('Для выполнения этой программы необходимо\
	 как минимум версия Python 3.0', RuntimeWarning)
else:
	print(sys.version_info)
