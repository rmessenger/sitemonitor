# sitemonitor

This is a simple script to monitor a website for specific changes and
send an email to a list of addresses containing the specific changes
specified by a regular expression.

## Installing
This script requires a linux server with a functioning and configured mail
server, cron daemon, and python2 or python3. To install, first clone this 
repository:

```git clone https://github.com/rmessenger/sitemonitor.git```

Next, open sitemonitor.py in a text editor, and enter the URL of the site
you wish to monitor, the regular expression which selects the subset
of the HTML of interest, enter a list of email addresses to which
notifications and errors can be sent, and enter the absolute path to
the data and log files. Then you must add a cron job by
calling:

```crontab -e```

and add an entry to automatically run this script on a recurring basis.
For example, to run every half hour, enter this line:

```*/30 * * * * /path/to/python /path/to/sitemonitor.py```

Save the file, and you're done!
