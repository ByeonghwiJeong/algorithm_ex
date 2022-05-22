from collections import Counter

a = [2, 2, 1, 1, 1, 3]
d = {}
for i in a:
  try:
    if d[i]:
     d[i] += 1
  except KeyError:
    d[i] = 1

print(d)
print()

c = Counter(a)

print(dict(c))