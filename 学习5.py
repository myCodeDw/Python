man = []
other = []
try:
    data = open('C:\\Users\\Administrator\\Documents\\GitHub\\Python\\sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)

        except ValueError:
                pass
    data.close()
except IOError:
    print('The datafile is missing!')

try:
    with open('man_data.txt', 'w') as man_file,open('other_data.txt', 'w') as other_file:
        print(man, file=man_file)
        print(other, file=other_file)
except IOError as err:
    print('File error:' + str(err))

"""
try:
    with open('man_data.txt', "w") as man_file,open('other_data.txt', 'w') as other_file:
        print( man , file=man_file)
        print( other , file=other_file)
except IOError as err:
    print('File error :' + str(err))

try:
    data = open('its.txt',"w")
    print("It's...",file=data)
except IOError as err:
    print("File error: " + str(err))
finally:
    if 'data' in locals():
        data.close()

try:
    with open('its.txt', 'w') as data:
        print('hello world!', file=data)
except IOError as err:
    print('File error' + str(err))
"""
