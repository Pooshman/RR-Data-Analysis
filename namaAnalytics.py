import os
import csv
from turtle import clear

class NamaBhikshaAnalytics:

    @staticmethod     
    def nbAnalytics(file_name):
        with open(os.path.expanduser(f'{file_name}')) as myfile:
            title = myfile.readline()
            data_list = []
            value_dict = {}
            for line in myfile:
                line = line.strip()
                conv_list = []
                temp_list = line.split(',')
                for i in range(len(temp_list)):
                    if i == 0:
                        continue
                    else:
                        if temp_list[i] == '':
                            conv_list.append(0)
                        else:
                            conv_list.append(int(temp_list[i]))
                value_dict[temp_list[0]] = conv_list

        title_list = title.split("\",\"")
        title_list[0] = "UserID / (Year,Month,Day,Hour,Min,Sec)"
        title_list[-1] = "2022,2,28,1,5,2"

        #element List
        monthdict = {}
        monthdict[0] = 6
        monthdict[1] = 37
        monthdict[2] = 67
        monthdict[3] = 98
        monthdict[4] = 128
        monthdict[5] = 159
        monthdict[6] = 190
        monthdict[7] = 220
        monthdict[8] = 251
        monthdict[9] = 281
        monthdict[10] = 312
        monthdict[11] = 343
        monthdict[12] = 371

        totalnamalist = []
        #Total Nama Chanted
        print('\nTotal nama chanted per month, March 2021 --> Feb 2022:')
        for i in range(12):
            march_num = 0
            for key in value_dict:
                march_num += value_dict[key][monthdict[i+1]]
            feb_num = 0
            for key in value_dict:
                feb_num += value_dict[key][monthdict[i]]
            march_num = march_num-feb_num
            totalnamalist.append(march_num)
            print(march_num, end =' || ')


        Chanter_dict = {}
        totalchanterlist = []
        print('\n\nTotal Chanters per month, March 2021 --> Feb 2022:')
        for i in range(12):
            numChanters = 0
            for key in value_dict:
                Chanter_dict[key] = value_dict[key][monthdict[i+1]] - value_dict[key][monthdict[i]]
                if Chanter_dict[key] > 0:
                    numChanters += 1
            totalchanterlist.append(numChanters)
            print(numChanters, end =' || ')

        #Find New Users per Month
        newuserlist = []
        print("\n\nNew users per month, March 2021 --> Feb 2022:")
        for i in range(12):
            newusers = 0
            for key in value_dict:
                newdata = value_dict[key][monthdict[i+1]]
                prevdata = value_dict[key][monthdict[i]]
                if prevdata == 0:
                    tempnum = newdata - prevdata
                    if tempnum != 0:
                        newusers += 1
            newuserlist.append(newusers)
            print(newusers, end =' || ')
        print('\n')

        #Making CSV File for Final Results
        finalData = []
        monthlist = ['March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December','January', 'February' ]

        field_names = [f'Months ({file_name})', 'Total Nama', 'Total Chanters', 'New Users']
        for i in range(12):
            tempdict = {}
            tempdict[f"Months ({file_name})"] = monthlist[i]
            tempdict["Total Nama"] = totalnamalist[i]
            tempdict["Total Chanters"] = totalchanterlist[i]
            tempdict["New Users"] = newuserlist[i]
            finalData.append(tempdict)



        with open(f'./FinalData.csv', 'a') as newfile:
            writer = csv.DictWriter(newfile, fieldnames = field_names)
            writer.writeheader()
            writer.writerows(finalData)

NamaBhikshaAnalytics.nbAnalytics('/Users/poosh/PYFiles/androidNew.csv')