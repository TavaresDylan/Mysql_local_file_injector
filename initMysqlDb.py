import pymysql
import getpass
import os
import inquirer
import typing

class Mysql:
	
	def __init__(self):
		self.cursor = None
		self.connection = None

	"""
	def AskAndSetMysqlCredentials(self):
		user = input("Enter Mysql username : ")
		try:
			password = getpass.getpass()
		except Exception as error:
			print('ERROR', error)
		self.user = user
		self.password = password
		con = self.Connect()
		if con != pymysql.err.OperationalError:
			database = input("Enter database to create or to use : ")
			self.database = database
			err = self.CreateDb()
			if err == None:
				self.AskAboutLocalFile()
				self.InsertLocalFile()
		else:
			self.AskAndSetMysqlCredentials()
	"""

	# Connect to Mysql using user credentials
	def Connect(self, host :str, port :int, user :str, password :str):
		try:
			con = pymysql.connect(host=host, port=port, user=user, password=password, local_infile=True)
			self.connection = con
			c = con.cursor()
			c.execute("SELECT VERSION();")
			version = c.fetchone()
			self.cursor = c
			print("Succefully connected to MySQ %s"  % version)
			self.cursor.close()
			return con
		except Exception as error:
			print('ERROR', error)
			return error
	
	# Create database with name passed by user
	def CreateDb(self, database :str):
		try:
			c = con.cursor()
			self.cursor.execute("CREATE DATABASE IF NOT EXISTS %s;" %database)
			print("Database %s created" % database)
			return None
		except Exception as error:
			print('ERROR', error)
			return error
	
	# Insert Local file using relative path
	def InsertLocalFile(self, filepath, tablename):
		self.cursor.execute("USE %s" %self.database)
		self.cursor.execute("DROP TABLE IF EXISTS %s;" %tablename)
		self.cursor.execute("CREATE TABLE IF NOT EXISTS %s (image_name varchar(255), description varchar(255));" %tablename)
		self.cursor.execute("SET GLOBAL local_infile = true;")
		self.cursor.execute("LOAD DATA LOCAL INFILE %s INTO TABLE %s FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n';" %filepath %tablename)
		self.cursor.execute("SELECT * FROM %s;" %tablename)
		self.connection.commit()
		print(self.cursor.rowcount, "Record inserted successfully into Laptop table")
		res = self.cursor.fetchall()
		self.cursor.close()
		return res
