import time
import json
from json2xml import json2xml

additional_one_time = time.time()

for lol in range(10):
    obj = json.loads(open('Расписание.json', encoding='UTF-8').read())

    f = open('Расписание_2.xml', 'w', encoding='UTF-8')
    f.write(json2xml.Json2xml(obj).to_xml())
    f.close()

additional_one_time = time.time() - additional_one_time
