#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import json
import sys

print()

print(json.dumps(dict(os.environ),indent = 2))#q1

print(f"<p> QUERY_STRING={os.environ['QUERY_STRING']}</p>")#q2
print(f"<p> Browser=${os.environ['HTTP_USER_AGENT']}</p>")#q3

#report the posted data
print("<ul>")
posted_bytes = os.environ.get("CONTENT_LENGTH", 0)
if posted_bytes:
    posted = sys.stdin.read(int(posted_bytes))
    #print(posted.split('&'))
    print(f"<p> POSTED: <pre>")
    for line in posted.splitlines():
        print(line)
    print("</pre></p>")
print("""
</ul>
""")


"""
print("<ul>")
for parameter in os.environ['QUERY_STRING'].split('&'):
    (name, value) =parameter.split('=')
    print(f"<li><em>{name} </em> =  {value}</li>")
print("""

""")
"""