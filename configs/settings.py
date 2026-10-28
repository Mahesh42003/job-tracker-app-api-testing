import os 

#BASE_URL=The url does not contain end-point
#which will change as per environment
#https://dev.jobtracking.com
#https://test.jobtraking.com
#https://localhost:3050/
BASE_URL=os.getenv("BASE_URL","http://localhost:3050")
DEFAULT_EMAIL="student@example1.com"
DEFAULT_PASSWORD="12345678"