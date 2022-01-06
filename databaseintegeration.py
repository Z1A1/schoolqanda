import mysql.connector
def DataUpdate(acedamicyear,address,child_grade,child_name,dob,email,first_name_last_name, gaurdian,phone,school,schooldetails):

  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="schoolqa"
   )
  mycursor = mydb.cursor()
  sql='INSERT INTO schoolqa (acedamicyear,address,child_grade,child_name,dob,email,first_name_last_name, gaurdian,phone,school,schooldetails) VALUES ("{0}","{1}", "{2}","{3}","{4}","{5}","{6}","{7}","{8}","{9}","{10}");'.format(acedamicyear,address,child_grade,child_name,dob,email,first_name_last_name, gaurdian,phone,school,schooldetails)
  mycursor.execute(sql)
  mydb.commit()

