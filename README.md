kweb:
=====
  * Asynchronous single-file python web-framework/HTTP-server;
  * outcome of several years of thoughts/experiments/experience


why:
=====
  * make simple things easy, and complicated things possible.
  * download/run/use


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
* hello

  1 liner - simplest kweb module

* txthello

  2 liner - simplest text/plain response

* auth

  HTTP Basic Authentication example

* redirect

  redirect html template - use in POST requests

* cookie

  set/get cookies

* listdir

  list directories from a different path of filesystem

* lorem

  html5 template with common tags
