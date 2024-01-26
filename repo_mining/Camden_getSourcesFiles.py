import csv


java = ".java"
with open('file_rootbeer.csv','r') as csv_file:
    csv_dict_reader = csv.DictReader(csv_file, delimiter=",")
    with open('src_files.csv','w') as new_file:
            fieldnames = ['Filename','Touches']
            csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames) 
            csv_writer.writeheader()
            for line in csv_dict_reader:
                if(line['Filename'].find(java) > -1):
                    csv_writer.writerow(line)