import os
import requests

# definition address of API
api_address = "fastapi"
# port de l'API
port = 8000

def get_request(username, password, version):
# query
    r = requests.get(
        url= f'http://{api_address}:{port}/{version}/sentiment',
        params= {
            'username': username,
            'password': password,
            'sentence':" "
        }
    )
    return r

def get_output(username, password, version, expected):
    request = get_request(username,password, version)
    status_code = request.status_code
    if status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
        
    output = f'''
    ============================
        Authorization test
    ============================

    request done at "/{version}/sentiment"
    | username={username}
    | password="{password}
    | sentence=" "

    expected result = {expected}
    actual restult = {status_code}

    ==>  {test_status}

    '''
    return output

# impression dans un fichier
def write_log(output):
    if os.environ.get('LOG') == '1':
        with open('/logs/api_test.log', 'a+') as file:
            file.write(output)
        
if __name__=="__main__":
    write_log(output = get_output("alice", "wonderland", "v1", 200))
    write_log(output = get_output("alice","wonderland", "v2", 200))
    write_log(output = get_output("bob", "builder", "v1", 200))
    write_log(output = get_output("bob","builder", "v2", 200))
        
