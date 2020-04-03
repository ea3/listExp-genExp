import array

# Cartesian product using a list comprehension

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

for color in colors:
    for size in sizes:
        print((color, size))

tshirts = [(color, size) for size in sizes for color in colors]
print(tshirts)

# Using a genexp to generate a tuple
symbols = 'ÓÔÕÖ×ØÙÚÛÜÝ'
tuple1 = tuple(ord(symbol) for symbol in symbols)
print(tuple1)

array1 = array.array('I', (ord(symbol) for symbol in symbols))
print(array1)

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)
