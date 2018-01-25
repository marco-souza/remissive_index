filename = './data.txt'

def get_index(filename):
    index = []
    lineCount = 0
    for line in open(filename, 'r'):
        lineCount += 1
        listWords = line.split(' ')
        for word in listWords:
            index.append([word.rstrip(), lineCount])

    finalList = []
    for j,_ in enumerate(index):
        # for j in index:
        # print(item[0])
        included = False
        for i,_ in enumerate(finalList):
            fl_item = finalList[i].keys()[0];
            if (fl_item == index[j][0]):
                # print(fl_item)
                finalList[i][fl_item].append(index[j][1])
                included = True
                break
        if included == False:
            add = { index[j][0]: [ index[j][1] ]}
            finalList.append(add)

    sorted_final_list = sorted(finalList, key=lambda x: x.keys()[0].lower())

    for i in sorted_final_list:
        key = i.keys()[0]
        print(key + ''.join(' {}'.format(i) for v, i in enumerate(i[key])))
        # print(i[key])
        # print(' '.join(i[key]))


if (__name__ == '__main__'):
    get_index(filename)