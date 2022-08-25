import csv
import os

directory = 'data'
stream= os.popen('git rev-parse --show-toplevel')
dir = stream.read().strip()

# print(dir)



combinedSales =  open(dir+'/combinedSalesData.csv', mode='w')

salesWriter = csv.writer(combinedSales, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
for filename in os.listdir(directory):

    filePath = dir+'/'+directory+'/'+filename

    with open(filePath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if(row[0] == 'pink morsel'):

                # print(float(row[1][1:]), float(row[2]), float(row[1][1:])*float(row[2]))




                salesWriter.writerow([float(row[1][1:])*float(row[2]), row[3], row[4]])

            # if line_count == 0:
            #     print(f'Column names are {", ".join(row)}')
        
        
            


            line_count += 1
