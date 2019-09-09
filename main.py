import csv
import matplotlib.pyplot as plt

avg_aux = {}
home_ownership_dict = {}

with open('home_ownership_data.csv') as home_ownership:
    ownership_table = csv.DictReader(home_ownership,delimiter=',')
    for row in ownership_table:                                        #Build dictionary with member_id as key and homeownership as value
        avg_aux[row['home_ownership']]=[0,0]
        home_ownership_dict[row['member_id']] = row['home_ownership']

with open('loan_data.csv') as loan_data:
    loan_table = csv.DictReader(loan_data,delimiter=',')
    for row in loan_table:                                             #Parse loan_data.csv and compute the total and count of each homeownership status
        val = avg_aux[home_ownership_dict[row['member_id']]]
        val[0]+=int(row['loan_amnt'])
        val[1]+=1

avg = [[x,avg_aux[x][0]/avg_aux[x][1]] for x in avg_aux]               #Calculate average of each status (total/count)

with open('average_loan.csv', 'w') as average_loan:
    writer = csv.writer(average_loan, delimiter=',')
    writer.writerow(['home_ownership','loan_amnt'])                    #Write results to average_loan.csv
    for row in avg:
        writer.writerow(row)

plt.bar([y[0] for y in avg], [y[1] for y in avg])
plt.xlabel('Home ownership')                                           #Plot results
plt.ylabel('Average loan amount ($)')
plt.suptitle('Average loan amount per ownership')
plt.show()