def create_phone_number(n):
    return f'({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}'

def create_phone_number(n):
    return f"({''.join(map(str, n[:3]))}) {''.join(map(str, n[3:6]))}-{''.join(map(str, n[6:]))}"

def create_phone_number(n):
	return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

def create_phone_number(n):
    n = ''.join(map(str,n))
    return '({}) {}-{}'.format(n[:3], n[3:6], n[6:])

