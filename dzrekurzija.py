def ispisi_string(string):
    if len(string) == 0:
        return
    else:
        print(string[0], end='')
        ispisi_string(string[1:])


