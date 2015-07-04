import random
import sys

n = int(sys.argv[1])

lines = [line.rstrip('\n') for line in open('users.txt')]

for x in range(0, n):

	name = lines.pop(random.randrange(len(lines)))

	print(name)

	with open('roster.txt', 'a') as f:
		f.write("%s\n" % name)


with open('users.txt', 'w') as f:
	for item in lines:
		f.write("%s\n" % item)

print('wrote %d lines' % n)