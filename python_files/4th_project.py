#program of basic school administration tool
import csv
def write_into_csv(info_list):
    with open('student_info.csv','a',newline='')as csv_file:
        writter = csv.writter(csv_file)
        writter.writerow(info_list)
condition =True
while(condition):
    student_info = input("Enter the student information like-(name roll_number contact_number E-mail_id): ")
    condition_check=input("if you want to add another student type yes else no : ")
if(condition_check=="yes"):
    condition =True
else:
    condition = False
