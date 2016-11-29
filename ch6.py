'''
cleese = {}
palin = dict()
print(type(cleese))
print(type(palin))

cleese['Name'] = 'Johe cleese'
cleese['Occupations'] = ['actor', 'comedian', 'writer', 'film product']
palin = {'Name': 'Michael Palin', 'Occupations': ['comedian', 'actor', 'writer', 'tv']}

print(palin['Name'])
print(cleese['Occupations'][-3])

palin['Birthplace'] = "Broomhill, Sheffield, England"
cleese['Birthplace'] = "Weston-super-Mare, North Somerset, England"

print(palin)
print(cleese)
'''
'''继承类实例
def sanitize(time_string):
    if '-' in time_string:
        splitter= '-'
    elif ':' in time_string:
        splitter= ':'
    else:
        return(time_string)
    (mins,secs)= time_string.split(splitter)
    return(mins+'.'+secs)

class Athlete :
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times= a_times

    def top3(self):
        return(sorted(set([sanitize(t) for t in self.times]))[0:3])

    def add_time(self, time_value):
        self.times.append(time_value)

    def add_times(self,list_of_times):
        self.times.extend(list_of_times)

vera = Athlete('vera Vi')
vera.add_time('1.31')
print(vera.top3())

vera.add_times(['2.22', '1-21', '2:22'])
print(vera.top3())
'''

class NamedList(list):
    def __init__(self, a_name):
        list.__init__([])
        self.name=a_name
johnny = NamedList("John Paul Jones")

# print(type(johnny))
# print(dir(johnny))

johnny.append("Bass Player")
johnny.extend(['Composer', 'Arranger', 'Musician'])

#print(johnny)
#print(johnny.name)

for attr in johnny:
    print(johnny.name + ' is a ' + attr + '.')
