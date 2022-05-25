from initMysqlDb import Mysql
from askQuestions import Ask
import pymysql

def main():
	print("Welcome, this utility is made to insert local text file data into Mysql database \n")
	ask = Ask()
	mysql_creds = ask.AskMysqlCredentials()
	mysql_config = ask.AskForMysqlConfig()
	dbInstance = Mysql()
	con = dbInstance.Connect(user=mysql_creds["user"], password=mysql_creds["password"], host=mysql_config["host"], port=mysql_config["port"])
	if con != pymysql.err.OperationalError:
		database = input("Enter database to create or to use : ")
		err = self.CreateDb()
		if err == None:
			self.AskAboutLocalFile()
			self.InsertLocalFile()
	else:
		self.AskAndSetMysqlCredentials()

if __name__ == "__main__":
	main()
