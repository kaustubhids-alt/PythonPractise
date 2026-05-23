a = "I live in Jaipur which is in india"
b = a.split()

print(f"My tuple is: {a}")
['I', 'live', 'in', 'Jaipur', 'which', 'is', 'in', 'india']
c = tuple(b)
('I', 'live', 'in', 'Jaipur', 'which', 'is', 'in', 'india')

print( c.count("in") )

print(a.count("in"))