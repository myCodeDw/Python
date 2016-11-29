def sanitize(time_string):
    if '-' in time_string:
        splitter= '-'
    elif ':' in time_string:
        splitter= ':'
    else:
        return(time_string)
    (mins,secs)= time_string.split(splitter)
    return(mins+'.'+secs)
'''
class Athlete :
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times= a_times

    def top3(self):
        return(sorted(set([sanitize(t) for t in self.times]))[0:3])

'''
class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return(sorted(set([sanitize(t) for t in self]))[0:3])

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        temp1 = data.strip().split(',')
        return(AthleteList(temp1.pop(0), temp1.pop(0), temp1))

    except IOError as ioerr:
        print('File error: ' + str(ioerr))
    return (None)

james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')
sarah = get_coach_data('sarah2.txt')

print(james.name + "'s fastest times are: " + str(james.top3()))
print(julie.name + "'s fastest times are: " + str(julie.top3()))
print(mikey.name + "'s fastest times are: " + str(mikey.top3()))
print(sarah.name + "'s fastest times are: " + str(sarah.top3()))


'''
sarah = Athlete('Sarah Sweeney', '2002-6-17', ['2:58', '2.58', '1.56'])
james = Athlete('James Jones')

print(type(sarah))
print(type(james))

print(sarah)
print(james)

print(sarah.name)
print(james.name)

print(sarah.dob)
print(james.dob)

print(sarah.times)
print(james.times)
'''