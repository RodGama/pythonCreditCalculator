

a = str(input()).split(" ")
if len(a) == 1:
    print(str(a[0]))
else:
    x = 0
    word_list = ""
    for word in a:
        if x == 0:
            word_list += word
        else:
            word_list += word.capitalize()
        x += 1
    print(word_list)
