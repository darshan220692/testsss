import mysql.connector as ct

bdb = ct.connect(host="localhost", user = "root", passwd = "Shankar22@")

csr = bdb.cursor()
# csr.execute("delete database globalone")

# csr.execute(" create table globalone.pks(employee_id int(10), employee_name varchar(80),employee_emailid varchar(20), emp_sal int(10), emp_attendance int(5))")
# s =("create table globalone.pks(employee_id int(10), employee_name varchar(80),employee_emailid varchar(20), emp_sal int(10), emp_attendance int(5))")
csr.execute(""insert into globalone.pks values (101 , "Darshan Kalamkhede", "kalamkhede@gmail.com", 50, 30)"")
bdb.commit()
# csr.execute("show databases")
print(csr.fetchall())

