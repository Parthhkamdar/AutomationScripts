from jsonrpclib import Server
import argparse

def configure():
	parser=argparse.ArgumentParser()
	parser.add_argument("hostname file",help="Filename containing the host names")
	parser.add_argument("configuration file",help="Configuration file")
	args=parser.parse_args()
	mylist=[]
	for arg in vars(args):
		mylist.append(getattr(args,arg))
	with open (mylist[0],"r") as fileobject:
			myhosts=fileobject.readlines()

	#Connecting to the switch and configuring it
	#Parameters

	username="admin"
	password=" "
	#cmds=["enable","configure","no router bgp","router bgp 999"]
	cmds=[]

	with open(mylist[1],"r") as file:
			commands=file.readlines()
	for command in commands:
		cmds.append(command.rstrip())
	cmds.pop()
	for ip in myhosts:
		try:
			eapi_url="http://%s:%s@%s/command-api" %(username,password,ip)
			switch=Server(eapi_url)
			response=switch.runCmds(1,cmds,"json")
	
		except:
			print ip
			print "Configuration FAILED for %s" % (ip)
			print "==========================================================================="
			with open('./output_logs.txt', 'a') as f:			
				status = "%s:             FAILED\n" % (ip)
      				f.write(status)
  		else:
    			print "Configuration SUCCESFUL for %s" % (ip)
    			print "============================================================================="
    			with open('./output_logs.txt', 'a') as f:			
      				status = "%s:            SUCCESFUL\n" % (ip)
      				f.write(status)

	
configure()
