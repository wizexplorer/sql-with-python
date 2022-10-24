import mysql.connector
con= mysql.connector.connect(user="root",password="tiger",database="school")
cur=con.cursor()
print("-------------------------MYSQL CONNECTIVITY 2-------------------------")
print("|                         DELETION OF RECORD                         |")
print("-"*70)
def search(x):
    query= "select * from student where adminNo = {}".format(x)
    cur.execute(query)
    cur.fetchall()
    return (cur.rowcount)

admno= input("  Enter the admission number to delete : ")
count=search(admno)
if count>0:
    query1="DELETE FROM student WHERE adminNo = {}".format(admno)
    cur.execute(query1)
    cur.execute("commit")
    print("\t\t RECORD DELETED SUCCESSFULLY")
else:
    print("\t\t INVALID ADMISSION NUMBER")
con.close()
