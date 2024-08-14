#Biopython, NLTK, custom_function
from pmParse import get_key, pmParse, score_sentences, place_tboxes
from requests_toolbelt import MultipartDecoder
#Base Packages
import base64
import urllib.parse
import json

with open("index.html", 'r') as file:
    html = file.read()


def lambda_handler(event, context):
    flag = 0
    try:
        z = event["requestContext"]["http"]["method"]
        flag = 1
    except:
        print("Event is irregular")
    finally:
        if flag == 1:
            if z == "POST":
                headers = event['headers']
                # decode the multipart/form-data request
                postdata = base64.b64decode(event['body'])
                request = {} # Save request here
                for part in MultipartDecoder(postdata, headers['content-type']).parts:
                    decoded_header = part.headers[b'Content-Disposition'].decode('utf-8')
                    key = get_key(decoded_header)
                    request[key] = part.content
                for k,v in request.items():
                    request[k] = v.decode("utf-8")
                out = pmParse(database=request["db"],query=request["query"],rmax=request["rmax"],sort=request["sort"],n_sent=request["n_sent"])
                
                if isinstance(out, tuple):
                    rehtml = place_tboxes(html,out[0],out[1],meta=[request["query"],request["db"]])
                else:
                    rehtml = html.replace('{replaceme}', out)
                    
                response = {
                    "statusCode": 200,
                    "body": rehtml,
                    "headers": {
                        'Content-Type': 'text/html',
                    }
                }
            else:
                rehtml = html.replace('{replaceme}',z)
                response = {
                    "statusCode": 201,
                    "body": rehtml,
                    "headers": {
                        'Content-Type': 'text/html',
                    }
                }
        else:
            response = {
                "statusCode": 202,
                "body": html,
                "headers": {
                    'Content-Type': 'text/html',
                }
            }
        return(response)