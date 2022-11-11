from pprint import pprint


pprint([{'bin': bin(num), 'oct': oct(num), 'dec': num, 'hex': hex(num)} for num in range(16)])
