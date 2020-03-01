"""
fitting to degree-6 polynomial in form ax6 + bx5 + cx4 + dx3 + ex2 + fx + g
"""
import matplotlib.pyplot as plt
outfile = open('output.csv', 'w')

def predict(x):
    coefs1 = [0.650599,-27.0259, 438.125,-3459.46, 13380.9, -22178.9, 32796.7]
    coefs2 = [-0.0491456, 2.77664, -53.6, 457.11, -1832.18, 3562.24, 3648.17]
    sums = [0, 0]

    i = 0
    while i < 7:
        sums[0] += coefs1[i] * (x ** (6 - i))
        sums[1] += coefs2[i] * (x ** (6 - i))
        i += 1

    return sums

# month days in order: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31

months = [31, 31, 30, 31, 30, 31, 31, 28, 31, 30, 31, 30]
outfile.write('month,day,wtp1,wtp2\n')
for n in range(12):
    for i in range(months[n]):
        output = ''
        output += str(n+1) + ','
        output += str(i + 1) + ','
        output += str(predict(n + 1 + ((i+1)/months[n]))[0]) + ',' + str(predict(n + 1 + ((i+1)/months[n]))[1])
        output += '\n'
        outfile.write(output)


outfile.close()
