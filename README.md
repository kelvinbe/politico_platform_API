# Politico

## Introduction
 [![Coverage Status](https://coveralls.io/repos/github/kelvinbe/politico_platform_API/badge.svg)](https://coveralls.io/github/kelvinbe/politico_platform_API) [![Maintainability](https://api.codeclimate.com/v1/badges/00d23f7da810ae6b79a9/maintainability)](https://codeclimate.com/github/kelvinbe/politico_platform_API/maintainability)

### Features

1. API can create political party.
2. API can delete political party.
3. API can edit political party
4. API can get all political parties
5. API can get a specific political party
6. API can create political office
7. API can get political office
8. API can can get specific political offices


### Installing



*Step 1*

Create directory
```$ mkdir politico```
```$ cd politico```
Create and activate virtual environment
```$ virtualenv env```
```$ source env/bin/activate```
Clone the repository [```here```](git@github.com:kelvinbe/politico_platform_API.git) or 
``` git clone git@github.com:kelvinbe/politico_platform_API.git ```
Install project dependencies 
```$ pip install -r requirements.txt```
#### Storing environment variables 
```
export FLASK_APP="run.py"
export APP_SETTINGS="development"
FLASK_DEBUG=1
```
*Step 2*
#### Running the application
```$ python run.py```
*Step 3*
#### Testing
```$ pytest app/tests```
### API-Endpoints
#### Parties Endpoints : /api/v1/
Method | Endpoint | Functionality
--- | --- | ---
POST | /parties| Create politiical parties
GET | /parties/int:id | Get single political party
GET | /parties | Get  all political parties
PATCH | /parties| Edit a political party
DELETE|/parties| Delete a political party
#### Offices Endpoints : /api/v1/
Method | Endpoint | Functionality
--- | --- | ---
POST |/offices | Create an office
GET |/offices | Get all offices
GET |/offices/int:id | Get a specific office
