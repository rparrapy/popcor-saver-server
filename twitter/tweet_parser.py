__author__ = 's150834'
import csv, sys, json
input_file = 'training_set.csv'
fixed_file = 'training_set_fix.csv'
output_file = "training_set.json"
input_file_has_double_quote = True #Does it have " symbol inside
run_on_test_set = False #Activate to run on testing set

if run_on_test_set == True:
  input_file = 'testing_set.csv'
  fixed_file = 'testing_set_fix.csv'
  output_file = "testing_set.json"


class dataSetHandler():
  def delete_weird_symbols(self,input_file, output_file):
    with open(input_file, 'r') as infile,\
            open(output_file, 'w') as outfile:
      data = infile.read()
      data = data.replace("\"", "")
      outfile.write(data)
    return
  def read_csv_file(self, file_name):
    data = []
    f = open(file_name)
    csv_f = csv.reader(f)
    for row in csv_f:
      try:
        if row[1] == '0':
          data.append({"text": ""+row[3].lstrip().rstrip()+"", "label": "neg"})
          #print {"text": ""+row[3]+"", "label": "neg"}
        else:
          data.append({"text": ""+row[3].lstrip().rstrip()+"", "label": "pos"})
      except:#then element is only in frist row[0] we have to split
        pass
    return data


#main run
if __name__ == "__main__":
  h = dataSetHandler()

  #To delete the symbol " for easy json create
  if input_file_has_double_quote == True:
    h.delete_weird_symbols(input_file,fixed_file)
    print "Symbol \" has been deleted from file"

  my_data_processed = h.read_csv_file(fixed_file)
  print len(my_data_processed),"Feed elements processed"
  json_str = json.dumps(my_data_processed)
  #print json_str

  with open(output_file, "w") as text_file:
    text_file.write(json_str)

