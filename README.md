# sitemonitor

This is a simple script to monitor a website for specific changes and
send an email to a list of addresses containing the specific changes
specified by a regular expression.

## Installing

1. __Prerequisites__: This script requires a linux server with a functioning and configured mail
server, cron daemon, and python2 or python3.

2. __Clone Repository__: ```git clone https://github.com/rmessenger/sitemonitor.git```

3. __Configuration__: Open sitemonitor.py in a text editor, and edit the following lines:

```python
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
```

4. __Cron Job__: Add a cron job by calling:

```crontab -e```

and add an entry to automatically run this script on a recurring basis.
For example, to run every half hour, enter this line:

```*/30 * * * * /path/to/python /path/to/sitemonitor.py```

Save the file, and you're done!
