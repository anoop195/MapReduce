#!/usr/bin/python
import sys

'''
The data is stored in the format %h %l %u %t \"%r\" %>s %b
Where:

%h is the IP address of the client
%l is identity of the client, or "-" if it's unavailable
%u is username of the client, or "-" if it's unavailable
%t is the time that the server finished processing the request. The format is [day/month/year:hour:minute:second zone]
%r is the request line from the client is given (in double quotes). It contains the method, path, query-string, and protocol or the request.
%>s is the status code that the server sends back to the client. You will see see mostly status codes 200 (OK - The request has succeeded), 304 (Not Modified) and 404 (Not Found). See more information on status codes in W3C.org
%b is the size of the object returned to the client, in bytes. It will be "-" in case of status code 304.
This is a reducer function to calculate number of hits for each Ip
The mapping here is url -> 1
'''


def reducer():
    hitAmount = 0
    oldKey = 0
    for line in sys.stdin:
        data = line.strip().split('\t')

        if len(data) != 2:
            continue
        thisKey, thisCount = data
        if oldKey and oldKey != thisKey:
            print "{0}\t{1}".format(oldKey, hitAmount)
            hitAmount=0
        oldKey = thisKey
        hitAmount +=1


reducer()

