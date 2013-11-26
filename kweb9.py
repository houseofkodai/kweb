#!/usr/bin/python2 -B
'''
kweb:
=====
  * Fast, simple, *single-file* python2 web-framework/HTTP-server.
  * outcome of several years of thoughts/experiments/experience.


why:
====
  * make simple things easy, and complicated things possible.
    1. [download kweb9.py](https://raw.github.com/houseofkodai/kweb/master/kweb9.py)
    2. run:
 ```
python kweb9.py
```
    3. open URL http://localhost:8010/ from local-browser or http://<ip-address>:8010/ from remote-browser


features:
=========

fast:
-----
  * over 2000/dynamic-requests-per-second on a core-i3 laptop !-)

simple:
-------
  * zero configuration - file-system and python modules do the needful
  * developing dynamic web pages is very easy, look at samples/hello.kweb
  * file-system-path-module discovery
  * modules are python files in URL-path with .kweb extension
    when ordinary-files are found, they are sent as-is to the client/browser
    when .kweb file is found, it is executed and those results sent-back to the client/browser
  * the HTTP method is mapped to the module method and called with a request parameter
    method-name is HTTP request-line method (GET/POST/HEAD/PUT/DELETE...)
    method returns None - causes path-modules to be executed
    method returns anything-else returns data back to client/browser
  * path-index-module:
    when request URL is a directory, index.kweb module is used, if it exists.
    index.kweb can act as a filter to request processing
  * single-site-module: serve an entire web-site from a single-python module
  * catchall-module: serve all sites from a single python module

secure:
-------
  * in *nix: run as the owner of app/hostdir/module
    per-host/module permissions (run-as - set uid/gid)

cross-platform:
---------------
  * should work wheverever python works

misc:
-----
  * save bandwidth with resume-file-download via. range-support
  * virtual-host support
  * not all features are documented:
    python programmers can "easily" figure them out, when the need arises


FAQ:
====
1. hello.kweb

```python
def GET(REQUEST):
  return 'hello kweb :-)'
```

2. what do I need to know to develop web-applications using kweb ?

  a knowledge of HTML/CGI (optionally CSS/Javascript) and python.

3. how do I test kweb server to verify your performance claim ?

  ./kweb9.py -t/hello

4. how do I develop other kweb modules ?

  read/understand the samples - then cut&paste as needed.

5. how can I help ?

  deploy...document...discuss...


LICENSE:
========

MIT License

Copyright (c) 2013 Karthik Ayyar - http://houseofkodai.in/

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


samples/
========
1. [hello.kweb](https://github.com/houseofkodai/kweb/blob/master/samples/hello.kweb)

  1 liner - simplest kweb module

2. [lorem](https://github.com/houseofkodai/kweb/blob/master/samples/lorem.kweb)

  html5 template with common tags

3. [txthello](https://github.com/houseofkodai/kweb/blob/master/samples/txthello.kweb)

  2 liner - simplest text/plain response

4. [auth](https://github.com/houseofkodai/kweb/blob/master/samples/auth.kweb)

  HTTP Basic Authentication example

5. [redirect](https://github.com/houseofkodai/kweb/blob/master/samples/redirect.kweb)

  redirect html template - use in POST requests

6. [cookie](https://github.com/houseofkodai/kweb/blob/master/samples/cookie.kweb)

  set/get cookies

7. [listdir](https://github.com/houseofkodai/kweb/blob/master/samples/listdir.kweb)

  list directories from a different path of filesystem

8. [form](https://github.com/houseofkodai/kweb/blob/master/samples/form.kweb)

  form field processing, including file-upload


  session
  rest
  api

notes-to-self:
  * BUG in osx-python asyncore
    + Modify /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/asyncore.py and set the default of use_poll from False to True:
      Line 207:
      def loop(timeout=30.0, use_poll=False, map=None, count=None):
      to
      def loop(timeout=30.0, use_poll=True, map=None, count=None):
  * python-performance-order
    read: local, nonlocal, global, builtin, classvar, instancevar,
          unboundmethod, boundmethod
    write: local, nonlocal, global, classvar, instancevar
  * general web-application guidelines:
    + do not store sensitive data in tokens (cookies/url)
    + constant-time string comparisons when testing incoming data for authentication purposes
    + do not provide distinguishable errors to authentication request
    + log weird queries
    + don't use third-party javascript
    * prevent csrf
      ~ check referrer
      ~ one-time-session-keys - transaction-key-expiry

pndng:
  * sample-app: file-upload - curl
  * blockip-on-multiple-errors
  * bandwidth throttling
  * ontimer/onclose events for handler - persistent connection

history:
  26 NOV 2013: removed 100% width in site.css table
               added sorting for directory listing
  25 NOV 2013: modified site.css
  22 NOV 2013: modified dirlist to display time, if today
               renamed dirlist to listdir
               made _dirlist public as htmldir
               changed order of directory listing to date, size name
  20 NOV 2013: modified server.debugfname to use request_count instead of conn_count
  09 NOV 2013: modified site.css to increase line-height and thinner top-border
  22 OCT 2013: removed _kweb.html_form._load_fieldvalues
               modified _kweb.load_form to include default field values
               renamed _kweb..html_form._load_fieldsets into _kweb.load_form - to enable use in form validation
  17 OCT 2013: modified _kweb.html_form._fieldset
                 include type 0 html
                 append error if fielderror
               added _load_field functions to html_form
               undo rename _KRequest._server property to server
               added _kweb.smtpmail
  16 Oct 2013: renamed _KRequest.data to _KRequest.content
               renamed _KRequest.server property to _server
               renamed _KRequest.parse_header to _parse_header
               modified _KRequest._parseBody to reset content - seek(0)
  31 Jul 2013: removed getquery - merged R.form with R.args
               changed return format of REQUEST.args/form parse_query/parse_formdata [(name,value,), (name,value,),...]
               bugfix in _kweb.html_ methods
  30 Jul 2013: added html_ methods to _kweb
  17 Jul 2013: rewrite of _KRequest/_KHTTPClient class to make code more readable
  15 Jul 2013: sendRedirect bug fix
  11 Jul 2013: removed css from html to /kweb.css and
  09 Jul 2013: modified sendResponse to send content only if method is not HEAD
               added self.HEAD to handle HEAD requests
               if module does not have HEAD method - then GET is used
  08 Jun 2013: updated dirlist() to include / in directory links
  28 May 2013: updated html()
  20 May 2013: upload to github.com/houseofkodai/kweb
'''

try:
  import sys
  import asyncore
  import base64
  import binascii
  import __builtin__
  import datetime
  import fcntl
  import imp
  import mimetypes
  import optparse
  import os
  import Queue
  import random
  import shlex
  import signal
  import socket
  import string
  import struct
  import subprocess
  import threading
  import time
  import zlib
  import cStringIO
  import tempfile
  import urlparse
  import urllib
  import traceback
  import collections
  import smtplib
except:
  print 'upgrade python to 2.4 or above'
  sys.exit(1)

# ##################################################################################################
# GLOBAL CONSTANTS
# ##################################################################################################
_KWEB_VERSION = 9
_KWEB_SERVER_VERSION = 'Server: kweb/%d/2013.NOV.26 github.com/houseofkodai/kweb Python/%s' % (_KWEB_VERSION, sys.version.split()[0])

#common mime-types - add/edit as required
_KEXTENSIONS_MAP = mimetypes.types_map.copy()
_KEXTENSIONS_MAP.update({
  '.py': 'text/plain',
  '.c': 'text/plain',
  '.h': 'text/plain',
  '.log': 'text/plain',
  '.ini': 'text/plain',
  '.kweb': 'text/plain',
  })

# common codes - NOT comprehensive; edit/add as required
_KHTTP_RESPONSES = {
  100: 'Continue',
  200: 'OK',
  206: 'Partial content',
  301: 'Moved Permanently',
  302: 'Moved Temporarily',
  303: 'See Other',
  304: 'Not Modified',
  400: 'Bad request',
  401: 'Unauthorized',
  403: 'Forbidden',
  404: 'Not Found',
  408: 'Request Time-out',
  411: 'Length Required',
  413: 'Request Entity Too Large',
  414: 'Request-URI Too Long',
  415: 'Unsupported Media Type',
  416: 'Requested Range Not Satisfiable',
  500: 'Internal error',
  501: 'Not Implemented',
  503: 'Service temporarily overloaded',
  505: 'HTTP Version not supported',
}

_KRESOURCES = {
'/blank.gif': ('image/gif', zlib.decompress(
 'x\x9cs\xf7t\xb3\xb0L\xe4`\xe0`h``\xf8\x0f\x02g\x14\x7f'
 '\xb20\xb2300\xe8\x001\x03H\x86\x81\x89\xbd\xa5\x7f\xe5\xe9\xb7\xb1'
 '\x0c\x0c\xd6\x00[/\rw')),
'/bitby.gif': ('image/gif', zlib.decompress(
 'x\x9c\x01\xff\x08\x00\xf7GIF89as\x00$\x00\xf7\xff\x00>'
 '4\x15\x9e\x99\x8angP\xcf\xcc\xc4e]DJA$\xf3\xf2\xf0V'
 'M2\xe7\xe6\xe2\xf5\xf3\xf0\xb6\xb3\xa7\xdb\xd9\xd3\x87\x80m\xc2\xb7\xa8\xc2'
 '\xbf\xb6bZA\xb0\x87\x1cJ<\x18\xe1\xdb\xd3|cC\x93\x8d|W'
 '=\x17\xd7\xcf\xc5\xeb\xe7\xe2{t^\x8b\x85s\xb2\xae\xa1UE\x1aD'
 '8\x17fJ&@5\x15\x9b\x87n\xaa\xa6\x98I8\x16\xd8\xd6\xd0\xae'
 '\x9f\x8bS<\x16\xc8\xa6I\\E\x19\\J\x1cbN\x1c\xc5\xa2D\xc3'
 '\xa0?\xb8\xab\x99\xc0\x9c:D7\x16\xbd\x983cJ&pY\x1f\xbb'
 '\x960mZ)\x91{`\xa6\x8bVtU\x1bQ;\x16\x8en\x1f\\'
 '?\x17K9\x16\xa2~-\xa6\x89<pX\x1d~f)\x91v2b'
 'F\x19xc-\xa5\x93}\xb4\x8c!pV3\xbc\xb8\xad\xa1\x821i'
 'S\x1d\xbe\x996\xb2\x8a\x1e\xa2}#\xc0\x9d;wa*\xb9\x92*\x86'
 'oQ\xc6\xa3E\xca\xa8LRC\x1ciK\x1aO;\x16\xc1\x9e<O'
 'A\x19nW#F7\x16B5\x16\xcc\xc3\xb6\x96x,PA\x1a\xc0'
 "\x9c9rT'\xc5\xc2\xb8\x86h\x1f\x91q#\xb9\x958\x95w*\xc7"
 '\xbb\xa9\xb4\x8d"xq[v`)\xc3\xa1@XI!jT\x1fs'
 ']$\xb9\x93,U<\x16nZ&]A\x17\xb2\x92G\x95\x90\x7fi'
 'S\x1e~c\x1e\x81{g\xc4\xa1B\xbb\x95.N=\x18u^&w'
 ']\x1eM9\x16TI-aP%iU&\x99}2\xc7\xa5G\xc6'
 '\xa4F\xaa\x84 \xc7\xa5FfS#VF\x1d\x8fp rW4E'
 "9\x18^L\x1eO<\x17\x92r'XH\x1f\xc7\xa5H\xb7\xa7\x8d\xb7"
 "\x90'\x80i/\x9fz\x1e\xeb\xea\xe7\xc9\xa6J\x93t'\xa8\x82\x1eu"
 'W(\xc7\xa4FJ=\x19v[5\xb9\x9e`\xcf\xbf\xa1lO&\x97'
 'u#\xb8\xb1\xa6\xae\x9c\x80\xda\xd7\xd2\x9b\x7f7bL\x1bC6\x16W'
 'G\x1e\x98u)_U;^M!\xca\xa7KaX>\x9d\x83\\\xc4'
 '\xbe\xb3\xa8\x8c@uX\x1d\x81r^y`"\xae\x87"\xa2\x81<\xe6'
 '\xe0\xd5\xa9\x875\xaf\x8d;\x98\x7fTWA\x18gP-\xbb\x9bC\x7f'
 '\\\x1dqS(\xa3\x857y_!\xac\x87+t_@\xa3\x8fp\x9c'
 '\x809\xb8\x96<WL0L>\x1a\x99w0\x8bo(\x96u,\x95'
 '\x80b\x91m\x1e\x81f$\x83i\'\xcc\xbf\xaa\xae\x89\'WI"\x9f'
 '\x8cpWF\x1a\xa0\x88f\x81^ \xa4\x81&\x9c~@\xe7\xe4\xe1\xdc'
 '\xd3\xc6\x94p&\xaa\x8eX\xb5\x8e$\xb4\xa1\x81\xa2\x84H\xb3\x913\x90'
 'p/\x93v-\x89p2\x86l+\x87n/\xaf\x93UfK\x1a\xae'
 '\x9c\x7fdM\x1b\x97z/\x96t\x1eA5\x16\x9e\x8bo\xb3\x8b g'
 'P\x1d\x81j0\x7fh-\xa8\xa3\x95\x9e~,\x8apG\xd0\xc3\xaa\x9e'
 '\x83Q\x9f\x80.\x9bx+\x9c|)r["\xb0\x91>\xc6\xa4E\x92'
 'w4\xa7\x81\x1d\xaf\x8fBx[\x1e\xb6\x9eg\xb3\xa3\x8cdP \xa5'
 '~\x1e\xa0z\x1f\x87k<\xff\xff\xff!\xf9\x04\x01\x00\x00\xff\x00,\x00'
 '\x00\x00\x00s\x00$\x00\x00\x08\xff\x00\xff\t\x1c8p\x00\xc1\x83\x08\x11'
 '\x1aX\x90\xb0\xa1\xc3\x87\x10#J\x9c\x88\x90\x02\x00\x83\x14\t>\x00\x90'
 '\xb1\xa3\xc7\x8f\x1f\x11\x008p\xd0@\x00\x03\x02\x1d8h\xa8\x00\x00\x03'
 '\x900c\xca\x1c\xc8\x00\xc0J\x82\x01\x00\x04\xf87\xc0e\xc3\x03\x05\x10'
 '\xcc\x1cJTbO\x01\x03\x18\x0et\x10`\xc1\x00\x01\x00\x14(\xc5\t'
 '\x80\xc2\x00\xa1\x02\x11`]X\xb4\xabL\xa8\x00\xc2R\x10\x98s\xc0\x81'
 '\xb0a\x0b\x94,\x80\xd6\xe6?\x03\x05\x1e\x08\xdc\xe8\xb5\xae\xc7\x9e\x05\x02'
 '8\x08\xfb\xb6\x00I\x04g\x1d\\=\x98\xf3\x80\x82\x9c\x02\xfe\xd5T\xf0'
 '\xaf\xe5K\xbb\x90%B5(\x92dN\xc6=\x1f\xaf-\x80\xd2\xf1\x02'
 '\x00r\r\x9c\xc5\x1a\xd9#\x82\x01\xa8S\x93\x8e\xe8\xf8\xedF\x07pI'
 '\xfe\x83*\x94+\xcd\xa8\xff\x16\x14\x08:\xf9_\xce\xb1\xa5?\xe6l\xab'
 '\x93\xe2h\x05g\x19_^\xb0\x91\x81I\xbf\x03+?/\xb0@d\xe8'
 '\xdd(\x83{\x1c\xdev\xa7\xc4\x96\xbbGb\xff\x84\xba1,P\x00\x02'
 'H\xd7<\x8b^\xe8g\xf4l\x81k\xef\xc8\x1d\xad\xf7\x88\x0b\x04\x08\xa0'
 'pS\xe0\x02\x0c\x18(`\x00\x03\x02\x04\xb0Zc\xfa5E\x90\x03\xfa'
 '\x9du@v\xf3QT_X\xf7E\xe8\xd0F\x18\xc1dA3+$'
 '\x90\x10\x02\x01\xe8\xa7\x1f\x03 @\xd8\xd0\x84:\x19\x00\x82\x88\x0cd\x18'
 '\xd9\x8a"\np\x96\\1]P\x81\x0c9L\xb0I4\x03\x19\x80\x01'
 'q\xdd=\x84"\x06\xec\xb5\xc5Xi!\xc6(@\x89 %\xb0B\x13'
 'm\x84\x10\x16\t\xabt"\x90\x01\x0fl\x10\x01\x90hi\x86\x10\x8a\\'
 '\x86u\xa0\x85\x1ea\xc1\x05\x1e=\x88"\x8529\x12D\xc1\x1d\x10\xc4'
 "\x11&\x85'\xce\t\xe4\x91d~\xb4\x88.\xc9x`\x8b>A\x9c\xf2"
 '\x81\x87\x03i#\t\x127\x98g\x16q\xb2}\x19\x16\x0fF\x98\xe7\x00'
 '[\xc4UH\xd4\x05\x9cPCC\x13AH \xd3\x08Ql\xb1\xc7\x0b'
 'X44\xc03j\xa8\x81HX\x89\xfdH\xdcTTm\xff\x00\x01\x04'
 '(\xf8\xe4j\x90]\x89\xe1\x8a\x13\xd8\xc0\xe1A8\xfd\\"\rH\xc8'
 '\x14\xc3\x01\x15k4\xe0\xd0\x00.\xb0\xa0\x848\xac\xfa\x06d\x7fT\t'
 '\xc2\x08#_\x147\x9c\x96t\x0e4\x82L\xed\xb4\x82\x0b:\xc0\xa0\xb1'
 '\xa5\x1d\x8a\x80\x01\x0e\xa1\x14]p\x0f\x1bF\xcc\x12\x84\x90*P\x02\x88'
 '\x0f\xd1\xa2h)Y\x00$\xb2\x05\x0b.h\x0b\x80\x11\xb3\xd6Za\x10'
 '\x1f\xc0\xd4@\x14(\x9c\xc0\xc76\xf2p\x10\xd6\x1eY\xa82\x81\xa7\x14'
 '\xc9"\x0c7\x88X\xc2nB\x018Q\xca\x13@\xa4%#\x90\xfbJ'
 '\xbb\x04=\x80\xa8 \xf0\r\xb3\xdaS\xdc@\t\x10\xb2\xc2G\x12\xbc\xe0'
 'A\x04\xf8\xdc\xd2\xc4\x04k\xb4\x80V\x04-t\x80qD\x16\x90`\x88'
 '\x0f6(+\xe4\x0e%@R\xb2\x9d)\xe7\xd4\xc8\xc8)\x08\x9cK5'
 'c\x98\xa3\x85\xa5\x16D!FG\td\xc2\x03\x00-\x0cq\x81@\x16'
 '\x0c!e\x04(D\xa0\xc50NCt\xcd\r0\x84BHD\x01\xf0'
 '\xffa\x86\x19e\xd893a\x00\xf8\xd2\x87".\xef\x94S\x151\xc4'
 '\xa0\xc6>\xfbZ\xa3\xc3\xd8\x13%0\x81\x0e\x7f\\a4A\x96[\x01'
 '\xf3\x1fi$\x12\xcb+\x10a\xe2\x02+\x11\xe0Q\xb7C\x01\x84\xe1\x82'
 '\x0bi\x08^5\x00\xcd*Q\x84\xc0PL\xa1\xc4\x11i\xa4\xec\xce4'
 '\xab?4C0\xb5@\xf1\xc2\xd14w\xf0\t\x12tl\xd1\x8d\x0f\xb0'
 ' \x7f\x90\x04n\xf8\xc1\x06\x00/||"\x0cB\x08\x01C\xb4\x12\x02'
 "0\x06\x13L\x18#0\x00\xf38\xa1B\x19)'p\x0b\x0e\xc1'T"
 'N\x12\xbe\x08RA\xfc\x02\xe5lH\x11)\x94\xc0\x06\x1c\x1dX\x1bB'
 "\x12\xc0\x8e94\x02\x00!\xf8\x16\xdfx0\xab\rD\xab'aA\xc1"
 " \xee0\xbbq@@\x12[R\\X\x80\x00\t',!e\xff\x90"
 '\x00\x17\x9c\x81\xbf\x81|\xe0\x07^\x00\xc6\xfd\x1e\x82\x85\n\x00\xe0\x0c\xa9'
 '(A:\xac0\x01\xedY\x8e\x1f\x91\x00\x80\x07:\xa0\xbd\x13E\xe0\x04'
 'T@Kb\xff \x08\x80H\xa8 \x0c\xb3\xe3\x00\x0f\xb6t>=<'
 '\xa1\x0f\x1ftH\x03\xe0Q\x01\x05"\x84\x17?\xd0\xe1\n!\xb2\x02\x1b'
 '\x00\xa0\x10\xf5`A<\x0e1\x04\x0b\x0c\xa4m!\xd8\x80\xc4Hp3'
 '\x89\x80\x00HCD\x0b)\xe6\x90\x85\xd9UJZ\x00\xd0C\x07\xd9\xf7'
 '\x90\x06T\xe0\x1b4\x10\xa0@\x12@\x8c\x18\xc0\xc0\x03[\x8c\xc8\x07\xbc'
 '\x08\x800\x08!\x0e\xcc\xf8\x837\xf2\x01\x8d\x1a\\\x01-!H\xd8D'
 '\x88(D\x9e\xb4E\x0b<\xb0c\x90\x86s\x86\x14\xa8 \x10 \x1cH'
 '\x03\xdaP\x047,\xe2\x02\x17h@6\xfc\xe0\x89\x16$R"\x1f\x90'
 '\x12\x07\x1c\xe1\x05\x00\x08\xc2\x07\xbd\xc8\xc2\t\x0c\xf1\x8e\r\x84\xa0\x86\x14'
 'yO[\x12\xb3\x17\xe2\xb8h C\x9aMX\x02\xc1\x82#\x14"\x95'
 'g\xec@\x15\xceA\x02\x12\x98`\x10=\xa8\xc3\xe6:2\x81\x1c\xa0\x85'
 '\nh\x80\x02Z\xbe\xd0\x83C 3#\x94BK^\xca#O\x13A'
 '\x13Hya\x0b\x07\xd6A\xdc\x87c\xe0&"\x17\x98\xc1\x0f4\x01\x84'
 "/\\\x81\x043\xe8\xe1D\x16\x89\x96P\xec\xc0\x05'\x08\x8b\x14\x12\xea"
 '\x917\nnp\x84\x0b\xd3\x06\x92\xd0\xbdJ\x00\x00V\x10\x91\xc02\xfc'
 '1\x89\x19\x981&#\xa8\x80\xd0\xdab\x05\x1cX\xb1 \x1a \xc2#'
 ' R\x13;%\xa6N\\\x8a\xc0\xac \x10)\x1a\xd5\xa5\x0b\x1a\xe8\x82'
 '\x08f\xda\x10\x0b\xd0"\x07\xe4\xf0\x00(\xa4\xb0\x0bT\x88\xe0\xa9"\xd0'
 '\x80\x00\x08@U\x02\x90\x81o\xf1$\x8e|@\x06\xa4\x15q\xc0\x0b\x8e'
 '8\xdb\x03@\xda\x95\xa7\x12A\x1dr\xb0j\x06\xd6\x9a\x81\xb4Ru\x14'
 'y\xc8\xc3/LQ\xd5\xba\xda\x95\x00\xd8\\J\x00\x08\x84\x81\x00\x08\x08'
 '"\xa7I\rjP2\x00\n\xec\x07O\x11\xd2@\x06\xee\xbaV2P'
 'U\x00\x19xCP\x89\xa0\x81\xca\xbe\xa1\xaeD\xc8\xd3C\x02\x02\x00;'
 '\x03\x08\x94\x1c')),
'/bitbykweb.gif': ('image/gif', zlib.decompress(
 'x\x9c\x15\xd7\xf7?\xd5\x8f\xfb\xc7\xf1\xd7\xd9\xc79\xc6\xb1O\xe6!3'
 '\xeb\x94\x91\x95\x8e=2NF\xb6\x8e\x91\x19\x8e\xca.\x9ds\xaccv'
 '\x90U\xd21\xb3\xaaC\xc8\xaa\x0e\xa2C\xd4Q\x94P\x1d-\x92t\xf4'
 'nH\xe3|?\xdf\xeb/x\xfe\xf2\xb8\xdfn\x97\xa3\xb3\x83\xa9Y\xa8'
 '\x07\x88\x06\xfc\x14\x00VF\xd2\x7f\xff\xfe\r9,\xfb\xfb\xf7\xef\x7f\xff'
 '\xfe\xed\xee\xee\xf2\xf9|O\x0b\x99?\x7f\xfe\\,\xce\xf0\xb6\x97\xdf\xd9'
 '\xd9iii\xf9\xf6\xed\x1bg|8?J\xf9\x1a\xdd4\xda\xd7\xe2\x94'
 '\x9f\xe2\xd8\xd8\xe8\xcf\x9f?\xc3\x02l\xe2\xc2]\x93\x83\xf6\xb2\xf2\x15\xc6'
 '\xef\xf6\xe5\xc5h\xfd\xfa\xf5\xab>]\xb1\xb5&?\xdcn\xcf\x9d\x1a\xa3'
 '\xf6\x96\xda\xc1\xc1\xc1\xad\xad\xad\x89\x89\x89\xaf_\xbf\xb6\xb7\xb7oll'
 '444$D\x12O\xc5\x05\xa6\x85\xdarZ\x9d]Le\xbe\x7f\xff'
 '\xfex\xe6\xfe\xbbw\xefN\xf9\x9b\xfe\xf8\xf1css3\xd2E}u'
 'uuqq1=|\xdf\xabW\xaf\xd6\xd6\xd6\xba\x0b\x14\xd7\xd7\xd7G'
 '\xeb-\xab\xcf\x1a^\xb9re\xf8\xb2m\xf6\xb9\xb8\x80\xa3\xa6333'
 'O\x9e<YXXX^^\xee\xef\xef\x7f1?s\xf7\xee\xdd\x823'
 '\x01\xb1.r\xcf\x9e=+/\xce\xe9\xcc\xd3\xe0p8<\x1eodd'
 'dee\xc5\xd3e\xbf\x9d\xd9\x9e\x9e\x9e\x9e\xc7\x8f\x1eU_,\xef\xea'
 '\xea\xba\xdf`\xe3rhOoWcUv\xac\xb5\xb1\xf4q_\xab\xc9'
 'f\x87cn\xc6,\x16k\xa0L{zz\xda\xc5Z\xad\xf1\x9cf\xc6'
 '\x99\xb0\xfa\xda\xc2\x1b7n,\xbfx\xdaW\xaa\xe6\xe3v\x80\xcb\xe5\x16'
 '\xe6e\xf5\xb6V\xb9\xdb\xeb4\xd5W\xde\xbb|p\xb8\n\xff\xdfW~'
 '\x90\x95\xect\x9b\xab\xddA\x990w\xc5\xa1\xbe\xae\xdeb\xd5\xb5\x0fo'
 '&\x1a\xedz\xbb\xdb#\x8e\xaa\xf6\xdf\xbav\xe9\xd2%v\x9dy\x90\x8b'
 'B>%~\xe8\xa2\x9e\x9f\x93r\xc6\xe9\x90\xde\xde\xde+\x14\x93\x8a3'
 ':\xc5\x05T?\x0f\xd3\xecsI\xb9\x94\xe4\xf1\x06B\x1bM\x91\x16\xe7'
 'V~Z\xfdJ\x86zQ\xce\x99\x9er+;S\xd9\x18/\xc5\xb9Y'
 '\xce\x8d\x8e\x86\xda\xca\x92\xabYzDG\xfd\xcc\xe4\xd8\xba\xda\xf2q\xe6'
 '\xe1\xd2$\x9d /s\xa2\x93\xc1\xdd\x9eF\x0fk9Z,\xde\xc9J'
 'e\xb0B\xf7\xee`\xf7EFq\xdcQ\x83\xcb\x17sb<\xf4J\xf3'
 '\xcf\xf5\x94\xea\x87;(_\xbd\x90^x.\x91qR-9\x98p\xab'
 'H\xf9l\x8c\xe7\xf9\xf4\xd8 k\xec\x97\xcd\x8d\xder\xa3\x92\x8c\xb0\xdc'
 '\x94\xc8w\xbce_w\xd3\xacp\xe5\x10\x1f\xc2\x83\x16\xc7\xe9\x07\xe3\xf1'
 '\xfe\xea~\x87d\xab\xd2\xf5\xaa\x93q\xe5\xe7\xa3\x07o\xdf\x8a\x0f\xd0\x8e'
 '9\xa6\xeeK<\x18\xecmQ\xc9\xa0\xf5_\xd0\xacM\xd1\xcb\xa3e\xf8'
 'y\x98\xdcfhQB\x94\xcf$\x1c\xcfN\xf0Z}\xb5\x94B&y'
 'Za\x13c\x8e\xf5\x94\xe2\x1f\xcdL-=\xe3\xceNsj\xaa*F'
 'n\xdf(H2\xe4o}\xcaJ;\xd1xV\xc9\x8fx\x90\x9a\x119'
 'Pm\xd9\xd4\xd4t>\x83\xdc\x7f\x8b\xe5}\xc4(\xc6u\xef\xe71\xbf'
 '\xeb\x9dm\xa5\xf4\xb4\x0b\t\xcam\xadL;C\x05\xf6U\xa7\x8f\xeb\x1f'
 '\x02=-\xc9\x1e\xf2\x9f6\xd6\xbd\x8f\xe0?\x7fZ_Y~\xfe\xfe-'
 '/\xc4\x1a\xeb\xeb\xa4\xf5\xfa\xf5\xca@\x99f_\xef\xad\xf3\x89\xc1\xf9i'
 '1\xacB\xad\x87S\x0f\x04\x02\x81\xca/(\x08\x00\x04\x80.\xf0\xbf\xfb'
 '\xff&\x00\xa4\x00\x10\x08)8\xb1\x98\xa3\xd9H\xc9}A\x1cV\xc3x'
 '>f\xafK\x9dSw\xe3D\x11\xd60v\x85\xd3\xdd\xf4\xe0\x02\xce\xb6'
 'P\xc1\xb9\xa7y\xaaB\xcb\xab#h\xaa\xa7\xe5a5>|\xba\xce\xf9'
 'V\xeb\xece\xd3\xd3\x1b+S\xb7\xae=\xbeJ\xc8F)\xba\xf4\xb6\xcd'
 '59U\xec\x0b\x9e\xeem\x7fz\x8d\xd8\xe4r\xc5\xa5\xafc\xa1\xd3\xef'
 'V\xec\xcb\xe9\xbe\xce\xe77I\xe3\x85\x8aG~\x1c\xcf;p\xf6l\xbd'
 "[`\xffu\x0f\x02\xf0F\x83'\xe4{cy\xd8,\xf8\xfe\xcba\xaf"
 '/!@\x1a\xe4\xb9\xeb\x7f\xa9\\\xf7\xb1L\x11t\xc8\x9f\xf2\xc7\xc7\x01'
 '\xfd3\xe6\xff\xe4k\xbb\xdfW\xd2\xdf6\xd2\xd3d\xec\x14r\xd2\xa6\xd3'
 '\x9e\xd5\xeca\x7fx\xd8\xe6\xe1\xfe\xaa\x08\x11\x16\x0c\x84\x05\xc8Z\xee\xd5'
 "\xb8Q\xf3X\xd6\xf7A\xe5\x95\xa1T\x8ei\xdfO0\xadM\x9e\xb0'"
 '[Z\xeb8\xf4_\xea\xc0\x975\xe5\x87\x96\x1f^\x12w\x8fc`E'
 'ooD_1\xfe\xf6E\xbe\x16-\xb8\xb0\xfe\xdc\xe4\xbbi\xcb\x15_'
 ')e\xdfC;?W\x04\xaf\xaa\xfcZSr\ra\xc3_\xee\xb6\x9d'
 '\xb7\xfa#\x90X\x15\x0f\nz\xb0\xbaJC/\xabK\xe5\xa3\xe7\xc5\xef'
 '+\x01[nj\xbc\xe30\xa5\x1a\x9c\r\xda\xc4\x89A\x95\x05\xaf?\x8b'
 '\x83V\xe5\x81\xb3\x90\x83\x98\x95$\x01\xbfl%\\\x17L\xb4\x86KP'
 '\xa3\xeb\xe8jJv\xf2T\x84\xbf&\xbcX\xe9U\xaec\x91\xdeW?'
 'n\xb6\xa0\x0e\xa4\xc6\x08\xb3\xfb\xf6\xb6\xec\xbc\xd0G\x1e\x85"\xed]\x1f'
 's\xe8\x95\xfa\xdb\xb2\x7f\xe2\x17\xd9\xc7c\xfe@\xc0\x15\xba\x1a\x1f\xe5j'
 "2O\x981\xb2\xa4\xb1\xdeKA>U'\xd4j3Co\xaf\x86\xc7"
 'Lt\xab\xd6\x86\xb1\xdes/\x93\xc1\xb85\x82\xe4V\xcb5\xc2D\xcc'
 '\xe2\x07_-\x16\xdd\x06~\xf5\x04\x7f1\x06B]Tg\xea\xab\x05|'
 '\xa0\xd6\x1c\x83\x97\xb5\x9c\xd7[Zo\x829wD\x9e\xce/7V?'
 '\xe9\xfeo\\\xbb\x92\xf2\xc4\x9f[\x9e\xd9 \xf0\x9bk\xb7\x90\xe9\xdd\xd7'
 ',`\xcb=g\n\xd6\x11\x94\x86\x96\x04;6\xeb\xbeL\xe6\xd3\x8e\x9f'
 "*\xcf\xb5\xad;\xdd]\x18\xcd\x8a\x0e9'K /\xa7:\x08\x1cQ"
 '\xa1\x96\xae\xd1H\xa3\x93\x00\x0fNa\x0f\xbc\xab\x92O\x00\xc6\xc7\xcet'
 '\xb4^\xf74\xe5\xfe\x0f<\x14pS\xe2z\x1cc\xa4g\xe9\x08\xf1\xfc'
 "\\\x8a\x8e8\x88'\x8a'\x80\xe4O\xb2\xd8\xa3H\xcd 2\x08\x9c}"
 '\x84rDUI-\xbc\xe4\xb6\x9c\x11\xb2\x1ak\x7f\x92{\x1f\xe2\xf3\xa7'
 'y\xf8_\x08\x94\xcfF\x13\xb96\x10\x11\x06\xf3\xeb\xb4n\xd3\n\x18\x86'
 '\xc6\x17\xeb\x1f\xc9\x95\xf3Vh.\xdd\xe7\xc8m\xff\xe6\xe0}:\x85\x89'
 '\xba\xf8_\xc8\xe6?H<G\x16\xc6\x00P\xae\x81\xbcoO\x89\x8e\xf1'
 'T$\xdc\x083\x0e\x87@\xd9\x9e\x19\xf0\x97m\xff\x1d\x963\x1c\xde\xb4'
 '\x0fz\x0cW\x8f\x80\xe4\xea1F\x0e\xed\xfdK\x04 ]K\x9a\x80\x01'
 '\x0f\x97\r\xd2#]Ov9,&\xf0V\x00N\xb6\xee\xf8\xcd\xed\xca'
 "\xf4\x1e\xb3='9\x1d\xc6\xb3}\xe0\xd3\xdb\x96\xe0+E\x00\x9d\xfa\xe9"
 '?.bPC"\x08\xc36\xcfId\x9c\x87\xfd\xf3P\xf0}\xd3\x91'
 'RH|\xb3\x8f\x81N-\xcc\xc2\xacg\x16\xb8\x0f5B\x83G\xaa7'
 '\xcen\xc9\x99\xd9Cq,\xc2{2\\\x05*e@\xe7\xb2\xc1H\xcb'
 '\xb3\x12\xf7\xb2\xae~~\x93R\xd2\xa4GT\xe8?\x7f%\xee\xfb%\xbd'
 '\xfb\x96\r\x8f|\x19\xcc\xce\xb0\xd7w-\xec\xc9^\xa4\xd1\x95\xf3n\xdc'
 '\x1c\xcc\xc1u\x12\x00\xf3?\x7f7\xfe\xc6\x89\x8b)\x99\xb4\xc5kS\x87'
 "\x8a\x1e\xbdIj\xb9\x8aJ'R7\x9e\xabJ\xa9\xb5\x91\x05\x04\xde\xce"
 '\xabc\x14\x99:\xb1sI\xdacP\x1a1[\x96w\xfd\xf4\xc3La'
 '\\\xd7w\xec\xf3\xbf\x10\x97\x182Hy\xf3v5\xe6+(\r\xf0\xa6'
 '\xdf4IS\x13\xab\xdf\xb0W\x85\xdam\xc8\x98\x96M\x99ahI\xbf'
 'l\x90\x97\xf0P9:\x13\x865*\xf8O@\x91\x1a\xcb\xe6\xf1\x9d\xb4'
 '\x00\x19\xeb\xbc\xc5FU\xb9w\xd6\xae\xb1\xf2"\xd2\x07\x06\xe1\x96\x18\x9a'
 '\xba\xd6\x182\x87\x07\xddc\x84\xa3\xab\x99I\x97Os\rD\x95\xc4a'
 '\xf6:\xe2u\xf7\t\x939;\x1bN+\x97\xc2l\xc1,\x90\x8eR\x19'
 '(\xa7\x06\xf8\xed\xca\xa5\x88\xa4%\xa8\x85\x9d\x15\x96\xff\xadn\xa4[\xb9'
 'Zr\xc5%\xdc\x06\xac}\xd5D?\xe2\x08\xd93\xe2\xe8\x93\xefea'
 'W\x1e\xfa\xa964)&q(\xda\xeb\xdb\xf0\xb3+\x00\x98\xeb\xa3\xeb'
 '\x9a\xf0\xee|\x0c`\xd7!1\x96\x7f\xab%\xd4H@Q\xab\x96`\xde'
 '\xcfazVb\xcc\xc6\x9f\xcc\xd0\xbb\x9b\x80\xcd\xa0U\xcfz\xfb,m'
 '}(r\xb3\x86\xa3\xd02\x9e3(\xee\x16"~\xee\xca\x9ff!\''
 '\x16\x05\xc4@\xd7\x82\xbd>\xcc\x1c8\x95g[\x98g-Q\x00Q\x16'
 '\x9dB\x88\xac\x86\xd6E\xb7\xab\xdb\x0e\xa5;a(^{\xd3\x18-['
 't0>\\\xa2\x8b$OZ\xd4\xaa\xfd%`\x1c_zJRo\x02'
 '`a\x18\x08\x15u\x06\xf4k\xfe\xda\xf8%\xff\x07Q\x8f\xf4.\xc5\x02'
 '\xef?`b\xf1\xd9rR\r\xa8\xbf{\xcf*I>\xb8J\x8f\x03V'
 '\xc8\xd6\x06\xc4\x0f\x07j\xa4I\x171\xed\x9aS\xae\x1f(UK\xa3\xa2'
 '\xa2\x1c\x02\\+\x94r\xa9\x1c8\x01+\xa95\xbe]\xdb\x9b\xf7j\xae'
 '\xc2\x9b\x02\x16\xb5#\x80S{\xbd\xe5\xf5\x92\xd9{N.Q\xaa?J'
 '\x05\t\xcc\x16\xaeRT\xf5\x13\xa2\xad\x01?i\n\xfe\x86\n\xa4\xc3\x98'
 '\x02>\xf0v\xcd\xda\xe1\x18\x05\x86\\\x95\xd2"\xbd\tyWF;\xf0'
 '\xad\xb1\x13\x8e\x1b}\xc8\xea\x7f\\\x9f A\xbbb\t\x86i\x83\x84\xf4'
 'q\xda0\x1c\x1e\xb4\xf0n\xd7\xbb;\xe4\x83\xb0\xbe\x13\xfb\xc5|LE'
 'Y\x92-\x0cL\x9e4+g,\x88\x8e\x10\x10\xa9q\xd6\xc6\xe9\xb1\x8c'
 '\x0c\x19\x9c\xdc5\x9cJ]#\x030F\xf6\xc7\xfa.\xb7\xdb\xd7\xa5?'
 '0P\x08\xc5>Y\xaf\xd0\x9a\xa6@F\x05\x12&qy\x9f]\xe0\xc4'
 '\xc5k\xc8\xcf\xf7o\xa1\xa3\xa1\xc7~b\x84tY\x04Q\xbf>\xd8\xb6'
 '+3\xff\xedDb\x17y|B\xac\x94\xd3\x980\x0f\xdc\xf2\x81\xe8$'
 'L\xady)\x14\x8e\xa3\n\xd8\xab\xfb\xf3\x18\x83\x1d\xf1&\xb7\x03\xcad'
 'E\xef<\xaf8^\xae\x0b\xbf\xca\xde\x87\xfe\xd7\x93\x0b!\xf9`\x8d\xb9'
 '9\x10\xbe\x86K7\xb8\x0b\xc0\x11uD\xed\x93Pr\xc2\xd2\x89k\xd7'
 'CSU\xd2\xc0\xf9\x8f\xaeKz3\xa9\xa2\xc5\xb7\xfd\xbb\xf1=\x1e\xd9'
 '\xb8w\xae\xde\x01\xcfd\xb0T\xa9\xb1\xbf\xf6E\x9b:\x94`\xc6\xb8\xd0'
 '\xa5\xb7u\x0e\x99\xbe\x94\x8f\x9e\xd5\xce\xd9D\x88\x88Q\xea\xc8\xa3\x86\x83'
 '*]\xc1_\x8a\xdc\x0cs\xe4\x85\x17\x06\xe5>O\x0b\xd8\xdeT(Q'
 'GS\xf9%\xa0gE\xcd\xd9\x13\xe1\x03 \xa2\xe7dX\xd3\xa5\xea\xde'
 '\xdc\xa2\xbf\x8a\xc8\xa2\xf4\xc1\xb7\xf7\x80Q9+\x13%?3\x8b\x07\xb0'
 '\xd4=\xb4K$e\xd1\x9d\xcb\x96\xddX-\x81\x179\xefV^\x9c\xcd'
 '\xb1\xa0\xe8\xd1)\x0f+6\xe8\xc3\xc3Fm4S:\x0e\xebh\xb0\x82'
 '\xb8w\xe7\xef\xf3\x89(+\t\xcc\x1fk\xcbF\x99\xddI\xf8TR\xe3'
 '\xdc\x03a%\x97^\xee)\xa9\x82\xa8\x98\xa4\x85\xae\xadZQ\x89\x1a('
 '\xd0\x8f\x0f\x03u\x81\x153\xd4i0\x1f]\xcc\xc09!\x80\x99\x06 '
 '\xb0\r\xa5\xce\x02u\xd8\xb8\x8e\x12CE5&\xf0\xe7\x94\xb0\xd4|r'
 '\x95\xe1\xe7\xb2\xb2\xf8\xff\x85R\x05A;\x05\x17;\x15\x87\xc9\x9d\xc2l'
 '\x87;\x8d\\0\xb0T\x11\x96\xfe\xd3P2a_\xb4D\x01Cx\xf0'
 '\x9f\xcag\x15\xab\x8d\xd0\x0bi\xe3\xfa\xff\x05O\xb9\xb5\x9e9[\xce\x85'
 'P\x8c\xba\x05\xb0\x83\x01\xc8\xe7\x10%?\x13\x80E.\xd0\xefbK\xfb'
 '_1\xd8O\xb7FH\xdc\xa3\x81\x9e\x89\xf6\xf7\x8f\xfbP\xbc\xee\xdb\xcb'
 '\xae\xc2oC\x17_\xe6}\xefK<M\x8ap\xba\xf9bV\xed\x80\xa5'
 '\xf5*A\xb8\xc7\x87.\xed\xea\xe2~\xea\xd4s\x01\xb9\x07z\x8aM\xbf'
 '\xe3\xc4\x13M\xe4\xdd\xafhX)=\x1d\xe1\x03\xd3\xd4\x1a\x95*%\xc0'
 'T\xbb\xd2g\xc8\x81\xecC\x1a7J\xe9\xe1\xccg\x8e\xfb\x1c\xe5K\x07'
 "rpZ\xa1\x93\x8f*S;g\x85\xad\r\x90X\xd7'\xdcF\x0c\xb3"
 '>\xa9\x03\xf3\xb4f\xb1\xb7\xf5@K\x88d\x924OR\t;\x8e\xb0'
 '\xc2\xd0\x156ah>sS8`\x0e\xe15svK\x93\x90\x86\xec'
 '\xd7\x9a\x9bu/\x95\x92e\x13\xf0\xa6\xa43\xcd\xf91"/\xd6\xc7M'
 '\xc9\xeb\xb9B\xdf\xce\xce\xaa\xa4r&\x7f^\x07`\x947N\x9e\xa6v'
 'o\x0c\xad_F\x01\xd2\x17\xe7O\xdez~\xd8\x85E\x91\xf8\xd6\xf8\xeb'
 '$\xb6\xb6\xac\x98r\x0b\xcd\x96N\xe4\xd8\xca\xa6\x90\xe8\x03\\\xd0 \x98'
 'n\xaf\xec\x8e\x13\x85\xf7\xda\xc0\xf0t{\x1d,\x9b"\xb1\xce\xdd\xeep'
 '\xf8\xa9%\xce\xa2*C\xf7"X\xf4\xbb\xdfN\xf3~\xc8\xf8\xe3\xb6\x0f'
 '\x99ZK\x91\xfdh\xe2\xdf\x18\x178\x15\xbb\x82w\xd9\xe2\t\xc9Nc'
 '\xbb\x05\x87G\x85\xfe\x0c\x85<\x87\x8f\xae\xc1\x91\x02o\xce\x10\x08\xc5k'
 '\x94u\xf6\x89u{\xbb4\x8f]\xf7\xae\xbd\xb7\x90\xb1\xad\x0e\xfc\xe5!'
 't\xf0\x88"r\xfa\xed\xa8\xd8?\xcc\xac\x89(\xd8q\x0cU\xc2\x14f'
 '\xcf\x87\xee%\xc0\x8c\xf1\xe1_*\x8c\xdfW\xc0S)\xf0h\x86\xf0,'
 'Wx\x8a\x02O%#\x08\xe5B\xc3\xbeg\xe7)\xb6\x87\xd9\xa7\xf9\xf9'
 "1r\x8e\xc9\x00\xe9\x8c\x029\xebB\x03-\xdd\x17\xdc\x9dkK'\xc1"
 '\x94}!\x87e\x13\x8f\x82\x82\xf6\x90\xa3\xc0<PR\xb5\x8f!\x17\xa9'
 '\xc8\x03_\xcb\r\xf0P?\xb5\x7f4\x0c\xb2\x83N\xe5\x83\xd2\x19\x88\xfb'
 '\x00\x80\x1e@\x1d\xe1B\xde\x90\xce\xe6`\xc0\x1edh4=O\x12\x0f'
 '\x0e\xc5A\xf7\xb4\x99\x11\x9a]a\x181&W\x98\x84GQ\x19\xf9M'
 'x\x14\x89!LhD\xa6G\xc1s\x08\xf0O}\xb6\x87z\xc9\x1b\x1f'
 '\x88~\xa43X&ZW\x00\xa6\x0b\xe3\xe8Ud\xbb\xc3\x03\xb6\xd2\xbd'
 '\xd4\x08M\xa9\xc9I8\x1e\x07\xf0y(W\x00\xcd\xfb l\xa8\t\xb4'
 '\xb2Q\x0e\x94\xe0S-\xc1D{IArn \x1b9\xcb\x07\xc9\xe1'
 'c9\xb0\xbcCl\xe0\x18\x1e\xa6\xc2\xca\x0b\xc5@\xd9\xc8bo^^'
 '\r$?\x03\xa2\x0f\xe3\x014\x0c\x92\x0c \xe2n\xa7\xcc\x9a\xa2\x08='
 '\xc2\xaf}\xa8=\x14\xdbx\x86c\xa6TF\xc1\x0e\x16E\x01\xcd\xcb\x96'
 'b)\xb0\x0b\xdd\xc2C~PG\x1e\xdc\x11\n=\xc6\xb2u!Y\x1f'
 'X\x94\x8aL\x15a\xbc\x17\xc6\xb0\x84\xb2\x00\xc4,\x0e$\x81O8\xc3'
 '\x06#p\x08>\x0et\xf1\x04\xfa"\xc3\xcc\xbb\xc9?\xd4X\x92\x1c\x0e'
 '5\xe4\x81n\x11b\x93\x99\xa2\x92\xb7a\xf7(>\xed\xb8\xbcc\x04\xa4'
 '#\x99jK\x84\xd8a\xcaU\xd2!5\x86\xa1\x7fr\x03\xdf\xf4\x00\x95'
 '8d\xdcO\xb8\xfe\xc7\xf28\x84\xf0\xd3Eg\x0f<\xe8\x12\xd9nK'
 ' \x9bm7\x80\x91\xbf\x06h"i\x9aH\xb4,\x1f\x9bO\xa8\xd8\xcb'
 '\x8f\xc5\xe4 \xd5y\xa5\x13\x92\x90\xc7\x13R\x91\xb2\xc7\x1fa\x84FX'
 '\xe0`\x96P"\x06\xe9J\xc9\xce<\x8a\xe0\xa5 \\y(g\x12Z'
 '\x9f\xec/\xb4\xc70\xf9\xbb\xc4w8D\x8c\x02B\xb1U\xd5R\xd0r'
 '\x05\xa5\x9fl\xa1F\xc4\x83\xe6\x8cjs\x12\xf8\xdaw\x1f\xcd\x13\xd1\x10'
 '\x02\xe8\x1a\x0f\x9d\xc8CX\x90k\xf2?"\x12q\x15z=p\x7f#'
 "P(K\xd41B\xa8j \xd6\xa3 \xdc\xfb'\x82D\xce?\xbb\x98"
 '\x7f\x81\x8f5\xd3\xb4\xb6\xc6\xd5Z\xd5\xd8\xef\xe5\x97\xaa\xf2.z\xef\x88'
 '\xdd\xef%Z\x86\xa6t\xf1@\xd3,\xa1\x11<\xe24\x0b\\F\x82d'
 '\x12JuO\x81XxT"\x0br\x99,t\x97\x8d\x9ap\xf2n\xef'
 '\xcb\xd0*+/\xe1\xa1\x9a\xd8P\xdd1\xb0_K\xa6\xd9\x832kn'
 '8r\xf0\xbc\xab\xb1o\xc7B,5\x1d%K\xaa\xb9, \xc3\xde\r'
 '"/\xb3 \x96\x80Z\x1c\xb7T\xd6O\xc8\xf5\x9a}>6\xdd\xd29'
 'Y\x96]<\x8bDP\xd9\xf9AB\x80&\xbb\xde\x9bW\xaf\xeb\x89\xf8'
 'c\x9a\xa0\xd7x\x91\xff\xe2b\xb53\x06\x94\xedz\xa3@\xf2M\x0f('
 '\x80\x01\x8du\xbc\xdc?(\x121\x96x\x99\x0b\x1ba ,\xf8@+'
 '\t1\x11\x1dr~JBw\x12\xeeL\x86Y\xf0\xd0\x17\xbaa\x9c\\'
 '\xd4\xf0\xb5\xd3\x8e\x18\xf8!\x13\xef\xce\xb4\xa3\xd8>\xaf\x19\xe8\xc1\xfd\x80'
 '\xa8\tK\xa8\x88\x95\x1b\xcc\x85\x05\x0e \x1b\x98\xf5\x9b\xedp\x00e]'
 '\xc0s\xce\xfcf\xdfi\x86\x91O\x05)\xf3\xcb\x13\x81\x12\x1a_\xf6\r'
 ')\xfeS\x05L\x17\x9c\xb4:\x89\x94\xfc\x89\x85o\x9cC\xee;\x05\xe2'
 '\x0b\xedc\x8b\x08\xddb\x1c\x0cM\x11\xdfW\xa4\xcc\x82\xa4\xf3 \xf6\xbb'
 '\xb2Lb\xba.\rfE\xa6\xe8\xb0\x90\xca\x00y\x0c\x17.\xe9\x00\x9e'
 '\xaa-\x985\x02\x1cp\x97O\x13\x91\x99\x82\x06`\x08@\xfd\xe8C\xed'
 ') {\x90b\xb6\xbc\xc2\x17\x8d\xf4EP-"\x11 \x13~\xd3\xbf'
 '~\xb0\x0e\x1bm\x13\x0bq\x18Ju\xca\xb0\xab_Kc\xce;z\x98'
 "'\x7f\x82\x03\xab\x055\x16\xcc\x1aefc&\x95\xbc\xdf\x1c\x9a\xc1\xc7"
 '\x16q\xe8\xa5;\xb2\xe1.!\xed\xb5\xcc\xaet\xb8_\x0bX;\xdbK'
 '\xc8!\n\\\x03-\xa6\x80RyhO^\xa7\t\x1b\x9aJ\x01)p'
 "U'\xd8\xd7.\x03\xa0\x0b\x04\x7f<\x03\xa4\xd2\xe1\xbf\x9c,a}\r"
 '\\\xcd@|&^/\xe7\x03f\x14\xd0y\x8a\xcfoFQ$+5'
 '\xd6!T\xc1\xcf\xc5{\xbe\xfd>.\xb31\xf6r\xe3\x12l\x82\xdc\xf1'
 '9\xddN\x9b\x17`m\xec\xf6\xd5\xd1\xde;\ni\x15P\xbf\xf6\x0bn'
 '[\xdb\xb9\xf5\xa0\xf3\xc2~\xa1bdB2\xae\xab\xd5\xb9\xabcO\x0c'
 '\x84\x1b\x13\x80\x03{g\x93\xd6\xf6I\xde\\/\xa0=\xef\xce\x04\xa1\x1a'
 '\x00\x90\x0e\x19\x96\x08\xc0\xc5\x04\xe4t\xbd\x1eD.\x19\x96\xc5\x862\xf1'
 'h?c\x88"\xa9Z\xf2Cu\xa3\xa3\x84`\x01\xa4\x04\xd4\xf9\xee\x83'
 'U3+\x93Ib`^\xe3_m\xebC\xd7\xe2f\xf7\xa5_\xd9\x87'
 "L'V\xf6k\xb3F\xc8-z\x9e\xa0'\x04\xf8a\x00\xf9\x98\xc2\x8a"
 "\xe4'\xd9\xf1\xacD\x8aj\xbb\x03\x90\x04\xb9\xe6tr\xbd\xb4\xbcl\xfa"
 '\xfb3wve%X\xddK\x1b\xdd\x88\x80.\x1d\x13\xb3\xff(Q\x8a'
 '\x14HfL\x88\xf6o\t\xc1{\xb0\xdfwt\xf3\xb3\xb6j\xfe\xf5!'
 'm\xe4\x88\xb3F&\x1bjFD<H>^m\xdbD\xca\xf5T\x13'
 '\x0f6\x04\xc4\xccxtO"\xf25\n\xf5D\x1b`0\x8a,dO'
 '\x86x\x87\x8a\x1f\xb5\x97a\xf7\x85\xfc\xeek\xda\xd7\xafP\r&8Y'
 '\xdb"c\xe4\x11\xa0\x06sV\xf2\xe5\xfaA\xb9a\x17\xd6m\xfd\xb5\xdb'
 '_\x87d\xc7\x03Zas\x16\xf2\\p3\xc3\xe7$\xb9\xda\xa8\xaaO'
 'o\xff\x01Qm\xe0\x94\x003\x08\xf0o\xb0\x00\xc4*{(\xa3?\xea'
 ',\\\x83\xc9\x14\xd5\x8b*\x9b*\x14y\x98\\~\xb3P|>\xd3\xc7'
 "\x99\x0f\xac\xc9\xa2\xd2\x01\x90'\xbb\x11\xcc\x04\xff\x88\xa5\x1b:\x80/h"
 '\x88\xf7\x17\r#\xda\x86G\xc8\x83\x9b\x1f\x86\xab\xb0#\xff\xed\xe9L\xc7'
 '\xb0n\xc7T\xfaRF\xd2:Gf\xe4eudK\xdf,\xd2\xb9\xbf'
 '\xbb\x9f\x1c\xc1\xcc/\x03p\n\xd4\xdf\xfe\x86\xdc@\\\xac\x19\xd0\xcb-'
 '8E@\x9co\xe8V\xe0\t\x13\x02\x0b\xa75\xeeFx\x1e\xf73\xbe'
 '\x91\xe8t//`\x18\xc6\x1b\x00\xb3\xa3h\xfc\xeb\x0br\xedG0\x97'
 '$\x99p\x9bd\xeb\xe9\xf6$\x18\xc9>H\xbe\x03\x1cW\xa9p[\x16'
 '\xb3\x02\xadF\x1e\x1e\x8b\x8b\xf4\xe4%\x1e\xcf\xbc\x1c\xcc\x18=_v\xfb'
 '\xe1o\xacA*-A\xe1\x9c\x19\xebz\x92\xf8\x1d\x9a\xc5\x1d\x93\x08`'
 '\x8e\x12e\xc8\x00\x11\xb9c\xbd\x0f\xff\x87\x94?\x980>W\xeb\xd3\x89'
 '\x01u\xf3Q)\x82|\x9f\xe9<\xab\xeb\x16\x90\x14\xcc\xfd\x0f\xe6\x13\xaa'
 '\x86\xc0(\xecn&H\xf82\xa14K\x06=\xb8\x9e\xf5"\xc5\xd2\xf1'
 '\xc8\xfd\x943\xb0`\x9d\x8e\xc9\xe1\x89\xa4\xb9\x89\xe3#\x15\xe4\xdf\xae\x99'
 '\x84\xc9\xa1\xccI9a ve\x14`!\xa6X\x0fG\x84/\xb2('
 '\xd9g\x14z`\xfb\xcd\xf6\x93\x00\r\xf2\x1d\xbf\x13\xa8g\xa4\xea\xc9\xe8'
 '.\r\xf13W\xfa\xef\x9e\xdf\xe6\xdc\xe6"\xce1\xce\xbda\nu\xb3'
 'P~\xc9\x80\xa5\xb0\x86.3\xa7\x93\x84p\xe1Z\xed\xbaL\x95{\x01'
 'wp\xc7\x93\xa8\xb0&vMY\x00\xeco\xc1M\xa6\xec\x05d\xd0\xc4'
 '\x9aa}\x8fl\xb3\xcd\x10\xb2C\x18\xe8\x12\xbe\xf0\xa8\x8b\x19y\x0c\xe9'
 'wv4\xead\xc7T\xa7o\xdc\x1fY\x1a+\x1f\xf3\xb2V}\xa7\n'
 '\xc0\xccL\xca\x9dQ\xc3A\x0c\xb81`\x00\xf2\xb0\x8b\x9a\xbewH\xcb'
 '\xfa\x8e"wV\xef\xc9P\x1b\x11\xa5\xe3\x07\xc6`\xa9\t8\x8e\xa1\xe5'
 '\xc1\x90\x8f\xc2\x9d\x026\xc20\xe3\x91\xedLE\xd5\n\x92\xcf\x13\xc1b'
 'd\x93\xc9\x08\xdb\x17S\xac\xcb\xb12jW\xdfe?\x06x\x08\xf1\xe1'
 '\\_r\xbd@\x81+\xbf\xd3Q\x9e\x07\xbb\x0c\xb0\xdat\x9b/3\xb9'
 '\xf23\xdc\x01a\xe0g\xfa\xd5\x0c$\\:n\xcez2L\x8f\x04\x98'
 '3\xa171\xfeJ\xbc\xb9\x99\xb3\xd6\xaa\xc1\x12\xc7\xe8>\xb7p\xa0\x83'
 '\xbfe\xcfP|\xb4\xaf\x9c\x8b\x88\xce\x8b\xc6\x82\xedq\xc2\xc5\xae\x9c\x0b'
 'sw\xa1C\xb2\xb2\xb8\xf9N.\xe8\xa0H\x84Y\t\xe6\xe6\xe2m\xde'
 '\x87Q,.\xf6\xc9 \xea\xebL\xfdkG\xb7\x1bA\xb6.\xb3\x907'
 "\x83Bk\xfe\x9d\xa6\xcb\xc3\x9f\xd7'\xc0n\x0b\xe8\x0f\xe8\xb1\xc1\xc7g"
 '\x86\x91\xda\x97&\x15fT\xab\xf9\xc5\x8f\x17\x8b\xa9\xc4gjA\x0fT'
 '\x87\x01\x11\x1c\xd8\x80\x01\x023\x85\x8b\x01\xb1\x12\x1c4i\xd6\xac\xa9+'
 '\xa6"\x1c\xeawBL\x01s3\xefg\xae\x0f\xa3H\xde\xbf\xc2\rS'
 '\x1c\x8a\x07K\nx\xf0\x15\x85\xa7\x99\r\xa2\xa3|\x04O\xa6+\xd1\x17'
 '\xdd\xbc\x0e\xff\x85z\xb1\xe7hb\x03W,\x1a\xf3@i\x06\xf4\x8e\x1e'
 '\x04Vp\xbbp\xdb\x0c2KH\x81\n{m \xc0\xa2\x15#\xbf\xd9'
 'qE\xf1`\xc5\xc9\xd4\t\xa1\xd1=\xdd\xef\xcc\xbaaY\x0fu\xc3 '
 '\xde\xa8\ne\x00Q\x1c\xf3\x8c\xeb\x03L\x9c\x04\x1b1{/\xf0\xe1\x8f'
 '(\xd0\xe9\xe0\x90\x99\xe0{?\x8e\x0c\xf1\xe2\x90Md\x84\x19\x1fH\x02'
 '\xb1\xcb\x0b_J\xccCc\x99P\x9c3\xd4\x18\x0f\xf5\xe6B+1\xaf'
 'r\xfet\xce\xa1\xce] \xcc%\x1d\x15\x1ea\x0bu2\x11\x9f\xff>'
 '\x90\x9e\xb3@\xb3Q\xb7\x15\x91\xb3\xa4\xb4\xa4\xb9\xa1\x16\xfccK;\xc8'
 "\xad\xe5\x95\x9f'\x1d\xebx\xc5\x03\xe7Va\xee\t\xf5\xd5\xb1\x12\x9b\xac"
 'T\x18/\xd7\xb9\xb3\x7f\x83-\xf1\x0f\x9b\xcc\xfbP\xe8\xdf\xb2\xe7\xd5\xf2'
 '\xd8\x8a\xffL\xfe\x98)\x19\xc2e@\xcbX`>\xe1MGU\xd8\xde'
 'K\xcex\x81\xb0\xff)L\xbd2\xbf\xae\xeel\x19\x18\xdf~\x0cw\xc9'
 '\x96\xfb\xc0\x94\xfc\xd1\x80\x00\xb1\xc3C\xad\x19\xb0U\xb7\xd8rL\x027'
 '\x1f\x9e\x8a\x146\xd5\x81}\xc6#0$QW\xa5H\xfd\xbaG\xfa\x80'
 '\x98$\x1aQ\x8a\x8fW\x14\x19\xe6\x1c\xcc\xd1zT\xe1r\x0e\x94Y\x93'
 "\x9fa\x8ar\xf8\x87\x8d'\x8a\x86\x907\x07\x19\x9b\xd3w7gnl"
 '\xd2\x01h!\xa9\x8f\xc8\xeb\xbfz\x0eS\x1e\x89\x0cso\x89\xbb\x86\xba'
 ' \xbevA\\\xb4\xd9m\xa9`\xb0\xe6t\xf1\xda\xdf\x9299=h'
 '+\x19t\x9a\x07Q"\xbcyx\x82\xad)\xfd\xa2\xfc\xf6S\xbf\x16\xc0'
 '\x8a\xdd\xb0@N\xe7\xeb\x00\xa7\xfcK$\xbd!\xee\xc4\xc0\xdf\x9a`\r'
 '\xee\x9a1\x01\x86\xe3\x0f4;\xa4a\x01t\xb3\x122\xce\x17\x9d\x89\x91'
 "m`\x81\xff>\xdcp{\xf5Z\x0e1\x8e'\x8c$\xff\x06\xa5Z\xc4"
 "\xfa%\xa3}>\x9d\xd3\xd2\x98\xfev\x83\xe9\xa2\x07R\x89\xce'\x11h"
 '\xd1\x02\xfc\xe6\xf9\xfd\xa2>\xe4\xd9\x11\xc7\xb3\xe6\xf7\xfe\xb3\xbc\xf9\x9f:'
 '\x8e\xeeHJ\x12\xfe\xf4~|\x84TJ\xce\x0fU,\xe9sZ\x0ey'
 '\xa9\xbaL\x9a\x96\x08\xec\xec#nQ/\xaf]\xb1\x9f\x99t\x85\xdc\xbf'
 '\x0e\xca\x02\xc8\xfcz\xb3\x1c\xf3/\xca\xdb\xcc+&"\x18<b\x84|'
 '7I\xbc\xfa\xf4\x1e\xbe^\x10Q#{L\x83\x0f\xb6\xc3A\xd5EN'
 '\x00\xa4Wfd\x04\t\xb7\x1d\x7fW(\x0c\r\xb2\xe0\x83FY\xa8f'
 'f\xa4O\xd3A\xe3\x88\xa9\x00\x1c\x08\xfc\xf0\x96\xf4=\xd9\xb2%\xc4\xd0'
 'nV\xe7\xb3d\xe7x\xc7\xf3\xc0\xb9\x84\xb3\x08\x16\x03btO\xb6\x80'
 '\xf5$\x12\x0fk=\xbf\xdbvu\xb7\xd5\x03\xb9\x9eFm\xd8tDe'
 '\xd9o\x90\xffGOm\xe6@\xed\x14c1\xf8\xfam\xb3\x87\x8f\xdd\xcf'
 '\xd5g\x11\xbeGl,\x97\xcf\x9e\x8dy\xb9\x96\x80\x03F\x01\xb4\x12\x0e'
 '\xc8\xf9\x07N\x1d_\xd1\xb9\x80\x89L\xfd\xa9D\xfe\xf1\xb9\xf4\x96\x9a\xc3'
 '\x15u\x01\xc3Q\n\xfa\xc4\xdc\xfe@\xcc\xf59"\x0e\xdaEz2\x04'
 '\xa0\xa7\xf0(2\xb1\xc6\xca\xfcZ\xb5&l\x01\x80\x9b1\xa0x<\xe8'
 '\xd0\x07+\x95;\x9f\x02\xe0\x18$\xea\xac\x041\xfaQ\x9dtz\xac3'
 '\x88K.R\x00u\xbb_\xd4:`\xc3\x11\x91T\x93\xc1\xe1\xf8\x8f\xdf'
 ':2T\xeci\xc2D&\x15\x06\xa0\xf0$\xce\xdc\x81\x07\xd3y\xfbO'
 '\xec\xdb\x18e\xa3\x1a0\x8e\xa5\xae\xdc\xf4wS\x8f1\xd6\xb9\xffV\xcc'
 'T9\x0cyS\xe1^-\x0c)\x82\x03\xc8\xbbO\xceWB\x9e]\xb1'
 '\x88\xe6\x92\xbek\xdcR\xc9\xd6v\xa4i\xcd\xbd5n\x15\x0b\x89\x19~'
 "7\xd8\x13\xe3hk'\xe5(\x9c\xae\xa2:\t\\\xf38\x04\xc7\xb2\x98"
 'T\xba\xac\x1d#-\x8daG\x01\xd4l\xe8#\xf8P\x9c\x03\xa84C'
 '\xfd\xb0:\x8e\xc1\xa4 V\x87\xba(\x94\x96U\xea\xf8\xbe]Way'
 '\x07\xa1\x92I=\x13\x9e\x087\x83\x00B\xa9\x01\xb6\xe2\xb4wx\x01\x1a'
 '\xc8\xdc\x1d\xfd\xc5\x8bzZi\x19\x9cfM\xd2\xd2\xc6\xc2\xa3\xc0$W'
 '\xc2\xd2N\xd2\xbb)e\xa1\x8bF\x07\xf6\n\xdd\x94\xd6I\xb3\x07\xabW'
 '\xe4R||\xee\x9fK\x97hv\x08nMor40\x93\x9ew\xd9'
 '\xd11\xab)\x19t\xad\xabTut\x10\xfe=\xf7\xfa\x9e.\x00\xb9h'
 '\x8f>\x06|LTT\x89%\xccv\xb7.V\xa0Z\xf26\xfc\xa6\xd4'
 '\xab\xff\xe1\xd1\xba\xdd\x9cF1\n\xb1\xe7i\xc2u\xfbW`\xdc\x8d\xc2'
 '\xf5\x1e\xb4\xc1\x0f8}\x16*\xd7FY\xc5c%\x03g\xcc8\xf3\x81'
 '\x1e7\xa7\xe1\x12\xec\xec\xfd\xbc\xb4p\xc97V\xe8\xf8^\x89\xb1\xd8\xc6'
 '\xc1\x96Xh\xcc\x10\xf8\xcf%7\xba,\x8c\t\x01\x9c\xf5\xdbN\xe4\xdb'
 '\x7fe\xeb\x0f\xdb\x84y\x92.\x8d3\xf7\xc4\x8d\xae\x99\x17\x96:\x07D'
 'b\x08\xb5:C\xebc\xf0\x9bJ\x12\x84\\%\xadK\xbc\xc6I\x19,'
 '{F^=Nll\x87WA\xb2\x05\x9ei}\xa5k\xcc\xb7\tr'
 '\x88\xce\x9eo\x00+\x18\x00\xd8u\xc3\xb4\xa3\xc9=m\xad\x85\x1f\xe7\x08'
 '\xcaL\xb1\xf1\xee\xe9F\xb1\xa2\xec\x9e\xb7\xb9\xd7\xddx\xe5\x0f\xef\x0f\x9f'
 'lve\xca\x08sW\xe1\x88y)^\xf5xDD\xb154\xe8\xb3'
 '\x979\xb5C\x12W\xa3p\x89j\x0b\xc9\x03v\xdc\xcdTKF\x9c\xf2'
 '[L\xd6}\x9a?\xee\xee\xea\xb0BB.\x86\xbb\x00\xcdZ\x91\x97g'
 'E\xcd\xa3\xe5k\t\x92l\x99\xff\xf6\xc5\x17zL\xef4\xda\xc3@\xe5'
 '\xeb\xf1\xf9\xe63`\xbd\x91\xdf\xf5\xd1o,\xc5\x9f\xfc\x96\xf6\xaa\x00D'
 '\x8cj\x1c\x0e\x06A\xee\x89\xb7\xb5Y{\xefJ\x11\xd7J#\xd9\x84\xbd'
 '\xf9N\x9a>\x0c\x87\xe3\xf6\xd3Rcy\x84P5+\xdaa\x11\x1do'
 '\x9b\xdb\xda\x95\xd5}\x9e\x8aI\x0bC\x01\xc1\x06\x00\xb4Y\x02\x94/\xef'
 'd\xb6){Z~;\x9f\x0e\xf3\xb1\xdd>\xfe\xb1\xcd\xcb\xabT(\xb9'
 ' \xc6\xdf\xbb\x03\xe7\xf6\xba\xe8b\xac\xf5\xe3bA\xbb\x89\xc9\x9e\x906'
 '\xc1h\xa9\x0f\x94\x11\x8e\xaee\xf1\xac\x83rP\xce2\xc0i\x8f\xa35'
 '\xfb%tE(/\x19\xdc\x9c\xea\x07GK\x8d\x8bJ\xc7\xc3\xda\x0b\x18'
 'Bm\x14p\x00*\x0b\x9e\xd1|X\xfe\xd2;P2\xaa\x9aI\xca\x9e'
 '\xe5\xcaj[ }p\xb5b\xaf\xf8o!x\xd5\xbf\xabm\xcd\xe5\xc5'
 '\x97\x9a\x11w\xc0\xb9^\xc1\x98\x9f(o\x91\x83j\xd2\r\xd2\x04\xef\xbe'
 "\xfbU\x7f'\xe7\x97^\x98\x9b\xce\xd4\x92\xca\xb3\x1b\xaa\x8b\xaai\x97>"
 '\x7f?%\x95\x12(l\xcab\xa94W\xc2\x8b>6\xdbE\x03\xb1S'
 '\xad\x1a\xd4\t\xb9\x9e\x81\x17]aK\xda}E\xe4\r\x18\t\x1d\x04\xc3'
 '\xff\x1e)\xd6\xbd\xd2\x1f_\x83N\xf3\x05\xd2\xfc\xa6\xa7\ro\x12.['
 '[\x1a\xdaD\xbf1z\xdf\xf2\xfe\xef\x97;`\x8d3\x02\xdb\xbb\x98N'
 '\xb8f\xf4x\x12y\xd1\x9al\xb2Mu\x9aR\r\xfd\x13\xcb\x86?\xcb'
 'k\x7f\xf49\xd1\xb69\x1c{\xee$\xc5|\xe1zq\xb2\xe6R\xdd\xa4'
 '\xf77\x81e\xa7:p.\x91\xc2\x0e%\x91\x100\xeb\xb8\xf4\xb4A\xe5'
 'R\x9a\xb1QB\xfa\x1a\xde\xd9\x02\x04\xe1\x84\x8bk\xcd\x9f\xc8U\xfc\x86'
 '\xac\xd0"\x012\xda\xd6)`S\x8a\xbf\x14\xa6`\xf3\x9d\x8a\x1dyI'
 '\xc9n$\xb5\xbf\xd82\xcf\x18\xcal\x8c3!A\xd3\x84(0\xfe\\'
 '\xbd0\x8c[X\xc0s\x13\xc94$\xbcN\xdb\xb9\xc9vfX\xfd\xfd'
 '\xad,\x02uj\x0bx\xb7\x8aKO\xcb\xc6\x01\x04\xf8\xbb\x13\x11{\xf5'
 '\xfep&\xe7\xb5z\x84}\x88\x1a(\x8co\x8ag\xff\xd0`\xefV\xb1'
 '\xb5\x0eA\x98\xe2\x94-\xb7\xf8A"\x98\xcb\x0e\x8dd\xc0\x80\rB\xfa'
 '\x9b\xc0w\x87\xa7\x7f\x0ec\x95\xe2\xf3&\x7f\xdb u{\xb0\xef\xf7\xdf'
 "L\x05'5\x0b%\xe0\xa1\xcb\xd1s\xba\x9e<\xebi\x8d\xd4\x02\x87\xb9"
 '\xd1\x82.J\xe3\x16\n\x0f\x90\xc0\x92&WY\xd2\t\xffpT\xa7\t'
 '!U|\x9bP\xfa\x8f\x16\xdb\xdf\xab_\xb4c\xfe4\xb9.\xb6\xe1\x0f'
 '\n\xb6\x1e\xcb\xfa:\x85)\x82p%\xaa\xefJ\x8a3\xde\xbc\rQ\xf5'
 '\x9b\xad!2\x88e\x84\x97\xed7\x00\x90]\xcftrT\xa1\x7fW\xa4'
 'q\x8eC\x1aO|\x83D\x95\xb4\xa0H)\xd0)P\xcf\xb3\xb8\xd2\x9d'
 '\x1ePX\xac\xde\xc5\xfb\x16\xc5\xdaN1.*\xef\xf0\x95\xba\x9b^\xa5'
 '\x9b\xe9\x10\x95\x08\xf1\x83\x91*y\x81\xaf\xf8\xd4\xa3\x96\xaa\xd5/\xbd\xac'
 '\xe1\x9eZ\\\x19"\t\x84f\x12\x84\x1b\xc5\x8f\x98\x9d\xbcH\x1c\x08\xb0'
 '\xd7v\xa7\\\xb5xII\xfc\xefb\xa4\xb2\x1bX\xe8L\xc0\xd3\xf3\x8b'
 'g\xf76\xd8t\xd3uv@\xa2e\x19\x93\x1c:\xf3\xe2\xdd\xca\xa7\x15'
 "k\xc2\x1d\xe6\x07\xefC\xbc\xa8t\xc4\xb6\xb7\x9a\xdc\xef'\xb4\xda\x97\x80"
 '\xfc\xd10\xaa\xfe\xe9\xdc\x12\x85\xd6\xc8\xd4\xcf\x1b\x0f5\xcb\xf9\x14R\xdb'
 '\xde\xdaF)\x8am\x9c\xdf\xb4\xd7\x06\xb7\xd8s\x01\x0b\xae\xb33<o'
 '\x17\xd3 \xa2=\xe9\xb8\n\xe4Y\xe4\x9cD3\x9d\xc7\xf6I\xf0(\xf2'
 "x\x07\x01\x14\xce\xd4=\xd4\x0b4\x1d'\xc7\x9f\xff0d\xef\xe60y"
 '\xf3\x1b_\xbaD\xc3\xda\x81\x18~\xca\r&]I\x94\xdd!\xe0\xb60'
 '\xedRZ\xfa\xc2\xc6\x94\x8dz\\\x9b\xf6\xd3\x80\x05Z\xac\xf5\xc21\xe3'
 "\x1a'Qp\x89\x81;\xca\x95\x948~H26;\xaa$\x86\xd2\xa2"
 '%gD\xd5%\xa0\x95\x880\xec)\xfc\xd5S\xc6\xdf\x1a\xf6\x12\xc7\xc3'
 '"\x18\xfd\xc9\x7f\xe3\x07\x9e\xab\xda\x18\xf4\xf4\xeb\xed\x06\x01\xa2M\x04\x88'
 '.\x9eYZ\xe3\x9a-\xfe\x8a\x9c\x87\x08\x19-\x14\x8d`B\xba8\x8d'
 '\xcf"\\\xdaN\xdci\x14\x13\xa6_\xb5\xc7\x97\x9b\xd4\xff0:/\xa2'
 'u=\x06D\t\x903r/A\x99\x8a\x9e\xbc\x8e;\xbcT5\xd7\x9f'
 '\xd5\xb8\xcf<9NF\xbe\x0b\xe6cAR-\xa0|\xea9ov3'
 '\xf6\xbd\xba\x0e\xa0F8.\xa6\x06P@\xea\xa3Oc\xe7\xe5jDH'
 '\x90\x01J\xb5a\n\x9f\x1a1Syr\xe9N\xa7\xf6\xf0o\xda\x97\x0e'
 '\xb7\xde\xa7\x02\xef\xa3\x90\x8e\x94\xbe\xffDe\x80\x0bN\x93\x8a!4\xd0'
 '\xe7v($\xba-\xef\x80\x11\x0e$\x12\xcd\x93\x08G:\xe0\xd5\x98/'
 '\xfe\xd6V\xe6\xa54\x8ey\x19_\xe3\xc5\xc80a\td~v>\x8a'
 '\xb0\xe0\xc2\x12\xad/\x9b\xc8\xfd\xe9\x13\xd8\xbe;7\xda\x82}\x81\x81j'
 "K\xca\xb3N\x88'l\x8f+\r\xc8\x051\x7far\x8c9\xcfBE"
 '\x99\x14\x85wMr\xb2\x14\x90\xf6\x93X\n\xfc>\t$\xafEh\xf7'
 '\x9f\x86\x1b\xab\x83\xc0\xe9\xfclxX\x8f\x9f\xea2\x97\xf3\n\x96h\xbd'
 '\xad\x19\xb3\xee\xec\x11\x17]*$SC>!\x8c\xd5\xb3\x19\xa5\xach'
 '\xa4%aB\x140"\xa3\x86\xe8\xdf!"e>\xbaT#\x81\xedW'
 'T\xb5\xe5\x92L\x04\xf3\xd1I\xa3\xc7"\xeb\'\x97\xb2\x0f\x85\xf6S\xee'
 '\xea=\xa0M\xc7\xdbV\x9f\x94LxAU~\xc5\xd0\x95|x\xabb'
 '^\x82#\xd6\xe0\x1b\xa3\xfa\x0c$Z\xe4\x07\xd2\xb4\xa4\xe4\x84\xa8\xb5\xec'
 'W\x8b&\x08\xd0\xc2\xaf\x8a\x1c\x90\x04\xf0f\xdd8\xb9<w\xc5\xac\xc4'
 "\xe1\xd9JK\xdf\xce\x8dx\xae\x83\x95'\xfd\xe0\xdb\xe4\x07V\xfd\x12\x1e"
 "SP)\xf6\xe2h\xa4D\xe3\xbc\x05\x99iq'\x0b\n\x8f\x00o{"
 '\x1b\x9dNr\x8f.\xde\xb3\xaa\xb0&\x13\x14\xbe\xfc\xefS\x8a\xb9B\x10'
 'l\x026:\xfbN\xf7\xe7\xa3\x0b\x18\xb8\x8a\x82\xb9\x86e\xf4\xed\xe1\xd7'
 '\xec\x82\x9aM\x1b}\x97\xf5\x8d\xeb\xfe\xbf\x9c\\4\xeb\xe8(\n`\xa3'
 '\x1a\x8a\r\x8c\xa0\xc2M\xf1T\xe1\x8d\xb2\xdc\x9cOO\xc5\xd29\xa5b'
 '\xc7\x12\x9e\xd1=\xa07\x1d\xdd\x0fD\xe8\xbf\xb2\xf4\x9b\xda\xa8\xb4\x9d\xe9'
 '\xf2\xdf\xe0\xefw\x10~\xacC\xc3\xdb\xa9\xa0F!"A\xa4\xf7"\xa3'
 '6*C\xbc|\x8b\x91\xa1\xcc+\xeax;C\xd9\xa5\xcb\x90\x04`?'
 '\x86\x8aU\xe8B~\xcd\tE\x12q\xd91-x\xa5n\x8c5B\x8e'
 'Z\x1a\x02\x8d\x0f\xe0\x1a^\x1f\xbdu\xd6\xf6\xf3\xe1]\x90\xe3A5\x98'
 'T\xed\xf1\x85\xeb\x82\xfa\xa4\xf5\xa3\xa0\xd63H{\xcfQF\xdd\x90\xf1'
 '\x1bi\xfcW\x00\xc1\xe5\x83t\x93\xf2\xd3\xdc77\x9f|\rH\r|'
 '\xad\x10)?\xd0\x86\xd9y\xb5m^\x14$}y;{\xaf\xc2\x81_'
 '\x97x\xbd\xb3\xe6+\x9c\x91\xbd\xd7U!\xcd\xecQ-\xfeiZ#i'
 ')\x98\xa2\x9e\x88\x8d\xe1\xed9\xae\xec\xbdk\xa8\xbeo=O\xe4E\xb6'
 '\x98)[\x8c\x02\xf1a\x14\xbc\xacP\xeex\x8a\xff\t\xa9\xcb\x183\xdf'
 'G\xca\x1d\xa7k\xebr)\x17\xb6\x01\xecG6d\x00\xa8\xc2\xcbD\x88'
 'K\xf0\xa3s\x950\xf9\xb614\xba\xcd\x01~\xec\x9d\x99\xff\xd4\x14\x7f'
 '\xa3/m[\x95\xa2\x0f\xef\x12\x11F\x0c\x05w\x8e\xfa\x86\x85\xf5w\x8b'
 '\x0b_<[dO^\xbe\x8b\x070d\xfc~L>\xb9\x91\xf6\xc2\xf6'
 '\x9a+\t\x18\x19\xad\x80\x0fH\x89\x8e_g\xba\x8c\x91/\x01G\x17\x19'
 'G(\x10\x03\xe1\x1c\xc2\x00\x00\xffv\xeb?\n\xc1t\xf9\xae\x9f\x90\x15'
 '\x86#\xa7jsK\xa0G\x02\x99\xea\xea\xdc(\xcb1gP\x9cI\xca'
 't\xc3\\u\xa7\xc36\x84\x8b\xd2RZ\xea\xf26\xe5\x94+\xb2\xcc\x92'
 '/\xcbW\xcd\x91\xf0\xe0EH\xd42\x86H\xa4\x0c\xd2\x86\x1f\r] '
 '\xbbT_B\x1bX\x07I\xdcS\x05\x9d]\xb4y*\x91+\xc5\xc8M'
 '$\xe3\xb5\x07\xb4\xbd\xe4\xc0r\xeb\xb2\xfb\xce\xdc\x11\xb5\xbdf\xe2\x04\x8a'
 '\xe1\xdbm\xec\x81\x05(\xc0\xf0\xeb\x8893\xacp&Hdx8\xa6'
 '\xb0\xf6X#H\x15C\xdb\xcbi\xacY\x02;\x13)\x0e+\x8c,\xf3'
 'b_N\x9e\xdc\x98\xf6\xdc\x91\xfa\x0fc\xf7]W\xd06F\xf7\xd1\x17'
 "{j\x80\\4\x85\xa2C\xcf\x89\xc7\xc1\xad)vs\xdb\x85'\xfcs"
 '\x9d\xef\xb7\xefo\x10\x97\x1dq\xf08 $\xee\x04\xc8w\xdd\x8ab5'
 '|\xd5\xb2\xbd\xac3\x94\xb1\xc2@;\xe5EF\xe7E8\xc1\x8d\xb0R'
 '\xb5~`\x1d\x8e\xe3\xa9\xa7w;\r\xa9l\x0cM\xc3\t0\xb9\x98\x1d'
 'CD\xf8aG\x05+D\xc4hS\xf6\x96?,k\x1d4\x88\xa6\n'
 'a\xd1\xb1A:i\x9b\r\xdb\x19\xe5*6\x06B\xa8\\\xb3]\xc0\xa8'
 '&G\x84j\xcc\xa7\x9b]n\xb3Sg\x0eF\xef\xb9Zq\xdf\xc1\xb1'
 '\x11\xe1\xbf\xe9h<\x96c.\xde\x04Y\xde\x8b\xe8\xb6ip\x15Jd'
 '\xa3\xae\x8d@4L\x1d\xe7%\xcd\xa3\xad\xa7gt\xaebq\xd4\x8e\x86'
 '\x12\x1c\x12\x14\xbdN\x08\xe6C\x94\xb5r\x9c(\xd9\nm\xb22x\xd9'
 '\xf7,\xed\xcb54M?\x9c\x1cQ\xa5b\xd3\xb9}\x15\x8d\xc2\x19\xa8'
 '\x90!&\x7fn\x82\x8bs\xdc(\xd9\xa4EL\xa9B\xcb\xb7q\xe7+'
 '\x85U\xda\x1d\xaa\n\x813\x9b\xc3}w\xd3\xea\xed\xfd]\x8c\x03 I'
 "\xf4\xab\xbf\x9c'\xb4\x83\x9a\x05\x9f\x1c\x9d\xd3\x80*&\xa3j\xbd1\x8f"
 'sO{\xf1\xf0\xa1\x0cG\xd8\xc3\xb2E\xa4\x8e:\x93&\xce\xcd\xbei'
 'Y\xacF\x84#\x07r\x1c\x19\x14\x08Y\x15T\x03\x92\xb4\x1b5\xe0\x88'
 'I\xd7\x89\x0b^\xa6\xeb\x0f\xd99/\x0e\xc8,q\xc0\xde,#~\x9c'
 '\x89E\xe3\x85\x13\x05\xc8\x02\x9d\x96\xb2\x19\xe7\xe8\xee\xee\x90\x18\x11(\xa6'
 '\x15\xbc\x08|\xd1\xed\x03\xadK\x1f\xcfA\xa5\x9f\xa5Z3f\xfeN\xe5'
 '\x14\xf8\xd9h\xb5\xe9\xcd\x9e\x9c\xe0\x1b\x96\x12\xa8b;_\x0b]Y\x92'
 '*\xcc\xc1\x7f\x0f\xed\x94w\xd1\x8a\x145z\x1dp\x8a\x95\xfb~\x93-'
 'j\x94{\xa1xR\x1b3\xd5\xb4ct5f\xe6\x8d\xb7\xdb\xf5\xb3\x9c'
 '\xb0\x95I\xf3\xeca\x9fh\x98j\x83{\xf9|\xf3\x07U\xe3\xad\x08m'
 "T4\x15\xae5'\xe1\xd6\x0ek+\xdb\xbe?\xa9|I:\x86\xe0\xb1"
 '\xdbF\x89\xb4\xb9\xf8\x94A\x85\xdb\xb8\xb1\xa9\x8f\xcd\xbd\xf2\x7f\x05\t9'
 "\x98:\xba\xe2'\xf6:\xdb\x9f_}\xbc\rn\x94\x1d\xa0>S\xa0\xee"
 'ER\xbd\x16\x11X\x8e\x9cWZn +G.\xf6a\x9d\xd3E9'
 '\xa7z\xaag\xb9T\xf8\xccD\xb3\xea\xbeK\xc5\x1f\xdbn\x0b)Nj'
 '`\xe0X3\x8a\xe0C\x9ds_\x0e\xd5\x13\x98R\x15w\xce]\xf5\x94'
 '\x92\x9e\x93\xc1\xc1<\x81\x1c\xd4\xba\x17\xda)\xdf\x85\x99?\x85\xea[\xa0'
 'p\xe5\xdb\x85k\xbb/EQ\x8e\xd62\xe6\xa6\r\xf1\xd1\xd6\xdd\xcdF'
 '\xb7c\xcbi(|\x91\xd2\x04\xe0\xe07\xf2\x14,}p\xd9q\xefB'
 'w\x97\x14U\xa00\x89#=\xc1h\xd1\xb4Y`\x1d-\x90o\x1f\xcd'
 '\xc0\x8f\xf87\x9a\x1b\xdc\xeePo\xe9\xfdYX#\x18\xa6\x01\xe5\xb8\xe3'
 '\xff\xfa(\x1e\x19\xcf?Is\xa1\x97\x87_\xc4]Zq\xb3_\xcf\x96'
 '\xac\xf3j"\xd28r\x034\x08\x88\xe0\x84\xc0\xac\xe7Z\xbd\x07\xc7\xbf'
 '<\x16\xbf\x00WdPW\x8d\xe6\xab\xa9\x87%\xc94\x15\xa7|f\xd0'
 't\x94\xd6\xcc\x88u\x8b|p\xcf\xec\x9f\xa6\xd46\xda\x91J\xa1\xe0\x9a'
 '\xc7n\xc6\xe8\xefvX\xcb\xd0;\xd2w\xca\xbe\x0e\x1e\xc1\x8d\x814q'
 '4\x15&M\x83W\xa0\xe9\xb4\xa0\x8a,\xbc\x12M\xc31\xa5\xe42\xe5'
 '\xdeX\xce\x0b\x84Y\x90\xbd\xcc\xfc\xcaF\xa04\xb8\xfd\xe8\xde>O\xb4'
 "?\x7f\xc5't\t\xa0&;\x19\x1d\x02\x07\x92lU\xc3\xa8\xa5\x99\xb6"
 "}A\xb9\xe7\xdah'\x19Oa\x8a\xce\x05\xc6\xd4\xa9'yg8\xc7"
 '\x12\xde\xd3\xc2M\xf3\xdc\xb1K\rn\x08-\xfa\xc3\x82B\x82\xc3\xc6\xdd'
 'P&|\xea\x1b\xcdv\xa0S\x1djS\xe2\xc42\xf5\x9a>\xac\n\x89'
 '\xac\x84\xd5\xb6\x95\xef\x10\x11\xee\x9f\xabN\xe0J\xca\xa0\xd7}r\x1e\xc4'
 '\xbe\xa0`\xa3)Ti\x07u\x0cx\x1f\x92\xa6\x81\xa5\x8aG\x83\xe9\xd2'
 '4\x15\xde\x9e\x1e\x88\xf1\x9a\x84\xef\xd4\x00\x9c\xbc\xfe\xd4\xca\rD0\x85'
 'ap0\x17SHv\x11h2>\xe8\xc1{?\xce\xfbEl4H'
 '\x02\xbb(\xdf\x06z>\x8f\x88\xa0S \xa6\x14\xd3\xe6l=d\xb09'
 'e\xfc\xd1\x95\xbcL\x02U*\r\x1e\xc3\xc9qu\x82\xda\xfbe\xab\x13'
 '\xf2\xbc\xd6\xf3\x12\x80|ef\xdeUX@\x83b\x00n=\x18\xb7\x93'
 "'x}\x1d0^|BYR\xf9\xe3<\xb5\xe7$\xd80-\xef\x8c"
 '\xc8>\x03\xa2\x07\\\x0b\xb4q\xbf\xf5\xc8\xb7\xc0\x922C\x97\xbf{\xfb'
 'uAG\xd2\xf2o\xd4\xe68#\x03\x81E\xd8\xe5}\xe5\xb5h\xe5N'
 '\xe9\xfb\x07\xe2\xcb\xbb\x14\x16\xd5rirD\x9a\n\x16\xac\xde\x06R\x1d'
 '\xa0v\xcb\x9b\x1eE{\xb4LL\x8a0\xa1\x08\x80z\x00\x8f9\x80Y'
 '\xb1\xfa\x0c\'\x009\x07\x00\x10<\x05\x84\xc8"!S@\'\xd7a\x16'
 "d\xc8A'\xc4\x01'\xea\xeb\xef\xb4St\xf0~\x0c\xcc\x1c\x19*."
 '\x13\xaa\x8d\xc96aC\xa5&s\xb4\xfcB\rHp\x9e\xe2R8\xe7'
 '%S}\xe9\xd5_x8\tn\xc0\tU\xfc\x97w\xd8\xbe\xf0S\xaf'
 '\xc3\xcd\xddN_\x14M(\x8d\xa6\xeeD\xfd\xdd\xd9\x1a\xc4\xcck+y'
 '\xf5z^l\xe3}e\x91N\x81L[\x0e\x94\x02%0`\x07\x18y'
 'QN \x83\x7fa\xf8\xac<\t\x8a\x8f\x8d\x16M\x95\x95\x93\xf1\x92!'
 '@a\x97\xfb\xbf\x8d?\x84\x84\r\x05\xbd\x86\xf9\x05B0 I.H'
 '!\rt\xe8Y\xb8"\xd7\x9f(i,}\xa7o\xb5\xf1\x7f_@\xc4'
 '\x1e\x06H\x9c\x99\xef\xb2\x03\x82\xc8\xac\xac\x9c\x8bH\x90^\x12\xf9A\x93'
 '\xfe\x01u\xc5d\x8b\xc9\xc0\xdcLVM\xd6\xdfI\xfd\xc8\x91\xd6\xcfW'
 '\x80\x87\xe0\xd6s<5\x02\xe4\xb6^\xca?[5Z\xe7I\x97\xd2N'
 '9A\x0cv\xf2R\xba\x96\xfeM8h\xfez,\x87\xa1\xe1\xb5\xc2|'
 '\x16r\xd4\xd3\xf2\xf4\xe1\xe1\x06y\xc1I$\xcaz\x1fM[\x8b\xa6\xc9'
 '\xf6_\x8d(\x0cT|\xae<\x06Z\x8a\xa6\xed%\xfa\x18\x92|\xe2\x9f'
 'E\x1a\xd6\x80\xeb\xb4\n\xc5y\x05\x18V\x8e\x9e\xd2\x07)\xe6L\xc4]'
 '\x7fi\xdd\xa9o\x87\xa6\xbe\x1b\xfbK\xb4t\x99\xebGLw\xec\xaf\xdc'
 'U\xfft\xa8b\xb50J\x9c\x01\x92\xdc\x89\xa2\xe8\xfb\x1e\xa2@\xd1\x94'
 "\x08'\xd1\xa5=\xc7\xde+d\xbd\x97JXw\xb7Z\xcd\x83\x9f\xf0{"
 "\x14*\x08\xc7\x9dx}'Z~rU!\xe1\xbd\xef\xd6\xba\xb4{6"
 "*\xda\xf7\x9b\xe9\xf2\xf1v\x99{\x84'\x0f\xa5i^\xdfO\xd8\xd4\xd0"
 '\x0c8\x1f\xe2#\x17\x0c\xe8\x0by\x0bb\xcd\xcb\x9ejo\xa5[\xd4)'
 '\x0fr\xea\x81\xefB\r\xc8\rL\x1a\xad\x11\t\xde\x87\x01\xab\x10!\x83'
 '\xdfOT\xff\x03\xeb\xe0\xb3\xfd\xfeF6\x01mn\xb1k\xa6\x8f\xba\xff'
 '\x07\xdbd<\x15Kl\x97z\xff\xfa\xbc\x88\x9c\xa2\xe4\xa2\xf9\x8f5\xca'
 '\xdd\xb7\x96Y \xb9\xb6\x9c\x03\xd1q\x07qQ\x07\xe8\x9f\x06\x94rP'
 '\xb8%T\xdbj"\'\xd4\xb7\x14\xec\xc1z\x97\xf7/N\xaa*\xda\xcf'
 "\x01\x14\xcb\xcc\xb3s\x82I\x01`}~\x98\x14'\xfa\xd8\xabO\xbe["
 '\x9f\xee\x86\x84\xfa\xfb)\xc8\xb1\x8e\xc6|l\xefm\t\xf2t{\x12\xdc'
 'J\xc3#\xa3r\x83\x17\x99\x1a\x1b\x8d\x03\x81u\xcf\xfc\x03?\x1f\xd7\xe8'
 '\xd6\x0c\xb5\\\xc4!!\xc3W>\xbf\x10\xa5\xe1\x88\xd9*m \xad\x01'
 '\xd0\xab\x1bTA\xb6\xc8\xe79\x93\xcfB\x84\xcf\xdd\xcbj\xa6\xfa\xee\xb1'
 '\xb5\xa5\n{_l\n\xc7\xb5\xd1o\xa4\xb5v\xd9\x98\xbc;\xff\x0ct'
 '(\x85&\xcf\x85D\xe0 \r\xd7)\xd6X(\x1a\x7f\xa28e\xb3D'
 '\x1f\x81f\xc2\xd1N_\\\xb6>\xd1\xab\xa2\xd1NP\xb7\xf5\x0f\x97\xea'
 '\x01PKb=_\xe8\xa0_\xbe*7\xe7D\x1bp\xe1C\xdc\x91\xaa'
 '\xe8#m\xf4\xac>\x97\x18\x94_\x7f_x\xdf\xdd\x95\xdb\xb9\x81\xcbU'
 '\xf1\xc3"\x90e\xab\x8d\x95<\xb0&C\xf7\xf8\xd8QJ\x9f\x8c\xdaD'
 '\x82j\x1b\x08#\xb6\x8d\xd1\xa4\xbdl\xa5\xca\xae\x87\xf7\xb6R\x1f*\x82'
 '\x11\xb7\xe3\x9bd\xc0\xea8\x1a:\xea\xc6\xa0\xdd\x96\xe1\xd1\x04\x05y\xaf'
 '\xef\xef\x8b4\xf6\xcc\xc1q\xd4\xe9\xca5\x1b\x87O\xb2d\xb0\x16\x0e\xfc'
 '\xeb\npH\x0b\x12\xc1{#g\x92\xe7\xf3\x83\x16\x8e\x83\x1c\xf1CT'
 '\xe7\xc5\xf8\x06Cp\x8b\xb9Z\x04h\x0c\x81\x9aD_\nw\x8f\xaa\xc3'
 "\xc5\xee\xb6\x06\n\x8cn'^A\xa2|\x92\xb3\xed\x18\xf0o\xa5'\x0b"
 '\x9eA\xc1\x87]D\x0cb\x94\x94\xe7\xa6+A\x96!\xfc\xbd\xb2I\xff'
 '[\xf3{\xe2\xb5\xe4\xcf\xb7\xb1]\x8bN:\x05\x15\xfd\xe1\x96\xee\x9f\xfe'
 '\x17\x88\x02\x9bj\xe5\x10\x01\x01NM\xbf9}X\xf6\x8c\xf5=*\xfa'
 '\xf52u\x9f\xf7Z\x7fR\xef\xfb\xa2\xe7\x98\xb9)\xf59\xe5\xea-\x8b'
 '\x10\xbeX\xd4\xf6@\xe52Y\x03\x81a\x91\x0e\x12m\x0c\xef&\x07%'
 "\xc6\xa0'\xbf\xee\xcf\x8a\xbd\x14\xf9\xe1i\x15YV\xf9\xc7\x0b\x99x\xe6"
 '\xb1\x05\x03\x16paK\xf9\xa1!\xf5\xfd\xe0i\xcb\xd7\xee?\xdc\xbeg'
 '\xfd[sJ\xfd\xe6\xe4\xb8=\x05\xee\xbb\x18P\x12-\xf3\xee.\xf7t'
 '\xbaR\xea\xa9\x9b\xdfh\xffmT\x85-\x9b\xf7\xff8)X\x9b\xea\xe8'
 '\x96\x92\xf68z5\xd5\xf2\xc1\x86\xe72\xa5\xe4\xfb\xf6t\xdf[\xcbc'
 '\xdb\xc7<b\x97\xeb\x03w\x9f\x15\\\xc5\xa1\xae\xb0\x12\x8d\x0f\xa7\x18\x8a'
 '\xa2Vo\x04\n\xf9BF\xae\xbf\x16`|\xc1\xbfN$5\x1f\xcb\x1e'
 '\x90N\xbbJ\xc8\xf7\xe6\x90\xecM\xa9\x9aJ\x923\x0e\x14\x15\xef\xad\xe7'
 '\xec\x9fSn\xdfOUG\xd1\xd0}\x99\xf0O\xb2]U]\xa5A\x0f'
 '>\xc7r\x14\xfb\x8e\xa3Z\xb7\xe6SOi\x9aJM\xac\x11\xaf\xfd\xac'
 '\xf7v\xady\xf1\x08\xf3}\xbb\xc7\x84j\xf9\x83\xbfc\xbfQ|5\xd0'
 '\xe8\xf6\xb2P~ZsB\xd2R\xd5\xae\xec\x83\xc0\xdf\xef\xe3\xe5\xf0\xdb'
 '\x8e_vo<\xd8\x92\xdf9\xed\x8b\xd8\xd2\x08N;|\xd2\x03>x'
 '\xe2@r\xc9sN\xacxI\xd0M\xf8\xd1\x7f\xb3k\xf7\x8e\xba6i'
 '\xbe\x08\xfe\xee3b\xf0\xa2\xe4\xbb\x1ff\xd6\xbdA\xf9O\xa0\xa4\x97B'
 '\xc5\x0f\xa5k+\xc9\xbe\x19}\xc7\x92v\xbe\x7f\xeep\x8c\xdd\x85m\xbf'
 '\xfc\x10\xffP\xc0\xdfi9^\xa0\xfc\xed\xc6y\x90s\xea\xcf\x8f\xa2\x7f'
 "cone)gr\xf2\x93\x87J\x16\xf7t\xbfo8\xfc'd\xe1"
 'w\xc8\xec6\xf3^\x92\x02\xc2k\xff{\xc5\x91\xf3\x7f\xf9\xef2\x05c'
 '_\xfe^\xf6J\x88q\xfc\xb5~\xe3\x87\x95o\\\xf7Z\x86\xa4\xe0\xcf'
 '-\xfd\x7f\x8e\xbeYW^\xfe\xa8:h\xfa\xf1\xa0\xa9\xe4\xdfm\\\xd4'
 '\x99c\x89\xfc\x95\xd2g}W\x7f.W\x9fS\xfcy.f\xe8/_'
 '\xf6\xfc\x7f\x1en\x15\x07\xfb\xaaT\xe7p\x1e\xbb\x94\xd6o\x197\xfe\xfd'
 '\xb8\xba\x95t\xe1\xdf\x8d\xc9\xf4\xb2YA\xe6\x83\xd4R\x18]F\xc4\t'
 '\x8b\t\x05?@\xcb\xa1\x8e\xafcB\x99\x13p(\xe8\xdf\xd1\xae\xe8m'
 '\xd5\xc9b\xb9\x83\xa76\xd7\xb7\xf7r\x18\xaa\x8e\xe5\xba1_#\x9c\xc1'
 'P0\x94\x80g\x12\xa8"h-"]\x85\x05zT\xa7\x17F\xf4c'
 '\x91 \xae\xb5\x86q\x93Z.O5\xb9`\x08\x1c\xc7\xe0|\xd5\x9e\xbf'
 '\xe6V=Yg\xc6b\nK\x1eP0\xa1w\x87\xb2\xed.\x86=('
 '\xd7\x8b\xfb\xa1\xbb\xd4\xab\xe1\xdbS\xb7{`=o\xc0\xb9\xda$w#'
 'E;\xa4\xd5\xdd\xbfC\xb8\xbd\xe7\xfaC\xb0a\xa2\xc9\xe2 !\xc6\xaf'
 '\xafP\xf6\x90a\xc2\xe6\xce\xf6\xd4\xbd\xa3\x9a?\xefh\xfdjw\x01G'
 '\xbe\x80\x97\nUh\x1f\xe14:V\xe8\xc7\xef~\x0b\xef?\xaa\xd3\x94'
 "\xf0y\xd7xs\xb1'\xea\xe9\x8d\xf8\xdf&[+C\xa9\xffm}\xfe"
 '\x9d\xfa\x85\x02X\xfc\x1f\x9f\xea\x88,')),
'/kweb.css': ('text/css', '''\
* {margin:0;}
html, body {height:100%;}
body {
 background-color:#FEFEFE;
 color:#333;
 text-align:center;
}
footer {background-color:#f0f0f0;}
.uptofooter {width:100%;}
.uptofooter {
 min-height: 100%;
 height: auto !important;
 height: 100%;
 margin: 0px 0px -3.8em 0px;
}
.content {
 font-family: "Open Sans", "Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;
 padding: 1em 1em 3.8em 1em;
 background-color:#FEFEFE;
 text-align:left;
 margin: auto;
 line-height: 1.8em;
}
h1, h2, h3, h4, h5, h6 {
 font-weight: 300;
 font-style: normal;
 line-height: 1.4em;
 margin-top: 1.2em;
}
.content > p,ul,ol,dl,h1,h2,h3,h4,h5,h6,pre,blockquote {
 padding-top: .5em;
 padding-bottom: .5em;
}
.content blockquote {
 background-color:#F0F0F0;
 margin:1em 2em;
 padding:1em;
 border-left: 4px solid #00709f;
 font-style: italic;
}
.content dl {
 margin-left: 1em;
 line-height: 150%;
}
.content dd {
 padding-left: .5em;
 border-left: 2px solid #DDD;
 margin-bottom: 1.1em;
}
.content pre {
 background-color: #DDD;
 font-family: Consolas, "Andale Mono", "Courier New", Courier, monospace;
 color: #444;
 padding:1em;
}
.content code {
 background-color: #DDD;
 font-family: Consolas, "Andale Mono", "Courier New", Courier, monospace;
 color: #444;
 text-indent: 0;
}
.content table {border-collapse: collapse;}
.content table th {background-color:#DDD; border:1px solid #DDD; padding:.2em;}
.content table td {vertical-align:top; border:1px solid #DDD; padding:.2em;}
.content table td.last {width:1px; white-space: nowrap;}

.topborder {height:.27em; background: #00709f;}

nav {
 width:100%;
 display:table;
 table-layout:fixed;
 background-color:#F0F0F0;
 margin-bottom:1em;
 margin-top:-1em;
}
nav ul {display:table-row;}
nav li {display:table-cell;display:inline-block;}
nav a {text-decoration:none; display:block; padding:.7em;}
nav li:hover, nav li a:hover, nav li a.active {background-color:#00709f; color:#fff;}

@media screen and (max-width:320px;) {
 nav li {display: block;}
}
.font-sans {font:1em/1.2em Arial, Helvetica, sans-serif;}
.push-right {text-align:right; float:right;}
''')
}
_KRESOURCES_DEFAULT = {
'/favicon.ico': ('application/octect-stream', zlib.decompress(
 'x\x9c\xb5\x93\xcdN\xdb@\x14\x85\x07\x95\x07\xc8\x8amYv\xc9#\xe4\x11x\x04\x96}'
 '\x8c\x88\x1dl\xa0\x9b\xb6A\xa2)\x0bVTB\xa9"\xa5?*I\x16\xad"\x84d\x84DE\x93'
 '\x14;v\xc01M\xe2$\x988\xb1l\x9d\xde;v\\\x03\x89TU\xea\xb5N\xe4\xb9\x9a\xef'
 '\x1c\xcfO\x84X\xa0\'\x95\x12\xf4\xbb,\x9e/\n\xb1$\x84xF\xa2\x16u\xc2>WzQ\xfc'
 '\xf7\xca\xad\xafo\x91T\xd2\x1ai\xe5\x1fx[\xf9\xf4\x01\xc57\xbb\xd8\xdf\xd8'
 '\x00\x8d\x11\xf9\x95\x12\xda\x9a\xc3\xae\xe5_\xbdDpk\x03\xc3\xaeT\xd0\xb3\xd0>?'
 '\x83Z\xfd\x86Z\xa5\x84\x1fG_\xa4\xe7\x1c^\xa9W\xbfJ\xfe\xb4\xf0\x0e^\xdb'
 '\x88}0 \xafA\x0f\xa3+c&O\xbd\xf4\xc1\xf6\xb6d\x9d\xc6\x05\xdcVSz\xb0x\x1c\x10'
 '\x0fo\x02\xc7\xd0\xe7\xf1%\xe5\xf3\xc78\xdb\xf9Y\x93\x1eI\x1f\xf8>\xfa\xb5'
 '\x8bG<\x8dW\x0f^\x84\xd9\xee\xb5~\x8f\xe1w\xaf{\x83\x80\xb2\xbd\xe1\x10\x83'
 '\x88\'\xa5\x12\xbcZ?9\x8e\xb3%\xd3\xeb`\xd4\xd2\xffdS\xb9\x96\x89!}W!\xfb\x9a'
 '\xf9t\xc4f\x8aos\x92\x9dtn\xe0\xe8Z\xcc\xc8=\xec\xf7d6\x97\xa3]\xc2Q\x1b(\xecd'
 '\x99_\x8dx\xd4\x15%\xce\x96\xf9\xbf\xacP\xd1:\xfc\xf1\x18\xbe\xeb\xe2\xaey'
 '\x89;]\xc5\xf1\xfb<\xf3\x99\xe9\x99\xefon\xa2\xdb6\xe5\x1c\xbb^\x8b}FV\x1b'
 '\x9es+\xb3\xbd\x81M\xeb\xd1\xe0^5\xf1\xbd|\xc4\xfca\xf2\xde\xf0w\x9cW\xabr.'
 '\xe7\xd9\x8dFx\x0e\xa6){\x93\x8e\x85\xf1\xb5\x81\x89\xd9\x82\xa1\x9c\xc8;\xf9'
 '\xe0\x0cV\xb8W\xdc\xdb\x83\xa9i\xb1O@g\xa6T*\xd3=O\xeaP\xcc(^\x17\xfb\xe4\xb3Y'
 '\xc9\xb1\x17{N\xf7\xfbo\x8b\xf7\x97\x94\xe3;\xcd\xff)\xd2\xf2\xacy\xa0\x9b'
 '\xd4g=\x11B\x8bT\x8e\x94Y\x08%\x12\xe2q\x99\xd4\x7f*\x84O\xfa\r\xb5\x916R')),
}
# ##################################################################################################
# GLOBAL CONSTANTS END
# ##################################################################################################

class _KRequest:
  '''
   kweb: An Asynchronous Python HTTP server/framework
 Author: Karthik Ayyar <karthik@houseofkodai.in>
 %s


URL resource path traversal
===========================
  http://<host:port>/path/path/path/..

  <hostdir> = <host:port>|<host> sub-directory in start-directory.
  if <hostdir> does not exist, then hostdir 0.0.0.0/ is used,
  if that does not exist start-directory is used.

  URL can be module/file/directory
  even if file/directory exists, if path/index module exists, that
    is invoked first.


kweb modules
============
  * python files with methods named as HTTP verbs (GET/POST/PUT...)

  * on HTTP each request, kweb loads the appropriate module and
    calls the requested method, passing a single REQUEST object

  * modules should be in the path of the host directory (hostdir)
    similar to files in the path of the host directory

  * accessed via. URLs http://hostname/path/path/path/..

  * four types of modules

    <path>/index.kweb
      * if module returns None,
        subsequent modules/files in urlpath are invoked
      * can act as a filtering mechanism for modules/files in urlpath

    <path>.kweb
      * must respond to request
        no further modules/files are served
      * if <parent-path>/index.kweb exists,
        it is invoked first before <path>.kweb
      * can utilize properties/methods of request object

    <hostname>.kweb
      * must respond to all requests for site named <host>
        no further modules/files are served
      * useful in deploying complete sites in a single module

    <catchall>.kweb
      * passed as command-line parameter in starting kweb
      * serves all requests
        no further modules/files are served

  * REQUEST properties/methods **have** __doc__ strings ;-)


hello.kweb
==========
def GET(REQUEST):
  return REQUEST.html('<h1>hello kweb</h1>')


REQUEST-properties
------------------
 args {'str':'str',}
 auth (username, password)
 clientaddr (ipaddress, portnumber)
 content None or tempfile.TemporaryFile()
 content_length 'int'
 headers {'str':[],}
 host 'str'
 hostdir 'str'
 line (method, request-URI, HTTP-Version)
 method 'str'
 modparts ('str',)
 moduledir 'str'
 pathparts ('str',)
 remoteip 'str'
 session
  .items {dict}
  .set(loginid, data=None, remoteip=None, timeout=1800)
    returns 'sessionid'
  .get(loginid, sid, remoteip=None, doLogout=False)
    returns (errmsg, data)
 url (scheme, netloc, path, params, query, fragment)
 urlpath 'str'
 version 'str'

REQUEST-methods
---------------
 addResponseHeader(line)
  None
 listdir(path='', sortby=0, fext=(), rtype=2)
  None, 'str', ()
 getheader(key, default='')
  'str'
 html(body='<p>arigato gozaimasu</p>', title='(-: kweb9 :-)', headend='', footer=None)
  'str'
 htmldir(sortby=-2, fext=())
  'str'
 htmlescape(s)
  'str'
 parse_formdata(fin, boundary, filedir=None, bufsize=4096, filemode=0)
  'err', ['part',]
 parse_header_value(line)
  'content-type', {options}
 parse_query(qs, result=[])
  [(name,value), (name,value),...]
 sendError(errcode=404, errreason=None, errmessage='')
  False
 sendFile(fname='')
  True/False
 sendRedirect(url='/')
  True
 sendResponse(content='', ctype='text/html', code=200, reason=None, clen=None, nocache=False)
  True
 setResponseHeader
  None
 setResponseType
  None

module properties
-----------------
 TIMEOUT = 5 seconds
 NOCACHE = False
 KEEPALIVE = False
 MAXBODYSIZE = 26214400 #25 MB
 PARSEBODY = True

common error-response-codes
---------------------------
 400 Bad request
 401 Unauthorized
 403 Forbidden
 404 Not Found
 408 Request Time-out
 411 Length Required
 413 Request Entity Too Large
 414 Request-URI Too Long
 415 Unsupported Media Type
 416 Requested Range Not Satisfiable
 500 Internal error
 501 Not Implemented
 503 Service temporarily overloaded
 505 HTTP Version not supported
'''
  def __init__(self, clientaddr, server, send):
    '''
    * private attributes start with "_"
    '''
    __builtin__.__import__ = self._import_hook
    #public attributes
    self.version = _KWEB_VERSION
    self.remoteip = clientaddr[0]
    self.clientaddr = clientaddr
    self.server = server
    self.line = None
    self.method = None
    self.url = None
    self.urlpath = None
    self.args = []
    self.headers = {}
    self.content_length = 0
    self.content = None #content size:content_lenth that starts after request header
    self.pathparts = ()
    self.modparts = ()
    self.host = 'localhost'
    self.hostdir = self.moduledir = server.requestdir
    self.auth = None
    self.session = None
    #per-module attributes
    self.KEEPALIVE = False
    self.TIMEOUT = server.timeout
    self.MAXBODYSIZE = 26214400 #25 MB #customizable per-host-basis
    self.PARSEBODY = True
    #private attributes
    self._send = send
    self._responsetype = None
    self._responseheaders = []
    self._hostmod = self._indexmod = self._pathmod = None
    self._modindex = 0
    self.HEAD = self.GET

  def _import_hook(self, name, *args, **kwds):
    '''
    import hook

    args:
      name: name of import module
      args: positional arguments
      kwds: keyword arguments

    returns:
      success
        module
      failure
        False

    notes:
      * import modules path-order moduledir/hostdir/requestdir/sys.path
    '''
    global _KBUILTIN_IMPORT
    if 'kweb' == name:
      return _KWEB
    try:
      return _KBUILTIN_IMPORT(name, *args, **kwds)
    except:
      pass
    modfname = os.path.join(self.moduledir, name+'.kweb')
    if not os.path.isfile(modfname):
      modfname = os.path.join(self.hostdir, name+'.kweb')
    if not os.path.isfile(modfname):
      modfname = os.path.join(self.server.requestdir, name+'.kweb')
    if not os.path.isfile(modfname):
      return self.sendError(500, 'import module "%s" does not exist'%name)
    (err, mod) = _kimport(modfname)
    if err is not None: return self.sendError(500, '_kimport exception', err)
    return mod

  def _parseHeader(self, hdr, hasbody):
    def _load_path_module_method(fname):
      (err, mod) = _kimport(fname)
      if err is not None: return (err, None)
      method = getattr(mod, self.method, None)
      #use GET method if HEAD is not available
      if (method is None) and ('HEAD' == self.method):
        method = getattr(mod, 'GET', None)
      #should actually send a 405 Method Not Allowed instead of 500
      #maybe needs to send error code in response ?!
      if not callable(method):
        return ('invalid %s in %s'%(self.method, fname), None)
      self.TIMEOUT = getattr(mod, 'TIMEOUT', self.TIMEOUT)
      if self.KEEPALIVE: #module override only if client is capable
        self.KEEPALIVE = getattr(mod, 'KEEPALIVE', self.KEEPALIVE)
      self.MAXBODYSIZE = getattr(mod, 'MAXBODYSIZE', self.MAXBODYSIZE)
      self.PARSEBODY = getattr(mod, 'PARSEBODY', self.PARSEBODY)
      return (None, method)

    if self.method is not None: return #should not get here

    #init attributes
    self.line = None
    self.method = None
    self.url = None
    self.urlpath = None
    self.args = []
    self.headers = {}
    self.content_length = 0
    self.content = None #content size:content_lenth
    self.pathparts = self.modparts = ()
    self.host = 'localhost'
    self.hostdir = self.moduledir = self.server.requestdir
    self.auth = None
    self.session = None
    self._responsetype = None
    self._responseheaders = []
    self._hostmod = self._indexmod = self._pathmod = None
    self._modindex = 0

    # REQUEST LINE
    i = hdr.find('\r\n')
    if i > 8190:
      return self.sendError(400, '_KRequest.requestline.8190 (%s)'%requestline[:20])
    requestline = hdr[:i]
    hdr = hdr[i+2:]
    self.line = requestline = tuple(requestline.split(' '))
    if len(requestline) != 3:
      return self.sendError(400, '_KRequest.requestline invalid\n%s'%requestline)
    self.method = requestline[0]
    # urlparse
    #  (0 scheme, 1 netloc, 2 path, 3 params, 4 query, 5 fragment)
    #  o.scheme, o.netloc, o.hostname, o.port, o.path, o.params, o.query, o.fragment, o.username, o.password
    #  scheme://netloc/path;parameters?query#fragment
    self.url = url = urlparse.urlparse(requestline[1])
    self.urlpath = urlpath = urllib.unquote(url[2]).replace('//', '/') # remove empty parts
    # END REQUEST LINE parsing

    if '/' != urlpath:
      self.pathparts = self.modparts = pathparts = ([p for p in urlpath.split('/') if p])
    else:
      pathparts = ()

    #http-headers are case-"in"sensitive - do getheader in lowercase
    self.headers = self._parse_header(hdr)

    clen = self.getheader('content-length')
    if clen:
      try: self.content_length = int(clen)
      except: return self.sendError(400, '_KRequest.Content-Length invalid\n%s'%clen)

      #
      # if PARSEBODY must have valid Content-Type
      # else module can do whatever it wants with body/content
      #
      if self.PARSEBODY:
        ctype = self.getheader('content-type')
        if ctype:
          ctlen = len(ctype)
          if (ctlen < 19):
            ctlen = 0
          elif ('multipart/form-data' <> ctype[:19]):
            if (ctlen < 33):
              ctlen = 0
            elif ('application/x-www-form-urlencoded' <> ctype[:33]):
              ctlen = 0
        else:
          ctype = 'PARSEBODY: no Content-Type header' #reuse variable for error
          ctlen = 0
        if (0 == ctlen):
          return self.sendError(403, '_KRequest.Content-Type unsupported\n%s'%ctype)

    # if entity-body - header must contain content-length
    if hasbody and (0 == self.content_length):
      return self.sendError(400, '_KRequest.Content-Length missing')

    self.KEEPALIVE = ('keep-alive' == self.getheader('connection').lower())

    # if we're running behind a proxy...set by forwarding proxy like lighttpd
    self.remoteip = self.getheader('x-forwarded-for', self.remoteip)

    host = self.getheader('x-forwarded-host')
    if not host:
      host = self.getheader('host')
      if not host:
        # http-version-parsing - if reqd., module can use REQUEST.line[2]
        # if needed to be done here, use requestline[2]
        # technically should error if version is 1.1 as Host is mandatory
        #   we're liberal ;-)
        host = url[1]#netloc
    self.host = host

    r = _KRESOURCES.get(urlpath)
    if r: return self.sendResponse(r[1], r[0])

    requestdir = self.server.requestdir
    hostdir = os.path.join(requestdir, host)
    if not os.path.isdir(hostdir):
      hostdir = os.path.join(requestdir, host.split(':')[0])
    if not os.path.isdir(hostdir):
      hostdir = os.path.join(requestdir, '0.0.0.0') #default-catchall host
      if not os.path.isdir(hostdir):
        hostdir = requestdir
    self.hostdir = self.moduledir = hostdir

    #
    #search/load-for-modules
    #  * close on error - minimize work upto errors
    #  * on-demand variables process/set-only-if-required by log/module-call
    #    auth/cookie/session
    #  * kall module-method only after request-read is complete
    #
    if self.server.catchall is not None:
      mod = self.server.catchall
      self._hostmod = getattr(mod, self.method, None)
      if not callable(self._hostmod):
        return self.sendError(410, 'invalid catchall %s'%urlpath)
      self.TIMEOUT = getattr(mod, 'TIMEOUT', self.TIMEOUT)
      if self.KEEPALIVE: #module override only if client is capable
        self.KEEPALIVE = getattr(mod, 'KEEPALIVE', self.KEEPALIVE)
      self.MAXBODYSIZE = getattr(mod, 'MAXBODYSIZE', self.MAXBODYSIZE)
      self.PARSEBODY = getattr(mod, 'PARSEBODY', self.PARSEBODY)
    else:
      #hostmod is requestdir/hostname.kweb not hostdir/index.kweb
      modfname = os.path.join(self.server.requestdir, host+'.kweb')
      if os.path.isfile(modfname):
        (err, self._hostmod) = _load_path_module_method(modfname)
        if err is not None: return self.sendError(500, 'host-module exception', err)
        modstat = os.stat(modfname)
      else:
        fqpath = hostdir + urlpath
        if os.path.isfile(fqpath):
          if '.kweb' == urlpath[-5:]:
            (err, self._pathmod) = _load_path_module_method(fqpath)
            if err is not None: return self.sendError(500, 'path-module exception', err)
            modstat = os.stat(fqpath)
            self.modparts = ()
            i = len(urlpath) - 5
            while (i > 0) and (urlpath[i] <> '/'): i -= 1
            self.moduledir = fqpath[:i+len(hostdir)]

        modfname = os.path.join(hostdir, 'index.kweb')
        if os.path.isfile(modfname):
          (err, self._indexmod) = _load_path_module_method(modfname)
          if err is not None: return self.sendError(500, 'host-index-module (%s) exception'%p, err)
          modstat = os.stat(modfname)
          self.modparts = pathparts
          self.moduledir = hostdir

        if ('/' != urlpath) and (self._pathmod is None):
          # find longest/rightmost index/pathmod
          prevmod = None
          previndex = 0
          mdir = hostdir
          for i,p in enumerate(pathparts):
            mpath = os.path.join(mdir, p)
            modfname = os.path.join(mpath, 'index.kweb')
            if os.path.isfile(modfname):
              prevmod = self._indexmod
              previndex = self._modindex
              (err, self._indexmod) = _load_path_module_method(modfname)
              if err is not None: return self.sendError(500, 'index-module (%s) exception'%p, err)
              self._pathmod = None #path/index.kweb is longer than path.kweb
              modstat = os.stat(modfname)
              self.modparts = tuple(pathparts[i+1:])
              self.moduledir = mpath
              self._modindex = i+1
            modfname = mpath + '.kweb'
            if os.path.isfile(modfname):
              (err, self._pathmod) = _load_path_module_method(modfname)
              if err is not None: return self.sendError(500, 'path-module (%s) exception'%p, err)
              modstat = os.stat(modfname)
              self.modparts = tuple(pathparts[i+1:])
              self.moduledir = mdir
            if not os.path.isdir(mpath):
              break
            mdir = mpath
          #if two indexmod and no pathmod - swap - so parent can be called first
          if (self._pathmod is None) and (prevmod is not None) and (prevmod != self._indexmod):
            self._pathmod = self._indexmod
            self._indexmod = prevmod
            self._modindex = previndex

      if ((self.content_length > 0) and
          (self.MAXBODYSIZE > 0) and
          (self.content_length > self.MAXBODYSIZE)):
        return self.sendError(411, 'content_length > MAXBODYSIZE')

      self.parse_query(url[4], self.args)
      self.session = self.server.gethost(host)[2]
      auth = self.headers.get("authorization")
      if auth is not None:
        auth = auth[0].split(' ', 1)
        if (2 != len(auth)): auth[1] = ':'
        if 'basic' == auth[0].lower():
          try:
            up = base64.decodestring(auth[1])
            self.auth = up.split(':',1)
            if 2 != len(self.auth): return self.sendError(401)
          except binascii.Error:
            return self.sendError(500, '_kall binascii.Error', traceback.format_exc())

      #could be the least-used feature - useful for segregating different hosts
      #probably better to run multiple kweb instances for each host, though...
      if self.server.runas > 1:
        try:
          if 2 == self.server.runas: modstat = os.stat(hostdir)
          os.setegid(modstat.st_gid)
          os.seteuid(modstat.st_uid)
        except:
          pass

    return None

  def _parseBody(self, body):
    if body is not None:
      if self.PARSEBODY:
        ctype = self.getheader('content-type')
        if ('multipart/form-data' == ctype[:19]):
          k, v = self.parse_header_value(ctype)
          boundary = v.get('boundary')
          if not boundary:
            return self.sendError(400, 'no boundary')
          err, parts = self.parse_formdata(body, boundary)
          if err: return self.sendError(400, err)
          self.args.extend(parts)
        else:
          #messed-up if request has query-string-params and form as urlencoded - but we deal with it ;-)
          self.parse_query(body.read(), self.args)
        body.seek(0) #as it has been parsed above and might be used by mods
      self.content = body

    if self._hostmod is not None:
      if self._kall(self._hostmod, True) is not None: return True

    if self._indexmod is not None:
      modparts = self.modparts
      self.modparts = tuple(self.pathparts[self._modindex:])
      if self._kall(self._indexmod) is not None: return True
      self.modparts = modparts

    if self._pathmod is not None:
      if self._kall(self._pathmod, True) is not None: return True

    # default module is self - look at GET method ;-)
    method = getattr(self, self.method, None)
    if callable(method):
      if self._kall(method) is not None: return True

    return self.sendError() #default is 404 Not found ;-)

  def parse_query(self, qs, result=[]):
    '''
    parse a HTTP query into a dictionary of arrays

    args:
      qs: query-string

    returns:
      [(name,value), (name,value),...]

    notes:
      * modifies the passed-dictionary, so that
        query_string in request-line and urlencoded body are accessible as one
      * from urlparse.parse_qsl
      * parse_qs was available only in cgi upto 2.4 and this logic is better
      * accepts name and name= formats - so &a&b&c are valid - probably violation of protocol
    '''
    for nvstr in [s2 for s1 in qs.split('&') for s2 in s1.split(';')]:
      if not nvstr: continue
      nv = nvstr.split('=', 1)
      name = urllib.unquote(nv[0].replace('+', ' '))
      if (len(nv) == 2): value = urllib.unquote(nv[1].replace('+', ' '))
      else: value = ''
      result.append((name, value))
    return result

  def _parse_header(self, s):
    '''
    parse a HTTP header into a dictionary of arrays

    args:
      s: header string

    returns:
      {key:[value,value2,...]}

    notes:
      * header keys can be repeated, hence the array-return
      * does not deal with folding
    '''
    result = {}
    if not s: return result
    for line in s.split('\r\n'):
      if (not line) or (line[0] in (' ', '\t')): continue
      kv=line.split(":",1)
      if 2 == len(kv):
        v = kv[1].strip()
      else:
        v = ''
      result.setdefault(kv[0].lower(), []).append(v)
    return result

  def parse_header_value(self, line):
    '''
    parse a Content-type like header

    args:
      line: HTTP header line

    returns:
      (content-type, {options})

    notes:
      * from cgi.parse_header
    '''
    parts = [i.strip() for i in line.split(';')]
    key = parts[0]
    result = {}
    for p in parts[1:]:
      i = p.find('=')
      if i >= 0:
        name = p[:i].strip().lower()
        value = p[i+1:].strip()
        if len(value) >= 2 and value[0] == value[-1] == '"':
          value = value[1:-1]
          value = value.replace('\\\\', '\\').replace('\\"', '"')
        result[name] = value
    return (key, result)

  def parse_formdata(self, fin, boundary, filedir=None, bufsize=4096, filemode=0):
    '''
    parse http-form-data (typically used for processing HTML forms)

    args:
           fin: input file handle
      boundary: MIME body part boundary - retrieved from MIME-header
       filedir: directory to store part-files in
       bufsize: buffer size - read file in buffer-size chunks
      filemode: file-override mode
                0 if file exists - append 1/2/3...until unique filename is found
                1 overwrite file, if it exists

    returns:
      (err, [parts])

    notes:
      * does not close fin
      * RFC 1867/2388
      * browsers dont' set content-length
      * does not parse multipart/mixed within multipart/form-data
      * does not deal with content-transfer-encoding
    '''
    parts = [] #(name, content, filename, content_length, content_type, content_encoding)
    partbegin = '--' + boundary
    lastpart = partbegin + '--'
    boundaryln = fin.readline().strip()
    if boundaryln != partbegin:
      return ('boundary not found in beginning', parts)
    while boundaryln != lastpart:
      #read header
      name = filename = ''
      cdisp = ctype = cencoding = None
      while 1:
        line = fin.readline()
        if not line.endswith('\r\n'):
          return ('invalid header termination (%s)'%line, parts)
        line = line[:-2]
        if line == '': break #end of header
        #since we are interested only in the content-disposition header - ignore everything else
        hname = line[:26].lower() #maximum header-name length is content-transfer-encoding
        if (cdisp is None) and ('content-disposition:' == line[:20].lower()):
          cdisp = self.parse_header_value(line[20:])
          if 'form-data' != cdisp[0]:
            return ('invalid Content-Disposition (%s)'%cdisp[0], parts)
          name = cdisp[1].get('name','')
          if not name:
            return ('Content-Disposition does not have name', parts)
          filename = cdisp[1].get('filename','')
          #ie6 bug sends full-path for filename - strip pathinfo
          if filename:
            n = len(filename) - 1
            while (n > 0) and (filename[n] != '\\'): n -= 1
            if filename[n] == '\\': filename = filename[n+1:]
        elif (ctype is None) and ('content-type:' == hname[:13]):
          ctype = self.parse_header_value(hname[13:])
        elif (cencoding is None) and ('content-transfer-encoding:' == hname[:26]):
          cencoding = self.parse_header_value(hname[26:])
      if not name:
        return ('Content-Disposition does not have name', parts)

      #set defaults for ctype and cencoding
      if ctype is None:
        #note: filename is optional (MAY in RFC ?!)
        if filename: ctype = ['application/octet-stream', {}]
        else: ctype = ['text/plain', {}]
      if not cencoding: cencoding = ['', {}]

      #read until end of part
      content = []
      clen = 0
      lastline = ''
      if ('' <> filename) and (filedir is not None):
        #open file in directory for writing here
        fqname = os.path.join(filedir, filename)
        if (0 == filemode) and os.path.exists(fqname):
          i = 1
          s = '%s-%d'%(filename,i)
          #possible race condition...
          while os.path.exists(os.path.join(filedir,s)):
            i += 1
            s = '%s-%d'%(filename,i)
          fqname = os.path.join(filedir, fname)
          filename = fname
        try:
          fh = open(fqname, 'wb')
        except:
          return ('unable to open: %s'%fqname, parts)
      else:
        fh = None
      while 1:
        line = fin.readline(bufsize)
        if not line:
          return ('invalid part', parts)
        if '--' == line[:2]:
          boundaryln = line.strip()
          if boundaryln in (partbegin, lastpart): break
        lastline = line
        clen += len(line)
        if fh: fh.write(line)
        else: content.append(line)
      if (len(lastline) < 2) or (lastline[-2:] != '\r\n'):
        if fh: fh.close()
        return ('invalid part termination', parts)
      if fh:
        #better safe than sorry ?!
        if (clen > 2):
          fh.seek(-2, 1)
          fh.truncate()
        fh.close()
      else:
        content[-1] = lastline[:-2]
      content = ''.join(content)
      #ignoring the parts for content-type and content-transfer-encoding
      parts.append((name, content, filename, (clen-2), ctype[0], cencoding[0]))
    return ('', parts)

  def _kall(self, method, mustkall=False):
    '''
    call/execute a module-method with the REQUEST object

    args:
      method: method to call

    returns:
      success:
        method return value
      error:
        False
    '''
    try:
      r = method(self)
    except:
      if getattr(method, '__name__', False):
        e = '%s exception\n%s' % (method.__name__, traceback.format_exc())
      else:
        e = traceback.format_exc()
      return self.sendError(500, '_kall exception', e)
    if r is not None:
      return self.sendResponse(str(r))
    elif mustkall:
      return self.sendError(404, 'mustkall: method response None')
    return None #None - call next method

  def addResponseHeader(self, line):
    '''
    add a HTTP response header line

    args:
      line: text to add to response header

    returns:
      None

    notes:
      * not checking for \r\n in header
    '''
    self._responseheaders.append(line)

  def setResponseHeader(self, key, value):
    '''
    set the value for a response header field

    args:
        key: field name
      value: field value

    returns:
      None

    notes:
      * does not set key, if reserved
      * reservedkeys are set by sendResponse
    '''
    reservedkeys = ('server', 'date', 'connection', 'content-type',
                    'content-length', 'accept-ranges')
    k = key.lower()
    if k not in reservedkeys: self._responseheaders.append('%s:%s'%(key, value))

  def setResponseType(self, ctype='text/plain'):
    '''
    set the Content-Type for the response

    args:
      ctype: content type

    returns:
      None

    notes:
      * since it is set by sendResponse, its' not really required
        but, useful in host/pathmod - results in shorter code.
    '''
    self._responsetype = ctype

  def sendResponse(self, content='', ctype='text/html', code=200, reason=None, clen=None, nocache=False):
    '''
    send HTTP response back to client

    args:
      content: content/http-response-body
        ctype: content type
         code: HTTP response code
       reason: HTTP reason
         clen: content length
      nocache: instructs the HTTP client not to cache the response

    returns:
      success:
        True
      error:
        False

    notes:
      * HTTP Status-Line = HTTP-Version SP Status-Code SP Reason-Phrase CRLF
      * pndng:
          range-header: multipart/byteranges
    '''
    if self.method is None: return False

    if not hasattr(content, 'read'): content = str(content)

    if self._responsetype is not None:
      ctype = self._responsetype
    if clen is None: clen = len(content)

    if (clen > 0):
      hrange = self.getheader('range')
      if ('bytes=' == hrange[:6]):
        firstbytepos = lastbytepos = 0
        byterangeset = hrange[6:]
        i = byterangeset.find('-')
        rangerr = (-1 == i)
        if not rangerr:
          try: firstbytepos = int(byterangeset[:i])
          except: rangerr = True
          if not rangerr: rangerr = (firstbytepos > clen)
          if not rangerr:
            i += 1
            if (i < len(byterangeset)):
              try: lastbytepos = int(byterangeset[i:])
              except: rangerr = True
            else:
              lastbytepos = clen-1
          if not rangerr:
            rangerr = (lastbytepos >= clen) or (lastbytepos < firstbytepos)
        if rangerr:
          code = 416
          reason = 'Requested Range Not Satisfiable'
          if hasattr(content, 'close'): content.close()
          content = ''
          clen = 0
          ctype = 'text/plain'
          self.KEEPALIVE = False
        else:
          code = 206
          reason = 'Partial Content'
          if hasattr(content, 'read'):
            content.seek(firstbytepos)
          else:
            content = content[firstbytepos:lastbytepos+1]
          self._responseheaders.append('Content-Range:bytes %d-%d/%d'%(firstbytepos,lastbytepos,clen))
          clen = lastbytepos-firstbytepos+1

    #small-optimization for frequent-use-cases
    if reason is None:
      if 200 == code:
        statusline = 'HTTP/1.1 200 OK'
      if 404 == code:
        statusline = 'HTTP/1.1 404 Not Found'
      else:
        global _KHTTP_RESPONSES
        statusline = 'HTTP/1.1 %d %s' % (code, _KHTTP_RESPONSES.get(code, '???'))
    else:
      statusline = 'HTTP/1.1 %d %s' % (code, reason)

    global _KWEB_SERVER_VERSION
    rlines = [statusline,
      _KWEB_SERVER_VERSION,
      time.strftime('Date: %a, %d %b %Y %H:%M:%S GMT',time.gmtime()),
      'Content-Type: %s' % ctype,
      'Content-Length: %d' % clen,
      'Accept-Ranges: bytes',
    ]

    if not self.KEEPALIVE:
      rlines.append("Connection: close")

    if nocache:
      rlines.append(time.strftime('Pragma: no-cache\r\nExpires: Mon, 26 Jul 1997 05:00:00 GMT\r\nCache-Control: no-cache, must-revalidate\r\nCache-Control: post-check=0, pre-check=0\r\nLast-Modified: %a, %d %b %Y %H:%M:%S GMT'))

    rlines.extend(self._responseheaders)
    rlines.append('\r\n') #End response-header
    rlines = '\r\n'.join(rlines)

    #zero-length body is valid
    if (clen > 0) and ('HEAD' != self.method):
      self._send(len(rlines), rlines, clen, content, self.KEEPALIVE)
    else:
      self._send(len(rlines), rlines, 0, '', self.KEEPALIVE)

    #minimal log information - more info: referer, useragent, could be accessed by index/modules, if reqd.
    self.server.log(self.host, self.remoteip, code, clen, self.content_length, self.line)

    self.method = None #so handle_read processes next request
    return True

  def sendError(self, errcode=404, errreason=None, errmessage=''):
    '''
    send HTTP error response back to client

    args:
         errcode: HTTP response code
       errreason: HTTP response status line reason
      errmessage: HTTP response content

    returns:
      False

    notes:
      * if app wants to respond with verbose errors - it should send 200
      * errors should be brief - save bandwidth/processing
      *  although http 1.1 mentions that persistant connections
         be maintained even on error - better to disconnect
         rogue connections.
      * pndng: custom 404
        + $HOSTDIR/404.html
        + $HOSTDIR/error.kweb
    '''
    self.KEEPALIVE = False
    if errreason is None:
      global _KHTTP_RESPONSES
      errreason = _KHTTP_RESPONSES.get(errcode, '???')
    if not errmessage: errmessage = errreason
    self.sendResponse(errmessage, 'text/plain', errcode, errreason)
    return False

  def html(self, body='<p>arigato gozaimasu</p>', title='(-: kweb9 :-)', headend='', footer=None):
    '''
    HTML5 template - loosely based on html5bones

    args:
         body: document body
        title: document title
      headend: end of document header
       footer: footer content

    returns:
      HTML5 document as a string

    notes:
      * sticky footer
    '''
    if footer is None:
      footer = '''<p><a href="http://www.houseofkodai.in/kweb"><img src="/bitby.gif" width="115" height="36" alt="bitby" /></a><br/>\
Copyright &copy; 2013 &nbsp;<a href="http://www.houseofkodai.in">houseofkodai</a></p>'''
    return '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="Content-language" content="en">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>%s</title>
<!--[if lt IE 9]>
<script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script>
<![endif]-->
<link rel="stylesheet" href="/kweb.css">
%s
</head>
<body>
<!--[if lt IE 9]>
<p class="chromeframe">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade to a HTML5 browser</a> or <a href="http://www.google.com/chromeframe/?redirect=true">activate Google Chrome Frame</a> to improve your experience.</p>
<![endif]-->

<div class="uptofooter">
<div class="topborder"></div>
<div class="content">%s</div>
</div>

<footer>
%s
</footer>
</body>
</html>''' % (title, headend, body, footer)

  def sendRedirect(self, url='/'):
    '''
    sends HTML redirect template

    args:
      url: redirect url

    returns:
      success:
        True
      error:
        False

    notes:
      * http://en.wikipedia.org/wiki/URL_redirection
      * http://en.wikipedia.org/wiki/HTTP_303
      * IE version 6 has a problem with redirect ?!
      * are we quoting the url too much ?!-)
    '''
    self._responseheaders.append('Location:%s'%url)
    return self.sendResponse(self.html('<p>redirecting to <a href="%s">%s</a></p>'%(url, urllib.quote(url)),
      title='::kweb::redirect',
      headend='<meta HTTP-EQUIV="refresh" CONTENT="0;URL=%s">\n'%url), code=303, nocache=True)

  def sendFile(self, fname=''):
    '''
    send file as html response

    args:
      fname: fully qualified file name

    returns:
      success:
        True
      error:
        False

    notes:
      * pndng:
          + send .gz files, if they exist and browser supports compression
    '''
    try:
      fs = os.stat(fname)
    except:
      return self.sendError(404, "os.stat(%s)" % fname)
    fsize = fs.st_size

    #int(fs.st_mtime) gets rid of microseconds - since it does not require it.
    lastmodified = datetime.datetime.fromtimestamp(int(fs.st_mtime))
    HTTP_DATE_FMT = "%a, %d %b %Y %H:%M:%S GMT"

    ims = self.getheader('If-Modified-Since')
    if ims:
      try:
        ims = datetime.datetime.strptime(ims, HTTP_DATE_FMT)
        if (ims > lastmodified): self.sendResponse(code=304)
      except: pass

    etag = '%d%d'%(int(fs.st_mtime), int(fs.st_size))
    if (etag == self.getheader('If-None-Match')):
      return self.sendResponse(code=304)

    if (fsize > 0) and ('HEAD' != self.method):
      #dont' worry fh will be closed in handle_write or handle_close
      try:
        fh = open(fname, 'rb')
      except OSError as e:
        return self.sendError(404, '-ERR %d %s' % (e.errno, e.strerror))
    else:
      fh = ''

    self._responseheaders.append('ETag:%s'%etag)
    self._responseheaders.append('Last-Modified:%s'%lastmodified.strftime(HTTP_DATE_FMT))
    global _KEXTENSIONS_MAP
    i = len(fname) - 1
    while i and ('.' <> fname[i]): i -= 1
    if ('.' == fname[i]): ext = fname[i:]
    else: ext = fname
    if not _KEXTENSIONS_MAP.has_key(ext): ext = ext.lower()
    ftype = _KEXTENSIONS_MAP.get(ext, 'application/octect-stream')
    return self.sendResponse(fh, ctype=ftype, clen=fsize)

  def getheader(self, key, default=''):
    '''
    get HTTP request header field value

    args:
          key: header field name
      default: default value if key does not exist

    returns:
      header field value or default
    '''
    return self.headers.get(key, [default])[0]

  def htmlescape(self, s):
    '''
    escape html characters: replace &<>" characters in string

    args:
      s: string to escape

    returns:
      html escaped string

     notes:
       * cgi.escape
    '''
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

  def listdir(self, path='', sortby=0, fext=(), rtype=2):
    '''
    list the files in a directory

    args:
        path: fully-qualified directory path name.
      sortby: sort by field (name, time, size)
              0 none 1 name 2 time 3 size
              negative numbers reverse the sort order
        fext: tuple of file-extensions (endswith strings)
              ex. fext=('.txt', '.log', '.tmp')
       rtype: return-type
              0 array 1 text/plain 2 text/html 3 text/json

    returns:
      success:
        Tuple/String
      error:
        None

    notes:
      * exceptions in file-stat sets value to 0
    '''
    if not os.path.isdir(path):
      if 0 == rtype: return ()
      elif rtype < 3: return ''
      elif 3 == rtype: return '[]'
      else: return None #should not come here
    flist = []
    if fext:
      fltr = lambda f: any(f.endswith(x) for x in fext)
    else:
      fltr = lambda f: True
    for fname in os.listdir(path):
      if not fltr(fname): continue
      fqname = os.path.join(path, fname)
      if os.path.isdir(fqname): ftype = 1
      elif os.path.islink(fqname): ftype = 2
      else: ftype = 0
      try:
        fs = os.stat(fqname)
      except:
        flist.append((fname, 0, 0, ftype)) #so errors can be detected by caller
        continue
      flist.append((fname, int(fs.st_mtime), fs.st_size, ftype))
    if (sortby > 3) or (sortby < -3): sortby = -2
    i = abs(sortby)
    flist.sort(key=lambda a:a[i-1], reverse=(sortby<0))
    #sequence-order is most-likely to less likely
    if 2 == rtype:
      sb = [1, -2, -3]
      sb[i-1] = -sortby
      if fext: fext = '&fext=%s'%','.join(fext)
      else: fext = ''
      div = ['<table id="dirtable">\n<tr><th align="right"><a href="?sortby=%d%s">Size</a></th><th align="left"><a href="?sortby=%d%s">Date</a></th><th align="left"><a href="?sortby=%d%s">Name</a></th></tr>'%(sb[2], fext, sb[1], fext, sb[0], fext)]
      suffix = ('','/','@')
      lnksuffix = ('','/','')
      uq = urllib.quote
      htmlescape = self.htmlescape
      now = time.localtime()
      for i in flist:
        name = i[0]
        if (name == 'index.kweb'): continue
        if ('.kweb' == name[-5:]): name = name[:-5]
        fdate = time.localtime(i[1])
        if (fdate.tm_year == now.tm_year) and (fdate.tm_mon == now.tm_mon) and (fdate.tm_mday == now.tm_mday):
          datestr = time.strftime('Today, %H:%M', fdate) #can also use %I:%M %p for 12 hour format
        else:
          datestr = time.strftime('%d %b %Y', fdate)
        div.append('<tr><td align="right">%s</td><td>%s</td><td><a href="%s%s">%s%s</a></td></tr>'%
          (_KWEB.strsize(i[2]), datestr, uq(name), lnksuffix[i[3]], htmlescape(name), suffix[i[3]]))
      div.append('</table>')
      return '\n'.join(div)
    elif 0 == rtype:
      return tuple(flist)
    elif 3 == rtype:
      return '[\n%s\n]' % (',\n'.join("['%s',%d,%d,%d]"%i for i in flist))
    elif 1 == rtype:
      return '\n'.join('%5d %s %s'%(i[2], time.strftime('%d %b %Y', time.localtime(i[1])), i[0]) for i in flist)
    return None #should not come here - better to enable the caller to get an exception by attempting to use None

  def htmldir(self, urlpath='/', sortby=-2, fext=()):
    '''
    list of files in a directory

    args:
     urlpath: url-path that along-with hostdir is file-system path
      sortby: sort by field (name, time, size)
              0 none 1 name 2 time 3 size
              negative numbers reverse the sort order
        fext: tuple of file-extensions (endswith strings)
              ex. fext=('.txt', '.log', '.tmp')

    returns:
      success:
        html
      error:
        html

    notes:
    '''
    def bread_crumb(path='', host=''):
      u = ''
      bc = []
      foo = path.split('/')
      if not foo[0]: foo = foo[1:]
      if not foo[-1]: foo = foo[:-1]
      for i in foo[:-1]:
        if i:
          u += '/%s' % i
          bc.append('<a href="%s/">%s</a>' % (u, i))
      if bc:
        return '<a href="/">%s</a>/%s/%s' % (host, '/'.join(bc), foo[-1])
      else:
        if foo: return '<a href="/">%s</a>/%s' % (host, foo[-1])
        else: return host
    div = ['<div id="divdir">']
    if urlpath[-1] != '/': div.append('<base href="%s/" />'%urlpath)
    div.append(bread_crumb(urlpath, self.host))
    div.append(self.listdir(self.hostdir + urlpath, sortby, fext))
    div.append('</div>')
    return '\n'.join(div)

  def GET(self, R):
    fqpath = self.hostdir + self.urlpath
    if os.path.isfile(fqpath):
      return self.sendFile(fqpath)

    if os.path.isdir(fqpath):
      if '/' == fqpath[-1]: fqname = fqpath + 'index.html'
      else: fqname = fqpath + '/index.html'
      if os.path.isfile(fqname): return self.sendFile(fqname)
      fqname = fqname[:-1] #index.htm
      if os.path.isfile(fqname): return self.sendFile(fqname)
      #no-need for redirect - as <base> element added in listdir
      #if '/' != urlpath[-1]: return self.sendRedirect(urlpath+'/')
      sortby = -2
      fext = ()
      for k,v in R.args:
        if 'sortby' == k:
          try: sortby = int(v)
          except: sortby = -2
        if 'fext' == k:
          fext =  v.split(',')
      return self.sendResponse(self.html(self.htmldir(R.urlpath, sortby, fext)))

    item = _KRESOURCES_DEFAULT.get(self.urlpath)
    if item:
      return self.sendResponse(item[1], item[0])
    if '/kweb' == self.urlpath:
      return self.sendResponse(R.__doc__%_KWEB_SERVER_VERSION, 'text/plain')
    if '/kweb/log' == self.urlpath:
      a = []
      for k,v in kweb.server.perhost.items():
        a.append('\n%s'%k)
        a.append('\n'.join(str(i) for i in v[0] if i))
      return self.sendResponse('\n'.join(a), 'text/plain')
    #can add kweb/admin interface here ;-)

# ##################################################################################################
# GLOBAL METHODS
# ##################################################################################################
_KIMPORT_CACHE = {}
def _kimport(fqname):
  '''
    returns
      (err, module)
      err is string, if exception or None if success
    notes:
      * imp.load_source stores module name in sys.modules, so modname needs to be unique
        especially if you want to import two modules with same name in different directories
      * using global _KIMPORT_CACHE instead of a class - simpler code, easier to understand/manage
  '''
  try: ft = os.stat(fqname).st_mtime
  except OSError, e: return (e, None)
  global _KIMPORT_CACHE
  (ct, cmodule) = _KIMPORT_CACHE.get(fqname, (-1, None))
  if (None <> cmodule):
    if (ct == ft): return (None, cmodule)
    else: del _KIMPORT_CACHE[fqname]
  alphanumeric = lambda s: ''.join([c for c in s if ((c >= 'a') and (c <= 'z')) or ((c >= 'A') and (c <= 'Z')) or ((c >= '0') and (c <= '9'))])
  try:
    ft = os.stat(fqname).st_mtime
    fmodule = imp.load_source(alphanumeric(fqname), fqname)
  except:
    return (traceback.format_exc(), None)
  if not hasattr(fmodule, 'NOCACHE'): _KIMPORT_CACHE[fqname] = (ft, fmodule)
  return (None, fmodule)

class _KeyValueFile(object):
  '''
  key:value file
  AUTHOR:
    Karthik@houseofkodai.in
  DATE:
    * 12 JAN 2011
      + added items()
      + changed index in set to -1 as default value to enable adding new value
      + moved kvsplit to load - save function call on every line
    * 14 DEC 2011
      + keepold and saveonset override bug fixed
      + deleting items was not working b4 - now fixed
    * 12 DEC 2011
      + added has_key
      + added keepold
      + load returns True or False
      + added dosave to set - enabling save on specific items
    * 11 DEC 2011
      + value in kvsplit should not be stripped
    * 10 DEC 2011
      + added getfirst
      + remove __getattr__ not working as expected ?!
    * 1 NOV 2011
      + stored value in addition to lineno in dict - speedier reads, by eliminating kvsplit
      + load file on get, if newer
    * 30 OCT 2011
      + changed _keys to _items
      + added get() to retrieve with default values
    * 1 JUN 2011
      + used _keys.setdefault instead of has_key in load()
    * 6 OCT 2010
      + maintains line positions ;-) similar to editing a file
      + should really be a seperate module - but is convinent to be in this file

  =====================
  key:value file-format
  =====================
  #r=relayid, n=name, e=emailid, m=mobile, t=transaction
  password:xyz
  n:Karthik Ayyar
  m:(93823) 15252
  e:karthik@enmail.com
  r:abc@def.com
  r:ijk@foo.com
  t:1029384:ts:234.32.44.1:activated <abc@def.com>
  t:1029384:ts:234.32.44.1:deactivated <abc@def.com>
  '''
  def __init__(self, fname='', delimiter=':', saveonset=True, keepold=True):
    self.fname = fname
    self.delimiter = delimiter
    self.saveonset = saveonset
    self.keepold = keepold
    self.flines = []
    self.mtime = 0
    self._items = {}
    self._delines = {}
    if fname: self.load(fname)
  def keys(self):
    return [k for k in self._items.keys() if not self._delines.has_key(k)]
  def items(self):
    return [(k,[i[1:] for i in v]) for k,v in self._items.items()]
  def has_key(self, name=''):
    return ((self._items.has_key(name)) and (not self._delines.has_key(name)))
  def load(self, fname):
    if not fname: return False
    try: fh = open(fname)
    except: return False
    self.fname = fname
    self.mtime = os.stat(fname).st_mtime
    self.flines = []
    self._items = {}
    self._delines = {}
    self.flines = map(string.strip, fh.readlines())
    fh.close()
    for i, ln in enumerate(self.flines):
      if 0 == len(ln): continue
      if '#' == ln[0]: continue
      kv = ln.split(self.delimiter, 1)
      #note: values are not stripped, only key
      k = kv[0].strip()
      if len(kv) > 1: v = kv[1]
      else: v = ''
      self._items.setdefault(k, []).append((i,v))
    return True
  def get(self, name, default='', firstvalue=False):
    '''
    description

    args:
      name: name of import module

    returns:
      success
        module
      failure
        False

    notes:
      *
    '''
    try: mtime = os.stat(self.fname).st_mtime
    except: mtime = 0
    #keep instance if file is deleted
    if (mtime > 0) and (mtime <> self.mtime): self.load(self.fname)
    if not self._items.has_key(name): return default
    if self._delines.has_key(name): return default
    vlist = [i[1] for i in self._items[name]]
    if firstvalue: return vlist[0]
    return vlist
  def getfirst(self, name, default=''):
    return self.get(name, default, True)
  def save(self, keepold=None):
    if not self.fname: return False
    fdata = []
    for i, ln in enumerate(self.flines):
      if not self._delines.has_key(i): fdata.append(ln)
    if fdata:
      tmpname = self.fname + '.tmp'
      try:
        fh = open(tmpname, 'w')
        fh.write('\n'.join(fdata))
        fh.write('\n') #for last line
        fh.close()
      except:
        return False
    oldname = self.fname + '.old'
    try:
      if os.path.isfile(oldname): os.remove(oldname)
      if keepold is None: keepold = self.keepold
      if keepold:
        if os.path.isfile(self.fname): os.rename(self.fname, oldname)
      else: os.remove(self.fname)
      if fdata: os.rename(tmpname, self.fname)
    except:
      return False
    #not the most efficient way to maintain internal-state-data-structures...but works
    self.load(self.fname)
    return True
  def set(self, name, value, index=-1, saveonset=None):
    '''
    append on index < 0 else change/add appropriate entry
    '''
    if None == value:
      #add line-number to delkeys if value is None
      for i in self._items.get(name, []):
        self._delines[i[0]] = None
      #set name also in delines - so keys() works
      self._delines[name] = None
    else:
      #add/edit/append appropriate entry
      value = str(value)
      ln = '%s%s%s' % (name, self.delimiter, value)
      n = len(self.flines)
      #remove key from delkeys, if exists
      if self._delines.has_key(name): del self._delines[name]
      if not self._items.has_key(name):
        self.flines.append(ln)
        self._items[name] = [(n,value)]
      else:
        #if valid index - update entry else append entry
        if (index >= 0) and (index < len(self._items[name])):
          self.flines[self._items[name][index][0]] = ln
        else:
          self.flines.append(ln)
          self._items[name].append((n,value))
    if saveonset is None: saveonset = self.saveonset
    if saveonset: self.save(self.keepold)
    return True

class _Ktxtbl(object):
  '''
  AUTHOR:
    Karthik@houseofkodai.in
  DESCRIPTION:
    txt file database
    one record per line
    fields seperated by delimiter
    optional 1st-#line is column-names
    does not save # and empty lines
    avoid the use of spaces in column-names
    default column-names a,b,... cannot be used if columns is present
  NOTES:
    * not using dict for column-lookup,
      for small sized lists, tuple-lookup is fast-enough
  DATE:
    * 18 MAR 2012
      + simplified txtable based on older version in db.py
  NOTES:
    * look at http://csvkit.readthedocs.org/en/latest/index.html
  '''
  def __init__(self, filename='', delimiter=':', columns='',
                                  keepold=True, saveonset=True):
    self.filename = filename
    self.delimiter = delimiter
    if columns:
      self.columns = tuple(headerline.split(self.delimiter))
    else:
      self.columns = None
    self.rows = []
    self.keepold = keepold
    self.saveonset = saveonset
    self.mtime = 0 #dont' load if file has not changed
    if os.path.isfile(filename): self.load()

  def addrows(self, s):
    if self.columns is not None: ncols = len(self.columns)
    elif self.rows: ncols = len(self.rows[0])
    else: ncols = 0
    if s[-1] == '\n': s = s[:-1] #avoid-last-empty-string on split
    nrows = 0
    for ln in s.split('\n'):
      ln = ln.strip()
      if not ln: continue
      if 0 == ncols:
        if ('#' == ln[0]):
          ln = ln[1:].strip()
          if not ln: continue
          self.columns = tuple(map(string.strip, ln.split(self.delimiter)))
          ncols = len(self.columns) - 1
        else:
          row = tuple(map(string.strip, ln.split(self.delimiter)))
          ncols = len(row) - 1
          self.rows.append(row)
          nrows += 1
      elif ('#' != ln[0]):
        row = ln.split(self.delimiter, ncols)
        n = ncols - len(row) + 1
        if (n > 0): row.extend(['']*n)
        self.rows.append(tuple(row))
        nrows += 1
    return nrows

  def load(self):
    try: mtime = os.stat(self.filename).st_mtime
    except: mtime = 0
    if (mtime > 0) and (mtime == self.mtime):
      return True
    try: fh = file(self.filename, 'r')
    except: return False
    s = fh.read()
    fh.close()
    self.mtime = mtime
    self.columns = None
    self.rows = []
    self.addrows(s)
    return True

  def __str__(self):
    cln = rln = lastln = ''
    if self.columns:
      cln = '#%s\n' % self.delimiter.join(self.columns)
    if self.rows:
      rln = '\n'.join([self.delimiter.join(row)
        for row in self.rows])
      lastln = '\n'
    return '%s%s%s'%(cln, rln, lastln)

  def save(self):
    if not self.filename: return False
    if self.columns or self.rows:
      if self.keepold:
        oldfname = self.filename + '.old'
        try:
          if os.path.isfile(oldfname): os.remove(oldfname)
          if os.path.isfile(self.filename):
            os.rename(self.filename, oldfname)
        except:
          pass
      try:
        fh = open(self.filename, 'w')
        fh.write(self.__str__())
        fh.close()
      except:
        return False
    return True

  def match(self, value, s):
    '''
      s starts with
        ^ value starts with s
        $ value ends with s
        ~ value contains s
        < value is less than s (value/s converted to int first)
          can also be >x<y
        > value is greater than s
    '''
    if value == s: return True
    lens = len(s) - 1
    if 0 == lens: return False
    c = s[0]
    s = s[1:]
    if c == '>':
      try: value = int(value)
      except: return False
      i = s.find('<')
      if -1 == i:
        try: gt = int(s)
        except: return False
        if (value > gt): return True
        return False
      else:
        try: lt = int(s[i+1:])
        except: return False
        try: gt = int(s[:i])
        except: return False
        if gt < value < lt: return True
        return False
    elif c == '<':
      try:
        s = int(s)
        value = int(value)
      except:
        return False
      if (value < s): return True
      return False
    elif ('$' == c):
      if lens > len(value): return False
      i = value.rfind(s)
      if (i == (len(value)-lens)): return True
      return False
    else:
      if lens > len(value): return False
      i = value.find(s)
      if ('~' == c) and (i <> -1): return True
      elif ('^' == c) and (i == 0): return True
      return False

  def selectrows(self, **kvargs):
    '''
    select rows where all column=value (kvargs) match
    default-column-names a,b,c are available only if columns is None
    '''
    if (not self.rows) or (not kvargs): return
    cvlist = []
    if self.columns is not None: ncols = len(self.columns)
    else: ncols = len(self.rows[0])
    for k,v in kvargs.items():
      if self.columns is None:
        #access columns as a, b, c, ...
        i = ord(k[0])-97
        if 0 <= i < ncols: cvlist.append((i,v))
      else:
        try: i = self.columns.index(k)
        except ValueError: continue
        cvlist.append((i,v))
    if not cvlist: return
    for i,row in enumerate(self.rows):
      match = True
      for c,v in cvlist:
        match = self.match(row[c], v)
        if not match: break
      if match: yield i, row

  def select(self, *kargs, **kvargs):
    '''
    select rows of columns (position/name from kargs) from selectrows
    '''
    if not self.rows: return
    clist = []
    if self.columns is not None: ncols = len(self.columns)
    else: ncols = len(self.rows[0])
    typint = type(0)
    for c in kargs:
      if isinstance(c, typint):
        if 0 <= c < ncols: clist.append(c)
      elif self.columns is not None:
        try: i = self.columns.index(c)
        except ValueError: continue
        clist.append(i)
      else:
        i = ord(c[0])-97
        if 0 <= i < ncols: clist.append(i)
    if kargs and (not clist): return
    for i, row in self.selectrows(**kvargs):
      if clist:
        yield tuple([row[c] for c in clist])
      else:
        yield row
    return

  def get(self, columnid=0, **kvargs):
    '''
    get value of column from selectedrow
    '''
    try:
      return self.select(columnid, **kvargs).next()[0]
    except StopIteration:
      return None

  def set(self, columnid=0, value='', numrows=1, **kvargs):
    '''
    set value upto first numrows matching rows
    return (number-of-rows-updated, file-saved)
    '''
    if not self.rows: return (0, False)
    typint = type(0)
    if not isinstance(columnid, typint):
      if self.columns is None: return (0, False)
      try: columnid = self.columns.index(columnid)
      except: return (0, False)
    if self.columns is not None: ncols = len(self.columns)
    else: ncols = len(self.rows[0])
    if (0 > columnid) or (columnid >= ncols): return (0, False)
    rcount = 0
    if kvargs:
      for i, row in self.selectrows(**kvargs):
        row = [v if c != columnid else value for c,v in enumerate(row)]
        self.rows[i] = tuple(row)
        rcount += 1
    else:
      for i,row in enumerate(self.rows):
        row = [v if c != columnid else value for c,v in enumerate(row)]
        self.rows[i] = tuple(row)
        rcount += 1
    if self.saveonset: return (rcount, self.save())
    return (rcount, False)

  def delrows(self, **kvargs):
    '''
     * returns (number-of-rows-deleted, file-saved)
    '''
    dlist = {}
    for i, row in self.selectrows(**kvargs): dlist[i] = None
    if not dlist: return (0, False)
    self.rows = [r for i,r in enumerate(self.rows) if not dlist.has_key(i)]
    if self.saveonset: return (len(dlist), self.save())
    return (len(dlist), False)

# ##################################################################################################
# GLOBAL METHODS END
# ##################################################################################################

class _kweb(object):
  '''
  holder class for common methods
  '''
  def __init__ (self):
    self.KeyValueFile = _KeyValueFile
    self.Txtbl = _Ktxtbl

  def txpand(self, formatstr, d, marker='"'):
    '''
    interpolating variables in a string - python cookbook
    '''
    def lookup(w): return d.get(w, w.join(marker*2))
    parts = formatstr.split(marker)
    parts[1::2] = map(lookup, parts[1::2])
    return ''.join(parts)

  def strsize(self, i):
    '''
    human-readable size in bytes (B), Kilobytes (KB), Megabytes (MB), and Gigabytes (GB)
    '''
    if 0 == i: return '0'
    for b in ((1073741824.0, 'GB'), (1048576.0, 'MB'), (1024.0, 'KB')):
      if i >= b[0]: return '%.2f %s' % ((i/b[0]),b[1])
    return '%d B' % i

  def strdate(self, t=None, timefmt='%H:%M %p'):
    '''
    human-readable date format
    '''
    if t is None:
      t = int(time.time())
    elif type(t) <> type(0):
      try: t = int(t)
      except: return 'invalid (%s)'%t
    t = time.localtime(t)
    now = time.localtime()
    #same year
    if now[0] == t[0]:
      #same month
      if now[1] == t[1]:
        ndays = now[2]-t[2]
        #same day
        if 0 == ndays:
          fmt = 'Today, %H:%M %p'
        elif 1 == ndays:
          fmt = 'Yesterday %s'%(timefmt)
        elif 7 > ndays:
          fmt = '%%A, %%d %%b %s' % (timefmt)
        else:
          fmt = '%d days ago, %%d %%b %s' % (ndays, timefmt)
      else:
        fmt = '%%d %%b %%Y %s' % (timefmt)
    else:
      fmt = '%%d %%b %%Y %s' % (timefmt)
    return time.strftime(fmt, t)

  def uniqueid(self, idlen=7):
    '''
    return '%d%.0f'%(random.randint(100000,999999),time.time())
    a is url-safe
    '''
    a = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    na = len(a)-1
    return ''.join([a[random.randint(0,na)] for i in xrange(idlen)])

  def command(self, cmdline, useshell=True, timeout=2):
    '''
    returns (pid, stdout, stderr)
      * if error pid is 0
    warning:
      * parse cmdline to ensure it is safe
    '''
    cmdline = shlex.split(cmdline)
    try:
      p = subprocess.Popen(cmdline, shell=useshell, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except OSError as e:
      return (0, e.errno, e.strerror)
    t = threading.Thread(target=lambda: p.wait())
    t.start()
    t.join(timeout)
    timeout = t.is_alive()
    if timeout:
      p.terminate()
      t.join()
    out = p.stdout.read()
    p.stdout.close()
    err = p.stderr.read()
    p.stderr.close()
    if p.returncode: return (0, p.returncode, err)
    return (p.pid, out, err)

  def parse_emailid(self, emailid):
    '''
     returns
       (localpart, domainpart)
       if domainpart is None - invalid emailid
     notes:
       according to RFC 5321 only domain-part can to be validated
         localpart is left upto receipient' server.
     pndng
       expand parsing to return name, comment for
        "Karthik Ayyar" <karthik@houseofkodai.in> (+919941996264)
     format
       local-part@domain-part
     refs:
       http://en.wikipedia.org/wiki/Email_address
       http://www.cs.tut.fi/~jkorpela/rfc/822addr.html
       http://www.secureprogramming.com/?action=view&feature=recipes&recipeid=1
    '''
    local = domain = None
    n = len(emailid)
    if (n < 6) or (n > 254): return local, domain
    maxl = n - 5 #smallest domain-part is @b.in 5 characters
    if maxl > 64: maxl = 64
    asciinotallowed = '()<>@,;:\\"[]'
    #local-part
    i = 0
    while i < maxl:
      if emailid[i] == '"' and (not i or emailid[i-1] == '.' or emailid[i-1] == '"'):
        i += 1
        while i < maxl:
          if emailid[i] == '"': break
          if emailid[i] == '\\' and emailid[i+1] == ' ':
            i += 2
            continue
          if ord(emailid[i]) < 32 or ord(emailid[i]) >= 127: return local, domain
          i += 1
        else: return local, domain
        if emailid[i] == '@': break
        if emailid[i] != '.': return local, domain
        i += 1
        continue
      if emailid[i] == '@': break
      if ord(emailid[i]) <= 32 or ord(emailid[i]) >= 127: return local, domain
      if emailid[i] in asciinotallowed: return local, domain
      i += 1
    if not i or emailid[i-1] == '.': return local, domain
    local = emailid[:i]
    #domain-part
    j = i = i + 1
    if j >= (n-2): return local, domain
    while i < n:
      if emailid[i] == '.':
        if i == j or emailid[i-1] == '.': return local, domain
      if ord(emailid[i]) <= 32 or ord(emailid[i]) >= 127: return local, domain
      if emailid[i] in asciinotallowed: return local, domain
      i += 1
    return local, emailid[len(local)+1:]

  def html_input(self, name='html_input', typ=None, value=None, label=None):
    if label:
      el = ['<label for="%s">%s</label><input name="%s" id="%s"'%(name, label, name, name)]
    else:
      el = ['<input name="%s"'%(name)]
    if typ: el.append(' type="%s"'%typ)
    if value:
      if 'checkbox' == typ:
        el.append(' checked')
      else:
        el.append(' value="%s"'%value)
    el.append(' />')
    return ''.join(el)

  def html_textarea(self, name='html_textarea', value=None, label=None, args=''):
    if label:
      el = ['<label for="%s">%s</label><textarea name="%s" id="%s" %s>'%(name, label, name, name, args)]
    else:
      el = ['<textarea name="%s" %s>'%(name, args)]
    if value: el.append(value)
    el.append('</textarea>')
    return ''.join(el)

  def html_select(self, name='html_select', value=None, label=None, items=None):
    if not items: return ''
    if label:
      el = ['<label for="%s">%s</label><select name="%s" id="%s">'%(name, label, name, name)]
    else:
      el = ['<select name="%s">'%(name)]
    if (type(items[0]) == type(())):
      for i in items:
        if i[0] == value:
          el.append('<option value="%s" selected>%s</option>' % (i[0], i[1]))
        else:
          el.append('<option value="%s">%s</option>' % (i[0], i[1]))
    else:
      for i in items:
        if i == value:
          el.append('<option selected>%s</option>' % (i))
        else:
          el.append('<option>%s</option>' % (i))
    el.append('</select>')
    return ''.join(el)

  def html_radio_list(self, name='html_radio_list', value=None, label=None, items=None):
    if not items: return ''
    if label:
      a = ['<fieldset id="%s"><legend>%s</legend>'%(name, label)]
    else:
      a = ['<fieldset>']
    if (type(items[0]) == type(())):
      for i in items:
        if i[0] == value: c = 'checked'
        else: c = ''
        a.append('<input type=radio name="%s" id="%s-%s" value="%s" %s/><label for="%s-%s">%s</label>' % (name, name, i[0], i[0], c, name, i[0], i[1]))
    else:
      for i in items:
        if i == value: c = 'checked'
        else: c = ''
        a.append('<input type=radio name="%s" id="%s-%s" value="%s" %s/><label for="%s-%s">%s</label>' % (name, name, i, i, c, name, i, i))
    a.append('</fieldset>')
    return ''.join(a)

  def load_form(self, fname):
    '''
    form definition parser that generates fieldsets used by html_form
    '''
    r = []
    try:
      flines = file(fname).readlines()
    except:
      return tuple(r)
    for ln in flines:
      ln = ln.strip()
      if not ln: continue
      c1 = ln[0]
      if '#' == c1: continue
      if (c1 >= '0') and (c1 <= '9'):
        c1 = int(c1)
        if 0 == c1:
          fa = ln.split(':',1)
        else:
          fa = [f.strip() for f in ln.split(':',4)]
          if 5 == len(fa):
            if (6 == c1) or (7 == c1):
              args = tuple([f.strip() for f in fa[4].split(',')])
              if (len(args[0].split(' ',1)) > 1):
                fa[4] = tuple([tuple(i.split(' ',1)) for i in args])
        fa[0] = c1
        if r:
          r[-1].append(tuple(fa))
        else:
          r.append([tuple(fa)])
      else:
        if '_' == ln:
          r.append([''])
        else:
          r.append([ln])
    return tuple(r)

  def html_form(self, action='', fieldsets=(), fieldvalues={}, fielderrors={}, method='', enctype='', attrs=''):
    '''
      html form generation
        * the last few years experience shows that html/tag generation templating is a mugs game
          only adds a new layer of complexity (additional thing to learn on top of html
        * current approach is to use long strings (simple, easy-to-understand/maintain, no-additional overhead)
        * however, methods to aid in html-form generation is quite useful as they provide a
        * consistent way to communicate data-structures
        * does not add class/additional attributes to form-elements
          better to set class attribute to form element and define it in css
          or use a enclosing div for that
        * sets' field-names and id to be the same - not convinced about use-case for different name/id
        * http://www.w3.org/TR/html401/interact/forms.html#h-17.3
        * when the form includes a TYPE=file INPUT element, the ENCTYPE should be multipart/form-data and the METHOD must be post

      args:
             action: form action
          fieldsets: tuple of fieldsets or file containing fieldsets
                     fieldset: tuple of fields
                               field: (type, name, label, args)
                                        type: (0:html, 1:text, 2:submit, 3:password, 4:checkbox, 5:file, 6:radio, 7:select, 8:textarea)
                                       value: default value
                                        name: field name
                                       label: field label
                                        args: list of name/value pairs for select/radio or element attributes for textarea
        fieldvalues: dictionary of field-name and field-value
        fielderrors: dictionary of field-name and field-errors - which gets added below field element
             method: form submit method *GET or POST (default is *)
            enctype: encoding type *application/x-www-form-urlencoded or multipart/form-data (default is *)
              attrs: form element attributes ex. id="frmX"

      returns:
        string: html form
    '''
    def _fieldset(legend='', fields=(), fieldvalues={}, fielderrors={}):
      if legend:
        a = ['<fieldset><legend>%s</legend>'%(legend)]
      else:
        a = []
      for f in fields:
        nf = len(f)
        if (not f) or (nf < 2): continue
        ft = f[0]
        ferr = None
        if 0 != ft:
          fn = f[2]
          fv = fieldvalues.get(fn, f[1])
          f3 = (f[3] if (nf>3) else None)
          ferr = fielderrors.get(fn)
        if 0 == ft:
          a.append(f[1])
        elif 1 == ft:
          a.append(self.html_input(fn, None, fv, f3))
        elif 2 == ft:
          a.append(self.html_input(fn, 'submit', fv, f3))
        elif 3 == ft:
          a.append(self.html_input(fn, 'password', fv, f3))
        elif 4 == ft:
          a.append(self.html_input(fn, 'checkbox', fv, f3))
        elif 5 == ft:
          a.append(self.html_input(fn, 'file', fv, f3))
        elif 6 == ft:
          a.append(self.html_radio_list(fn, fv, f3, (f[4] if (nf>4) else ())))
        elif 7 == ft:
          a.append(self.html_select(fn, fv, f3, (f[4] if (nf>4) else ())))
        elif 8 == ft:
          a.append(self.html_textarea(fn, fv, f3, (f[4] if (nf>4) else '')))
        if ferr is not None: a.append(ferr)
      if legend: a.append('</fieldset>')
      return ''.join(a)
    a = ['<form']
    if action: a.append(' action="%s"'%action)
    if method: a.append(' method="%s"'%method)
    if enctype: a.append(' enctype="%s"'%method)
    if attrs: a.append(attrs)
    a.append('>')
    if type(fieldsets) == type(''):
      fieldsets = self.load_form(fieldsets)
    for fs in fieldsets:
      if (type(fs[0]) == type('')):
        a.append(_fieldset(fs[0], fs[1:], fieldvalues, fielderrors))
      else:
        a.append(_fieldset('', fs, fieldvalues, fielderrors))
    a.append('</form>')
    return ''.join(a)

  def smtpmail(self, mxhost, helo, mailfrom, rcptto, data, authuser=None, authpass=None):
    '''
    quick and dirty smtp email sender
    '''
    try:
      s = smtplib.SMTP(mxhost)
      r = s.ehlo(helo)
      if 250 == r[0]:
        if authuser and authpass:
          r = s.login(authuser, authpass)
        if 250 == r[0]:
          r = s.mail(mailfrom)
          if 250 == r[0]:
            r = s.rcpt(rcptto)
            if 250 == r[0]:
              r = s.data(data)
      s.quit()
      if 250 <> r[0]:
        return '- err %s: %s' % (mxhost, r)
    except Exception,details:
      return '- err %s: %s' % (mxhost, details)
    return '+'

_KWEB = _kweb()

_KBUILTIN_IMPORT = __builtin__.__import__
class _KHTTPClient(asyncore.dispatcher):
  '''
  * clean name-space
    general method names starts-with-alphabet except subclass
    class-only private-methods start with _

  * handle_read does the request-processing
    + on-demand:
      - delay parsing, until required
      - exit on error, as early as possible
    + parsing-order
      requestline
       method, uri, http-version
      headers
       key: value
      body
    + module-search-order
      catchall
      hostmod
      pathmod
      self

  * catchall/host.kweb allows for single-file site hosting
  '''
  def __init__ (self, sock, clientaddr, server):
    asyncore.dispatcher.__init__ (self, sock)
    self.outgoing = collections.deque()
    self.server = server
    self.atime = time.time()
    self.data = '' #gets appended
    self.REQUEST = _KRequest(clientaddr, server, self.write)

  def write(self, hlen, hdr, clen, content, keepalive):
    '''
    called by the Request object to send data back to client
    '''
    #close file-handle of previous request, handle_close does it, but still...
    [fh.close() for (fh,n) in self.outgoing if hasattr(fh, 'close')]
    self.outgoing.clear()
    if hlen: self.outgoing.append((hlen, hdr))
    if clen: self.outgoing.append((clen, content))
    if not keepalive: self.outgoing.append((None,0))
    self.handle_write()

  #
  # BEGIN subclassing dispatcher methods
  #
  def writeable(self):
    return (self.connected) and (len(self.outgoing) > 0)

  def handle_write(self):
    '''
    outgoing[] = (data, size)
    '''
    if not self.outgoing: return
    self.atime = time.time()
    (size, data) = self.outgoing.popleft()
    #close when None is left !-)
    if (data is None) or (size < 1):
      self.handle_close()
      return
    #if data is a file handle - then read one block from fh and write to socket
    BLOCKSIZE = 1024
    if size > BLOCKSIZE: numbytes = BLOCKSIZE
    else: numbytes = size
    if hasattr(data, 'read'):
      fh = data
      try:
        sdata = fh.read(numbytes)
      except:
        self.handle_error()
        return
      #if EOF then close file-handle else appendleft for next iteration
      if len(sdata) < numbytes:
        try:
          fh.close()
        except:
          pass
        fh = None
        data = sdata
        size = numbytes = len(sdata)
    else:
      sdata = data[:numbytes]
      fh = None
    try:
      sendbytes = self.send(sdata)
    except socket.error:
      self.handle_error()
      return
    if self.server.debugfname:
      try: file(self.server.debugfname, 'ab').write(sdata)
      except: pass
    # appendleft remaining
    remaining = size-sendbytes
    if remaining > 0:
      if fh is None:
        self.outgoing.appendleft((remaining, data[sendbytes:]))
      else:
        self.outgoing.appendleft((remaining, fh))

  def handle_close(self):
    [fh.close() for (fh,n) in self.outgoing if hasattr(fh, 'close')]
    self.close()

  def handle_read(self):
    '''
    all the magic happens here ;-)

    notes:
      * partial-reads are to be handled
        - partial-request-line
        - partial-request-header
        - partial-request-body
      * while it is tempting to start request-processing on request-line/headers
        before request-body is complete
        - it complicates logic, particularly cuz. RFC allows for body even in GET ?!
        - we take the safer approach to read a complete request, before serving the response

    pndng:
      * file-upload progress
    '''
    BLOCKSIZE = 4096
    MAX_REQUEST_HEADER_SIZE = 8190 * 20 #MAX_REQUEST_LINE_SIZE * MAX_HEADER_LINES
    self.atime = time.time() #update read time - prevent socket getting closed by reaper

    try:
      data = self.recv(BLOCKSIZE)
    except socket.error, why:
      return self.handle_error()
    if 0 == len(data):
      return self.handle_close() #socket closed connection eof
    if self.server.debugfname:
      try: file(self.server.debugfname+'.response', 'ab').write(data)
      except: pass

    # BEGIN header processing
    if self.REQUEST.method is None:
      self.server.count_request()
      i = data.find('\r\n\r\n')
      if (-1 == i):
        #wait to receive complete REQUEST headers - before processing
        # not worth doing request-line processing for errors before full-headers
        #  but then, if requestline is not in first-read - something is wrong ?!
        #  what are the odds of requestline being more than 1500 bytes
        #  with a slow-writer being a "normal" http-client
        self.data += data
        if len(self.data) > (MAX_REQUEST_HEADER_SIZE):
          return self.REQUEST.sendError(413, '_KHTTPClient.MAX_REQUEST_HEADER_SIZE')
        return

      #received full-headers - start-parsing
      if (len(self.data)+i) > (MAX_REQUEST_HEADER_SIZE):
        return self.REQUEST.sendError(413, '_KHTTPClient.MAX_REQUEST_HEADER_SIZE')
      hdr = self.data + data[:i]
      data = data[i+4:] #body - will set to empty if i+4 > len(data)

      #process request-header
      if self.REQUEST._parseHeader(hdr, (len(data)>0)) is not None: return True

      if (self.REQUEST.content_length > 0):
        # safe to reuse self.data now ~ use it for body writes
        # * tempting to use cStringIO.StringIO()
        #   probably ~5% faster than TemporaryFile
        # * safer to use TemporaryFile
        #   prevents python-memory-abuse by requests ?!
        self.data = tempfile.TemporaryFile()
      else:
        self.data = None

    # note: not handling transfer-encoding chunked
    # repeat until content_length data is received
    # can do file-upload progress here
    if self.data is not None:
      self.data.write(data)
      dsize = self.data.tell()
      if dsize < self.REQUEST.content_length: return
      if dsize > self.REQUEST.content_length:
        return self.sendError(411, '_KHTTPClient.Content-Length invalid')
      self.data.seek(0)

    self.REQUEST._parseBody(self.data) #calls mods so called even if no data
    self.data = '' #so next request can be received
    return True

class _KHTTPServer(asyncore.dispatcher):
  '''
  pndng documentation
  '''
  class Session(object):
    '''
    notes:
      * needs more thought - adding persistant sessions to server - accessible to all
      * timeout
      * user IP verification
    '''
    def __init__ (self):
      self._items = {}
    def items(self):
      return self._items
    def set(self, loginid, data=None, remoteip=None, timeout=1800):
      '''
      create/overwrite a session-object
      '''
      a = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
      sid = ''.join([a[random.randint(0,(len(a)-1))] for i in xrange(7)]) #change for longer
      self._items[loginid] = (int(time.time()), sid, remoteip, timeout, data)
      return sid
    def get(self, loginid, sid, remoteip=None, doLogout=False):
      '''
      returns
        (errmsg, session-data)
      needs more documentation...
      errors 1/2 represents invalid loginid/password
      '''
      sessn = self._items.get(loginid) #lastaccess, sid, timeout, data
      if not sessn: return ('3:invalid session', None)
      if sessn[1] <> sid:  return ('4:invalid session', None)
      if (sessn[2] <> None) and (sessn[2] <> remoteip): return ('5:invalid IP', None)
      ctime = int(time.time())
      if doLogout or ((sessn[3] > 0) and ((ctime - sessn[0]) > sessn[3])):
        del self._items[loginid]
        if doLogout:
          #remove expired sessions
          for k,v in self._items.items():
            if ((ctime - v[0]) > v[3]):
              del self._items[k]
          return (None, None)
        return ('6:expired session', None)
      else:
        self._items[loginid] = (ctime, sid, remoteip, sessn[3], sessn[4])
        return (None, sessn[4])

  def __init__ (self, options, listenbacklog=1024):
    asyncore.dispatcher.__init__(self)
    self.version = 'HTTP/1.1' #know the diff. bet 1.0 and 1.1 http servers
    self.ip = options.address
    self.port = options.port
    self.requestdir = options.requestdir
    self.runas = options.runas
    self.loglevel = options.loglevel
    self.debugdir = options.debugdir
    self.timeout = options.timeout
    self.debugfname = None
    self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
    self.socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    self.set_reuse_addr()
    self.bind((self.ip, self.port))
    self.listen(listenbacklog)
    self.host = self.getsockname()[0]
    self.block_count = 0
    self.conn_count = 0
    self.request_count = 0
    self.perhost = {} #store perhost-config, sessions
    self.ipblacklist = {}
    #search path for default module import - can override default modules here
    sys.path.insert(0, self.requestdir)
    self.catchall = options.catchall
    #convinence functions
    self.hostname = socket.gethostname()
    self.fqdn = socket.getfqdn()

  def __getattr__(self, key):
    if 'debugfname' == key: return self.debugfname
    elif 'gethost' == key: return self.gethost
    elif 'loglevel' == key: return self.loglevel
    elif 'perhost' == key: return self.perhost
    elif 'runas' == key: return self.runas
    elif 'count_request' == key: return self.count_request
    elif 'ipblocklist' == key: return self.ipblocklist
    elif 'blockip' == key: return self.blockip
    elif 'clearip' == key: return self.clearip
    elif 'hostname' == key: return self.hostname
    elif 'fqdn' == key: return self.fqdn
    return asyncore.dispatcher.__getattr__(self, key)

  def count_request(self):
    self.request_count += 1

  def gethost(self, reqhost='localhost'):
    #5MB 5242880 25MB 26214400
    #loglines, logindex, session
    # 101 lines per host - adjust as reqd.
    return self.perhost.setdefault(reqhost, [[None]*101, 0, _KHTTPServer.Session()])

  def checkip(self, conn, addr):
    '''
    ip-to-be-blacklisted if too many errors
     - should err message be sent - so browsers display them or ?!
     - how long ? admin should be able to remove blocked-ip
     - admin - should keep track of ip/err-count
    '''
    if self.ipblacklist.has_key(addr[0]):
      self.block_count += 1
      try: conn.close()
      except: pass
      #log entry
      perhost = self.gethost('kweb.blockip')
      logindex = perhost[1]
      loglines = perhost[0]
      if logindex >= len(loglines): logindex = 0
      loglines[logindex] = (int(time.time()), addr[:2][0], 0, 0, 0, 'kweb', 'blockip')
      perhost[1] = logindex + 1
      if self.loglevel:
        self.log_info('%s %s BLOCKIP\n'%(addr[:2][0],time.strftime('%H:%M:%S')))
      return True
    return False

  def blockip(self, ipaddress):
    self.ipblacklist[ipaddress] = None

  def clearip(self, ipaddress):
    if ipblacklist.has_key(ipaddress):
      del self.ipblacklist[ipaddress]

  def handle_accept(self):
    try:
      conn, addr = self.accept()
    except socket.error:
      self.log_info('warning: accept() threw an exception', 'warning')
      return
    except TypeError:
      self.log_info('warning: accept() threw EWOULDBLOCK', 'warning')
      return
    if self.checkip(conn, addr): return
    self.conn_count += 1
    if self.debugdir:
      self.debugfname = os.path.join(self.debugdir, '%f.http'%self.request_count)
    try: _KHTTPClient(conn, addr, self)
    except:
      self.log_info(traceback.format_exc(), 'warning')

  def log(self, host, remoteip, rescode, reslen, reqlen, reqline):
    perhost = self.gethost(host)
    logindex = perhost[1]
    loglines = perhost[0]
    if logindex >= len(loglines): logindex = 0
    loglines[logindex] = (int(time.time()), remoteip, rescode, reslen, reqlen, reqline)
    perhost[1] = logindex + 1
    reqline = ' '.join(reqline[:2]) #cuz. reqline should contain 3 but can be 1
    if self.loglevel > 0:
      self.log_info('%8s %15s %d %9d %s %s'%(time.strftime('%H:%M:%S'),
        remoteip, rescode, reslen, host, reqline))

class _KHTTPServerTest:
  '''
  simple performance test of http-server
  '''
  def __init__(self, host='localhost', port=8010, url='/', duration=5, count=2):
    if '0.0.0.0' == host: host = 'localhost'
    if url[0] <> '/': url = '/%s'%url
    self.results = Queue.Queue()
    self.refused = 0L
    self.transferred = 0L
    self.reflock = threading.Lock()
    #execute the test on init itself ;-)
    starttime = time.time()
    self.endtime = starttime + duration
    print 'http://%s:%s%s (t=%d, n=%d)'%(host, port, url, duration, count)
    for i in xrange(count):
      threading.Thread(target=self.worker,
        args=(host, port, url.lstrip('/\\'))).start()
    while self.endtime > time.time():
      time.sleep(.1)
    r = []
    while self.results.qsize():
      r.append(self.results.get())
    rc = len(r)
    t = time.time()-starttime
    a = ['%i rps %ss (%i seconds %i requests %s)' % ((rc/t), _KWEB.strsize(int(self.transferred/t)), t, rc, _KWEB.strsize(self.transferred))]
    #late finishers
    while threading.activeCount() > 1:
      time.sleep(.1)
    r = []
    while self.results.qsize():
      r.append(self.results.get())
    if r: a.append("late finishers (%i):"%(len(r)))
    if self.refused: a.append("         Connections refused: %d"%(self.refused))
    self.str = '\n'.join(a)

  def __str__(self):
    return self.str

  def worker(self, host, port, file):
    C = 0
    D = 0
    request = 'GET /%s HTTP/1.1\r\nHost: %s\r\n\r\n'%(file, host)
    t = [time.time()]
    while time.time() < self.endtime:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      try:
        s.connect((host, port))
      except:
        C += 1
        s.close()
        continue
      t.append(time.time())
      s.sendall(request)
      t.append(time.time())
      try:
        while 1:
          _ = s.recv(65536)
          if not _:
            break
          elif len(t) == 3:
            t.append(time.time())
          D += len(_)
      except:
        pass
      s.close()
      while len(t) < 5:
        t.append(time.time())
      t2 = []
      x = t.pop(0)
      while t:
        y = t.pop(0)
        t2.append(y-x)
        x = y
      self.results.put(t2)
      t = [time.time()]
    self.reflock.acquire()
    self.refused += C
    self.transferred += D
    self.reflock.release()

#note: call to main must be after MODULE-CLASS-definition
_KSIGEXIT = False
def _krun(options):
  def _reaper():
    '''
    close idle clients - prevent socket starvation (denial of service)
    '''
    t = time.time()
    for k, v in asyncore.socket_map.items():
      if not hasattr(v, 'atime'): continue #listen-socket does not have atime
      #print 'acyncore.loop', len(asyncore.socket_map)
      if v.outgoing:
        v.handle_write()
        continue
      if (0 == v.REQUEST.TIMEOUT) or (not v.outgoing): continue
      t2 = int(t - v.atime)
      if (t2 > v.REQUEST.TIMEOUT):
        v.handle_close()
        if not options.background:
          print '%s timeout %d seconds (%d)' % (v.remoteip, t2, (len(asyncore.socket_map)-1))

  global _KSIGEXIT
  os.chdir(options.requestdir)
  s = _KHTTPServer(options)
  _KWEB.server = s #to enable modules to blockip/clear-logs/etc.
  u = g = 0
  try:
    os.umask(022) #upload files to have permission of 644
    if 1 == options.runas:
      #stat requestdir instead of sys.argv[0]; cuz. kweb can run as root !-)
      st = os.stat(options.requestdir)
      os.setegid(st.st_gid)
      g = st.st_gid
      os.seteuid(st.st_uid)
      u = st.st_uid
  except:
    pass
  if not options.background:
    t = time.strftime('%d %b %Y %H:%M:%S')
    print "%s: running kweb as %d:%d from %s on address %s port %d (%d %s)" % (t,
      u, g, options.requestdir, options.address, options.port, options.loglevel, options.debugdir)
  while asyncore.socket_map:
    try:
      asyncore.loop(timeout=2, count=9)
      if _KSIGEXIT:
        asyncore.close_all()
        if not options.background: print "SIGINT caught, shutting down."
        break
      _reaper()
    except KeyboardInterrupt:
      asyncore.close_all()
      if not options.background: print "Crtl+C pressed, shutting down."
  if not options.background:
    t = time.strftime('%d %b %Y %H:%M:%S')
    print '%s:Server handled %d connections (%d requests)' % (t, s.conn_count, s.request_count)

def _kdaemonize(run, runparams):
  def _onsignal(signum, frame):
    global _KSIGEXIT
    _KSIGEXIT = True
  try:
    #first fork
    pid = os.fork()
    if pid > 0: sys.exit(0) #exit first parent
    #decouple from parent
    os.chdir('/')
    os.setsid()
    os.umask(0)
    #second fork
    pid = os.fork()
    if pid > 0: sys.exit(0) #exit second parent
    sys.stdout.flush()
    sys.stderr.flush()
    #close all file-descriptors - use resource.getrlimit() for more precise value
    for fd in range(0, 3):
      try: os.close(fd)
      except: pass
    #open stdio handles
    if hasattr(os, "devnull"):
      os.open(os.devnull, os.O_RDWR) #stdin
    else:
      os.open('/dev/null', os.O_RDWR) #stdin
    os.dup2(0, 1) #stdout
    os.dup2(0, 2) #stderr
    signal.signal(signal.SIGHUP, _onsignal)
    run(runparams)
  except:
    pass

if __name__=="__main__":
  usage = "usage: %prog -a<address=0.0.0.0> -p<port 8010> -r<requestdir .> -o<timeout=10> -l<loglevel=2> <catchall.kweb>"
  parser = optparse.OptionParser(usage)
  parser.add_option('-a', '--address', dest='address', type='str',
                    help='Address to bind/connect to (default 0.0.0.0)', default='0.0.0.0',
                    action='store')
  parser.add_option('-p', '--port', dest='port', type='int',
                    help='Port to listen/connect on (default 8010)', default=8010,
                    action='store')
  parser.add_option('-r', '--requestdir', dest='requestdir', type='str',
                    help='Default directory to serve files from', default='',
                    action='store')
  parser.add_option('-o', '--timeout', dest='timeout', type='int',
                    help='timeout/test-duration in seconds (default 5)', default=5,
                    action='store')
  parser.add_option('-l', '--loglevel', dest='loglevel', type='int',
                    help='loglevel/test-threadcount (0 None, 1 normal, 2 short line (default 2)', default=2,
                    action='store')
  parser.add_option('-d', '--debugdir', dest='debugdir', type='str',
                    help='Directory to store all request/responses - debug', default='',
                    action='store')
  parser.add_option('-t', '--test', dest='test', type='str',
                    help='threaded test of http server at address/port using timeout-duration and loglevel-threads\n      ex. kweb7.py -t/ -alocalhost -p80 -o7 -l7', default='',
                    action='store')
  parser.add_option('-b', '--background', dest='background',
                    help='run in background/daemonize (default False)', default=False,
                    action='store_true')
  parser.add_option('-u', '--runas', dest='runas', type='int',
                    help='run http-server as user - 0 none 1 requestdir 2 module (default 1)', default=1,
                    action='store')

  options, args = parser.parse_args()
  if options.test:
    print _KHTTPServerTest(options.address, options.port, options.test, options.timeout, options.loglevel)
  else:
    cwd = os.getcwd()
    if not options.requestdir:
      options.requestdir = cwd
    else:
      if (options.requestdir[0] != '/'):
        options.requestdir = os.path.join(cwd, options.requestdir)
      if not os.path.isdir(options.requestdir): options.requestdir = cwd
    if args:
      (err, options.catchall) = _kimport(args[0])
    else:
      err = None
      options.catchall = None
    if err is not None:
      print err
    else:
      if (1 == options.background) and hasattr(os, 'fork'):
        _kdaemonize(_krun, options)
      else:
        options.background = 0 #os not having fork
        _krun(options)
