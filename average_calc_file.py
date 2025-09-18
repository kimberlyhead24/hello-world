# Read file contents
print ('Reading in data....')
file = open('mydata.txt')
lines = f.readlines()
file.close()

# Iterate over each line
print('\nCalculating average....')
total = 0
for line in lines:
    total += int(line)

# Compute result
avg = total/len(lines)
print(f'Average value: {avg}')
