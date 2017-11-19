Author: Xavier Ashe

Using the html2text command, you can strip out HTML out of event data.  This uses the htmllib from
Splunk's packaged python for HTML parsing.  It is a streaming command meaning that you can use it 
in your searches.

Usage:

<search> | html2text (field1 field2 ...)

There are no required arguements.  Then this command is used with no arguements, html2text is run on 
all fields on the event.  

If you only want certian fields converted, then list the fields as arguemens seperated by a space.


Version History
---------------
v1.1 Added the ability to specify fields
v1.0 Initial Release
