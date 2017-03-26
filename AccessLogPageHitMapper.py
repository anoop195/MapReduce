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
This is a mapper function to calculate number of hits for each page
The mapping here is url -> 1
Also once mapper gets executed hadoop will sort and shuffle and send the key -> value pair to corresponding reducer function based on the 
partitioner.
'''


def mapper():
    for line in sys.stdin:
        data = line.strip().split(' ')
        if len(data) == 10:
            ip, identity, username, time, timezone, requestType, Url, http, status, size = data
            print "{0}\t{1}".format(Url, 1)


mapper()
