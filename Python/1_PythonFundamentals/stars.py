# def stars(l):
#     for i in range(len(l)):
#         out =''
#         for k in range(l[i]):
#             out = '*' + out
#         print out
#
# x = [4, 6, 1, 3, 5, 7, 25]
# stars(x)


def stars(l):
    for i in range(len(l)):
        out =''

        if type(l[i])==int:
            for k in range(l[i]):
                out = '*' + out
            print out
        else:
            word = l[i].lower()
            # m = len(word)
            for k in word:
                out = word[0]+out
            print out


stars([4,"Tom",1,"Michael",5,7,"Jimmy Smith"])
