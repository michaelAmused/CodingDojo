import random
head = 0
tail = 0
throw = ''
for i in range(1,5001):
    coin = round(random.random())
    if coin < 0.5:
        head += 1
        throw = 'head'
        print "Attempt #" + str(i) + ": Throwing a coin... It's a " + throw + "! ... Got " + str(head) + " head(s) so far and " + str(tail) + " tail(s) so far"
    else:
        tail += 1
        throw = 'tail'
        print "Attempt #" + str(i) + ": Throwing a coin... It's a " + throw + "! ... Got " + str(head) + " head(s) so far and " + str(tail) + " tail(s) so far"
print "Ending the program, thank you!"
