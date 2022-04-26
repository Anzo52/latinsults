# Latinsults
Generates insults in Latin.

## Response Codes 
### Response Codes
```
200: Success
400: Bad request
301: Moved Permanently
401: Unauthorized
404: Cannot be found
405: Method not allowed
422: Unprocessable Entity 
50X: Server Error
```
### Error Codes Details
```
100: Bad Request
110: Unauthorized
120: User Authenticaion Invalid
130: Parameter Error
140: Item Missing
150: Conflict
160: Server Error
```
### Example Error Message
```json
http code 405
{
    "code": 405,
    "message": "Method Not Allowed",
    "resolve": "The method is not allowed for the requested URL."
}
```
**Request:**
```json
GET / HTTP/1.1
Accept: application/json
Content-Type: application/json
Content-Length: xy

{
    "username": "foo",
    "password": "1234567" 
}
```
**Successful Response:**
```json
HTTP/1.1 200 OK
Server: My RESTful API
Content-Type: application/json
Content-Length: xy

{
   "apitoken": "xxxx",
   "expirationDate": "xxx"
}
```
**Failed Response:**
```json
HTTP/1.1 401 Unauthorized
Server: xxx
Content-Type: application/json
Content-Length: xy

{
    "code": xxx,
    "message": "xxx",
    "resolve": "xxx."
}
``` 

## Overview
 * overview of project goes here example...  
	- **API Features** Push notifications, link previews, new message markers, and more bring IRC to the 21st century.
	- **Always connected.** Remains connected to IRC servers while you are offline.
	- **Cross platform.** It doesn't matter what OS you use, it just works wherever Node.js runs.
	- **Responsive interface.** The client works smoothly on every desktop, smartphone and tablet.
	- **Synchronized experience.** Always resume where you left off no matter what device.
	

## Installation and usage  
* How to connect

### Swagger UI
Swagger UI is already included in this repo. For detailed instructions on how to us UI within the project refer to https://idratherbewriting.com/learnapidoc/pubapis_swagger.html

### Running stable releases  

 * running and stable releases info goes here

### Running from source  

The following commands install and run the development version of:

```sh
* git commands goes here
```


## Development setup  

Simply follow the instructions to run The project from source above, on your own
fork.
