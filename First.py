import time

main_task_time = time.time()
for lol in range(10):
    data = open('Расписание.json', encoding = 'utf-8').read().split('\n')
    outfile = open('Расписание_1.xml', 'w', encoding = 'utf-8')

    data = data[1:len(data) - 1]
    for i in range(len(data)):
        data[i] = data[i][4:]

    res_xml = list()
    endings = list()
    flag = 0
    size = len(data)
    numspace = [0] * size

    for i in range(size):
        if data[i].startswith(' '):
            numspace[i] = data[i].count('    ')

    for i in range(size):
        temp = ''
        if '"' in data[i]:
            st_Quot = data[i].find('"') + 1
            fin_Quot = data[i].find('"', st_Quot)
            tag = data[i][st_Quot: fin_Quot]
            if numspace[i] == numspace[i + 1] or data[i + 1].lstrip() == '}' or data[i + 1].lstrip() == '},':
                textStart = data[i].find(tag) + len(tag) + 4
                textEnd = len(data[i]) - 2
                if data[i][-1] == ',':
                    text = data[i][textStart: textEnd]
                else:
                    text = data[i][textStart: textEnd + 1]

                if flag == 1:
                    temp += '\t' * (numspace[i] - 1) + '<' + tag + '> ' + text + ' </' + tag + '>'
                else:
                    temp += '\t' * numspace[i] + '<' + tag + '> ' + text + ' </' + tag + '>'
                res_xml.append(temp)

            elif '[' not in data[i] and numspace[i] != numspace[i + 1]:
                text_s = '\t' * numspace[i] + '<' + tag + '>'
                text_e = '\t' * numspace[i] + '</' + tag + '>'
                res_xml.append(text_s)
                endings.append(text_e)

            elif '[' in data[i]:
                flag = 1
                massiveTag = tag
                ind = i
                temp += '\t' * numspace[ind] + '<' + tag + '>'
                res_xml.append(temp)

        if ']' in data[i]:
            flag = 0
            temp += '\t' * numspace[ind] + '</' + massiveTag + '>'
            res_xml.append(temp)

        if flag == 1:
            if '}' in data[i] and '{' in data[i + 1]:
                temp += '\t' * numspace[ind] + '</' + massiveTag + '>'
                res_xml.append(temp)
                temp = '\t' * numspace[ind] + '<' + massiveTag + '>'
                res_xml.append(temp)

    endings.reverse()
    res_xml += endings

    outfile.write('<?xml version="1.0" encoding="utf-8"?>')
    outfile.write('\n'.join(res_xml))
    outfile.close()

main_task_time = time.time() - main_task_time
