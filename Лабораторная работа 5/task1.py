from pprint import pprint

end_number = 15
pprint([{'bin': bin(number), 'dec': number, 'hex': hex(number), 'oct': oct(number)} for number in range(end_number + 1)])
