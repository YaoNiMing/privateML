"""
>>> pairs_for(['Andrea', 'Bob', 'Cassandra', 'Doug'])
# [[('Bob', 'Cassandra'), ('Andrea', 'Doug')],
#  [('Andrea', 'Bob'), ('Cassandra', 'Doug')],
#  [('Andrea', 'Cassandra'), ('Bob', 'Doug')]]
"""


def pairs_for(names):
    n = len(names)
    assert n % 2 == 0
    result = []
    first = names[:n/2]
    second = names[n/2:]
    for _ in range(n-1):
        second.append(first.pop())
        first.insert(1, second.pop(0))
        result.append(zip(first, second))
    return result

print pairs_for(['Andrea', 'Bob', 'Cassandra', 'Doug'])
