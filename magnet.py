source = open("C:/2.txt", "r")  #打开C盘下的2.txt
f = open("C:/link.txt", "w")    #输出到C盘下的link.txt
line = source.readline()
line = line[:-1]
while line:
    line = source.readline()
    line = line[:-1]
    temp = line.split('magnet:')
    link = temp[1]
    print(link)
    f.write('magnet:' + link + '\n')
