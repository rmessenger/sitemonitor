# -------------------------------------------------------------------
# SIMPLE SITE MONITORING SCRIPT
# Robin Messenger
# 
# This script checks a specified website for a key string
# and uses the unix "mail" command to send the relevant string
# to a list of email addresses.
# As an example, this script is configured to scan the city of
# Halifax, NS service update page for the status of the winter
# parking ban.
# -------------------------------------------------------------------


import urllib2
import ssl
import subprocess
import re
import datetime


#List of email addresses to notify or send errors to
NotifyEmails=['email@somesite.com']
ErrorEmails=['email2@somesite.com']

#Regular expression to search for, where parenthesized () group is
#sent to notify email addresses
MatchRE='Status:\s*</td>\s*<td[^>]*>\s*([^<]+)\s*</td>\s*</tr>'

#Website to search
SiteURL='https://www.halifax.ca/transportation/winter-operations/service-updates'

#File to store whether or not we've informed user of change
DataFilename='/path/to/sitemonitor.dat'

#File to store log
LogFilename='/path/to/sitemonitor.log'


#A function to log messages
def myLog(msg):
	try:
		with open(LogFilename,'a') as f:
			f.write("[%s] %s\n" % (datetime.datetime.now(),msg))
	except:
		pass


#A function to use "mail" command to send emails
def sendMail(emailList,msg):
	myLog(msg)
	try:
		p=subprocess.Popen("mail "+" ".join(emailList), 
				   shell=True, stdin=subprocess.PIPE)
		p.communicate(msg)
		return True
	except:
		return False


#A funtion to handle errors
def myError(msg):
	print("Error: "+msg)
	sendMail(ErrorEmails,"Error: "+msg)


try:    #Load HTML from page
	ctx=ssl.create_default_context()
	ctx.check_hostname=False
	ctx.verify_mode=ssl.CERT_NONE
	response=urllib2.urlopen(SiteURL, context=ctx)
	html=response.read()

	try:    #Read data file
		lastStatus=""
		with open(DataFilename,'r') as f:
			lastStatus=f.read()

		#See if we can find the status string
		m = re.search(MatchRE, html)

		try:    #Extract status line from page
			currentStatus=m.group(1)

			#If last status does not match current, text user
			if currentStatus != lastStatus:
				#Text me the new status, and if nothing goes wrong...
				if sendMail(NotifyEmails,currentStatus):
					try:    #Write most recent update to data file
						with open(DataFilename,'w') as f:
							f.write(currentStatus)
					except:
						myError("Problem writing to data file!")
				else:
					myError("Problem sending text message!")
		except:
			myError("Cannot find status on page!")

	except:
		myError("Problem reading data file!")
except:
	myError("Problem loading service update page!")
