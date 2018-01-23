def number_of_groups(n, l): #n is the number of groups desired,
    d = (len(l)//n)
    return students_per_group(d, l)

def students_per_group(n, l): #n is the number of students per group desired
    return [l[x:x+n] for x in range(0, len(l), n)]

def clean_list(l):
	return [name for name in l if name not in ['', '\r', '\n', '\r\n']]

def clean_name(name):
	temp = name.split(',')
	return ' '.join(reversed(temp))