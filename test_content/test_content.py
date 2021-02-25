import os, json
import requests

# definition address of API
api_address = "fastapi"
# port de l'API
port = 8000

def get_request(username, password, version, sentence):
# query
    r = requests.get(
        url= f'http://{api_address}:{port}/{version}/sentiment',
        params= {
            'username': username,
            'password': password,
            'sentence': sentence
        }
    )
    return r

def get_output(username, password, version, sentence):
    request = get_request(username,password, version, sentence)
    status_code = request.status_code
    if status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
        
    output = f'''
    ============================
        Content test
    ============================

    request done at "/{version}/sentiment"
    | username= {username}
    | password= {password}
    | sentence= {sentence}

    sentiment_score = {json.loads(request.text)["score"]}

    ==>  {test_status}

    '''
    return output

# impression dans un fichier
def write_log(output):
    if os.environ.get('LOG') == '1':
        with open('/logs/api_test.log', 'a+') as file:
            file.write(output)
        
if __name__=="__main__":
    write_log(output = get_output("alice", "wonderland", "v1", "Life is beautiful"))
    write_log(output = get_output("alice", "wonderland", "v1", "That sucks"))
    write_log(output = get_output("alice", "wonderland", "v2", "Life is beautiful"))
    write_log(output = get_output("alice", "wonderland", "v2", "That sucks"))

 
        
