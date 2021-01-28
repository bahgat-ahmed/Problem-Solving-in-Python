import re

print(len(set(filter(None, re.split(',| ', input()[1:-1])))))
