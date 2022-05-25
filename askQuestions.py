import getpass
import inquirer

class Ask:

	def AskMysqlCredentials(self) -> dict:
		user_question = [inquirer.Text(
				"user",
				message="What is your mysql user ? ")]
		user_response = inquirer.prompt(user_question)
		try:
			password = getpass.getpass()
		except Exception as error:
			print('ERROR', error)
			return error
		return {"user": user_response, "password": password}

	def AskForMysqlConfig(self) -> dict:
		host_question = [inquirer.List(
			"host",
			message="What is your host ? ",
			choices=["localhost (default)","manual"],
			),]
		host_response = inquirer.prompt(host_question)

		if host_response["host"] == "manual":
			host_question = inquirer.Text('host', message="Enter Mysql host"),
			host_response = str(inquirer.prompt(host_question))
		else:
			host_response = "localhost"

		port_question = inquirer.List(
			"port",
			message="What is your port ? ",
			choices=["3306 (default)","manual"],
		),
		port_response = inquirer.prompt(port_question)
		if port_response["port"] == "manual":
			port_question= inquirer.Text('port', message="Enter mysql port",validate=lambda _, x: re.match('\d', x))
			port_response = int(inquirer.prompt(port_question))
		else:
			port_response = 3306
		return {"host": host_response, "port": port_response}

	def AskAboutLocalFile(self) -> []:
		questions = [
			inquirer.List(
				"Columns separed by",
				message="What is separing your columns ?",
				choices=[",",".", "/", ";", "\\t (tab)", "\\n (whitespace)"],
			),
			inquirer.Path('log_file',
				message="Where your file is located?",
				path_type=inquirer.Path.DIRECTORY,
			),
		]

		answers = inquirer.prompt(questions)