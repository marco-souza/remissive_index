filename = './data.txt'

def get_index(filename):
    index = []
    lineCount = 0

    # 1. Create list with all words
    for line in open(filename, 'r'):
        lineCount += 1
        listWords = line.split(' ')
        for word in listWords:
            index.append([word.rstrip(), lineCount])

    # 2. Create remissive list
    finalList = []
    for j, _ in enumerate(index):
        included = False
        for i, _ in enumerate(finalList):
            fl_item = finalList[i].keys()[0];
            if (fl_item == index[j][0]):
                # 2.2 Increment list of occurencies
                finalList[i][fl_item].append(index[j][1])
                included = True
                break
        # 2.1 Add word if it isn't on the list already
        if included == False:
            add = { index[j][0]: [ index[j][1] ]}
            finalList.append(add)

    # 3. Sort list
    sorted_final_list = sorted(finalList, key=lambda x: x.keys()[0].lower())

    # 4. Format and Print
    for i in sorted_final_list:
        key = i.keys()[0]
        print(key + ''.join(' {}'.format(i) for v, i in enumerate(i[key])))


if (__name__ == '__main__'):
    get_index(filename)