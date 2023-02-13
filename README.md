# Calls API

## About
This Calls API helps create and retrieve calls.

## Created With
- Language: Python
- API Framework: FastAPI 
- Database: SQLite3
- Deployment: Render

## Usage

### Endpoint: `GET /`
*Index page*

Request format: `None`

Response body:
```json
    STATUS: 200

    {
        "detail": "This is the index page."
    }
```

### Endpoint: `POST /initiate-call`
*Create a call given a from-number and a to-number*

Request format: 
```json
    {
        "from_number": "string",
        "to_number": "string",
    }

    Example:
    {
        "from_number": "98xxxx78",
        "to_number": "87xxxx12"
    }
```

Response body:
```json
    STATUS: 201
    {
        "success": true
    }
```


### Endpoint: `GET /call-report`
*Get a list of all call records where the provided number exists in from or to column*

Request format: 
```sh
    Query parameter: phone=string

    Example:
    /call-report?phone=98xxxx78
```

Response body:
```json
    STATUS: 200
    {
        "success": true,
        "data": [
            // Call  data
        ]
    }

    Example:
    {
        "success": true,
        "data": [
                    {
                        "id": 1,
                        "from_number": "98xxxx78",
                        "to_number": "87xxxx12",
                        "start_time": "2023-02-13 04:50:18"
                    }
               ]
    }
```

## Installation

To get a local copy up and running, do the following steps:

1. Make sure to have Python>=3.7 installed on your system.
2. Clone the repo
   
   `git clone git@github.com:outoflaksh/frejun-calls-api.git`
3. Change directory into the cloned repository.
4. Create a Python Virtual Environment to install the dependencies.
   
   `python3 -m venv venv`
5. Activate the environment & install the dependencies.
   
   `pip3 install -r requirements.txt`
6. Run the development server.
   
   `uvicorn src.api:app --reload`
7. Run the production server (Requires a Unix-based OS).
   
   `chmod +x entrypoint.sh && ./entrypoint.sh`
   