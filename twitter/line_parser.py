__author__ = 's150834'
#Imports
import json

#Variable
max_line_read = 200
head = []
data = []

#######################################################################for positive feed
#Read n lines from file and store to list
with open("line_sentence_pos.txt") as myfile:
    head = [next(myfile) for x in xrange(max_line_read)]
#Process n-lines road and convert them into json aceptable format
for h in head:
    data.append({"text": ""+h+"", "label": "pos"})
#write results into a json file
json_str = json.dumps(data)
with open("line_sentence_pos.json", "w") as text_file:
    text_file.write(json_str)

#######################################################################for negative feed
head = []
data = []
#Read n lines from file and store to list
with open("line_sentence_neg.txt") as myfile:
    head = [next(myfile) for x in xrange(max_line_read)]
#Process n-lines road and convert them into json aceptable format
for h in head:
    data.append({"text": ""+h+"", "label": "neg"})
#write results into a json file
json_str = json.dumps(data)
with open("line_sentence_neg.json", "w") as text_file:
    text_file.write(json_str)

########################################################################combine into 1 file pos+neg
#Read each file and insert into array
result = []
with open('line_sentence_pos.json') as f:
    for line in f:
        result.append(json.loads(line))
with open('line_sentence_neg.json') as f:
    for line in f:
        result.append(json.loads(line))
#Merge the elements
total = result[0] + result[1]
#Transform into json again
total = json.dumps(total, ensure_ascii=False)
#saveToFile
with open("line_sentence_merge.json", "w") as text_file:
    text_file.write(total)




















