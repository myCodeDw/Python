def sanitize(time_string):
    if '-' in time_string:
        splitter= '-'
    elif ':' in time_string:
        splitter= ':'
    else:
        return(time_string)
    (mins,secs)= time_string.split(splitter)
    return(mins+'.'+secs)

print(sanitize('19:20'))


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        temp1 = data.strip().split(',')
        return ({'Name' : temp1.pop(0),
                 'DOB'  : temp1.pop(0),
                 'Times': str(sorted(set([sanitize(t) for t in temp1]))[0:3])
                 }
                )
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return (None)

james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')
sarah = get_coach_data('sarah2.txt')

'''
(sarah_name,sarah_dob) = sarah.pop(0), sarah.pop(0)
print(sarah_name + "'s fastest times are: " +
      str(sorted(set([sanitize(t) for t in sarah]))[0:3]))

sarah_data = {}
sarah_data[ 'Name' ] =  sarah.pop(0)
sarah_data[ 'DOB' ] = sarah.pop(0)
sarah_data[ 'Times' ] = sarah
print(sarah_data[ 'Name' ]+ "'s fastest times are: "+
str(sorted(set([sanitize(t) for t in sarah_data[ 'Times']]))[0:3]))
'''

print(james[ 'Name'] + "'s fastest times are: " + james[ 'Times' ])
print(julie[ 'Name'] + "'s fastest times are: " + julie[ 'Times' ])
print(mikey[ 'Name'] + "'s fastest times are: " + mikey[ 'Times' ])
print(sarah[ 'Name'] + "'s fastest times are: " + sarah[ 'Times' ])
