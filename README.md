# Python HTTP Server
> a HTTP Server made by python, without using any external python package.
> Open your terminal & clone this repo by using git or by downloading it manually.
```bash

git clone https://github.com/anamiikajha/HTTP-Server-Py.git

```
> Then move to the project directory by using the command:
```bash
cd HTTP-Server-Py
```
> Then, finally start the server by using the command:
```bash
python server.py
```
> It'll start a server on the local network on http://localhost:8000
## ℹ️ About this project:

- HTTP-Server-Py, In this code we have:
- A http-server package which is already included in python.
- From http-server package we are importing particular sets of code and module like BaseHTTPRequestHandler,  HTTP-Server
- HTTP-Server is a built in package in python, which helps us to import a built-in server from python, without re-inventing the wheel.
- 'class handler' is a object in which we are giving argument of BaseHTTPRequestHandler which will help us to handle the user requests. In object handler we have a function of do_GET function for get request will run, when the user visits the server ip (internet protocol). In the function we have an argument named 'self' in which we have a server response of Status 200 Ok, and have a header of Content-type which corresponds to text/html which specifies the request we get is in html format. We have a 'page' variable in this function which has html code in string to show on the user request. And at last we are writing the page which is our html code stored in a string by the 'wfile.write' method in which we have a encoding of utf-8.
- ❗ This server is only meant for development usage and not for the production usage!
---
# License:
[![MIT License](https://img.shields.io/badge/license-MIT-blue)](https://github.com/anamiikajha/HTTP-Server-Py/blob/master/LICENSE)

### Author:
[@AnamiikaJha](https://github.com/anamiikajha)

### Language used in this repo:
[![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
