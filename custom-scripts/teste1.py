import SimpleHTTPServer
import SocketServer
import os.path, sys
import psutil, os, time
import datetime
from datetime import timedelta
import platform, subprocess, re

#Handle de http requests.
class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	#Build the html file for every connection.
	def makeindex(self):
		# DATA E HORA
		tempo = str(datetime.datetime.now())
		print(tempo)

		# UPTIME
		with open('/proc/uptime', 'r') as f:
			uptime_seconds = float(f.readline().split()[0])
			uptime_string = str(timedelta(seconds=uptime_seconds))

		# print('uptime:', uptime_string)

		# TIPO DE PROCESSADOR E VELOCIDADE

		def get_processor_name():
			command = "cat /proc/cpuinfo"
			all_info = subprocess.check_output(command, shell=True).strip()
			for line in all_info.split("\n"):

				if "model name" in line:
					return re.sub(".*model name.*:", "", line, 1)
			return ""

		ProcessorData = str(get_processor_name())

		# VERSAO DO SISTEMA
		plataforma = platform.platform()
		# print('Sistema:', plataforma)

		#RAM total e utilizada

		total = str(psutil.virtual_memory().total)
		used = str(psutil.virtual_memory().used)

		#cpu usage
		cpuPercent = psutil.cpu_percent(interval=1)

		#list
		#process_names = [proc.name() + proc.name() for proc in psutil.process_iter()]
		#pid = str(process_names)

		#proc_names = [for proc in psutil.process_iter():
		#				proc_names.append(proc.name() +  proc.pid())]
		#pid = str(proc_names)

		#process = str(psutil.Process().pid)

		#pids = psutil.pids()
		#for pid in pids:
		#	process = psutil.Process(pid)
			#print "%d   s" % (pid, process.name(),)
			#print "%d   s" % (pid, process,)

		#process = psutil.Process(pid)

		#process_name = process.name()
		tofile = str()
		for i in psutil.pids():
			tofile = tofile + "<br>" + str(psutil.Process(i).pid) + "-" + str(psutil.Process(i).name()) + "<br>"


		html_str = """
		<!doctype html>
		<html>
		    <head>
		        <title>Trabalho 1</title>
		    </head>

		    <body>
		        <h1>informacoes basicas sobre o funcionamento do sistema</h1>

		        <p>  Data e hora do sistema: """ + tempo + """    </p>
		        <p>  Uptime em segundos: """ + uptime_string + """   </p>
		        <p>  Processador: """ + ProcessorData + """   </p>
		        <p>  Versao do sistema: """ + plataforma + """   </p>
		        <p>  Capacidade percentual ocupada do processador: """+ str(cpuPercent) +"""   </p>
		        <p>  RAM total (MB): """+ total +"""   </p>
		        <p>  RAM utilizada (MB): """+ used +""" </p>
		        <p>  Lista de processos: """ + tofile + """  </p>
		    </body>   
		</html>
		"""

		f = open("index2.html", "w")
		f.write(html_str)
		f.close()
		return
	
	#Method http GET.	
	def do_GET(self):
		self.makeindex()
		self.path = './index2.html'
		return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

#Start the webserver.
Handler = MyRequestHandler
server = SocketServer.TCPServer(('0.0.0.0', 8082), Handler)
server.serve_forever()
