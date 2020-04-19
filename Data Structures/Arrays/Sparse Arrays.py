import re

no_strings = int(input())
strings = []
no_q = 0
queries = []

for _ in range(no_strings):
    strings.append(input())

no_q = int(input())
for _ in range(no_q):
    queries.append(re.compile(r'^'+input()+'$'))

for pattern in queries:
    found = 0
    for s in strings:
        found += len(pattern.findall(s))
    print(found)
