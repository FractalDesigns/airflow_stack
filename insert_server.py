# Final request is returning 200 but for some reason i am unable to add server through api
import requests
import re

s = requests.Session()

params = {
    'email': 'elafrit.achraf@gmail.com',
    'password': 'postgres',
    'language': 'en',
    'internal_button': 'Login'
}



# Send the POST request with headers specifying the content type
response = s.post("http://localhost/authenticate/login", data=params,
                  headers={'Content-Type': 'application/x-www-form-urlencoded',
                           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})

# Check the response
# if response.status_code < 400:
#     print('Request was successful!')
#     # print('Response Content:', response.text)
# else:
#     print('Request failed with status code:', response.status_code)

## extract csrf token
pattern = r'csrfToken": "([^"]+)"'
match = re.search(pattern, response.text)

csrf_token = ""
if match:
    # Extract and print the CSRF token value
    csrf_token = match.group(1)
    # print(csrf_token)
else:
    print("CSRF token not found in the text.")

##############################


server_data = {
    "gid": "1",
    "name": "fromscript",
    "bgcolor": "",
    "fgcolor": "",
    "host": "postgres",
    "port": 5432,
    "db": "postgres",
    "username": "postgres",
    "role": "null",
    "connect_now": "true",
    "password": "postgres",
    "save_password": "false",
    "db_res": [],
    "use_ssh_tunnel": "false",
    "tunnel_port": 22,
    "tunnel_authentication": "false",
    "save_tunnel_password": "false",
    "connection_params": [
        {
            "name": "sslmode",
            "value": "prefer",
            "keyword": "sslmode",
            "cid": "c24"
        },
        {
            "name": "connect_timeout",
            "value": 10,
            "keyword": "connect_timeout",
            "cid": "c25"
        }
    ]
}

headers = {"X-Pga-Csrftoken": csrf_token,
           "Accept":
               "application/json, text/plain, */*",
           "Accept-Encoding":
               "gzip, deflate, br",
           "Accept-Language":
               "en-US,en",
           "Connection":
               "keep-alive",
           "Content-Length":
                "473",
           "Content-Type":
               "application/json",

           "Host":
               "localhost",
           "Origin":
               "http://localhost",
           "Referer":
               "http://localhost/browser/",
           "Sec-Ch-Ua":
               '"Chromium";v="116", "Not)A;Brand";v="24", "Brave";v="116"',
           "Sec-Ch-Ua-Mobile":
               "?0",
           "Sec-Ch-Ua-Platform":
               "Windows",
           "Sec-Fetch-Dest":
               "empty",
           "Sec-Fetch-Mode":
               "cors",
           "Sec-Fetch-Site":
               "same-origin",
           "Sec-Gpc":
               "1",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
response = s.post("http://localhost/browser/server/obj/1/", data=server_data, headers=headers)
print(response.text)