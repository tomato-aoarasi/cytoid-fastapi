from typing import Annotated
from dotenv import load_dotenv
from fastapi import FastAPI,HTTPException,Depends,Header
from fastapi.security import HTTPBearer
import os,ast,json,requests
from starlette.status import HTTP_401_UNAUTHORIZED,HTTP_400_BAD_REQUEST
from gql import gql, Client
from urllib.parse import urlparse
from gql.transport.requests import RequestsHTTPTransport

app = FastAPI()
security = HTTPBearer()
load_dotenv()
tokens = os.getenv("TOKEN")
proxy_url = os.getenv("PROXY_URL")
client_ua = os.getenv("CLIENT_UA","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36")
if not tokens:
    print("No token found in .env!!!Program is stopping now!")
    exit()
token_list = ast.literal_eval(tokens)
token_dict = {value: True for value in token_list}

def get_a_RequestsHTTPTransport(url:str):
    """new a RequestsHTTPTransport object

    Args:
        url (str)

    Returns:
        RequestsHTTPTransport
    """
    # TODO:use proxy
    # session = requests.Session()
    # if proxy_url:
    #     session.proxies = {
    #         'HTTP': proxy_url,
    #         'HTTPS': proxy_url,
    #     }

    transport = RequestsHTTPTransport(
        url=url,
        use_json=True,
        
        headers={"Content-type": "application/json","User-Agent":client_ua}
    )
    
    return transport

def bearer_auth(header:str|None):
    if header == None or not header.startswith("Bearer "):
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Invalid authorization header")
    
    token = header.split(" ")[1]
    if token not in token_dict:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Unauthorized")


@app.get("/")
def read_root():
    return {"msg":"This is Cytoid-Fastapi endpoint. The docs at /docs"}


@app.get("/user/info")
async def user_info(uid:str = "",recent:int|None = None,with_bests_info:bool|None = None,authorization: Annotated[str|None,Header()] = None):
    bearer_auth(authorization)
    if uid == "":
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="uid is required")
    
    from graphql_request_context import user_info_query_without_any,user_info_query_with_recent,endpoint_graphql,endpoint_oldhttpapi,b30avg_and_r10avg_query
    
    transport = get_a_RequestsHTTPTransport(endpoint_graphql)
    client = Client(transport=transport, fetch_schema_from_transport=True)
    if(recent==None):
        query=gql(user_info_query_without_any.replace("$uid",uid))
    else:
        query=gql(user_info_query_with_recent.replace("$uid",uid).replace("$recentLimit",str(recent)))
    result = client.execute(query)
    f=json.loads(json.dumps(result))
    if not f["profile"]:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="User not found")
    
    if(recent!=None):
        for record in f["profile"]["recentRecords"]:
            score=int(record["score"])
            if(score==1000000):
                playGrade = "MAX"
            elif(1000000>score>=999000):
                playGrade = "SSS"
            elif(999000>score>=995000):
                playGrade = "SS"
            elif(995000>score>=990000):
                playGrade = "S"
            elif(990000>score>=950000):
                playGrade = "AA"
            elif(950000>score>=900000):
                playGrade = "A"
            elif(900000>score>=800000):
                playGrade = "B"
            elif(800000>score>=700000):
                playGrade = "C"
            elif(700000>score>=600000):
                playGrade = "D"
            elif(600000>score>=0):
                playGrade = "F"
            else:
                playGrade = "Null"
            record["grade"]=playGrade
    if(with_bests_info==None): with_bests_info=False
    if(with_bests_info):
        query=gql(b30avg_and_r10avg_query.replace("$uid",uid))
        result = client.execute(query)
        r=json.loads(json.dumps(result))
        
        recent_records = r['profile']['recentRecords']
        best_records = r['profile']['bestRecords']
        average_recent=average_best=0
        
        if len(recent_records)!=0:
            recent_ratings = [record['rating'] for record in recent_records]
            average_recent = sum(recent_ratings) / len(recent_ratings)
        if len(best_records)!=0:
            best_ratings = [record['rating'] for record in best_records]
            average_best = sum(best_ratings) / len(best_ratings)
        f["profile"]["best30_avg"]=average_best
        f["profile"]["recent10_avg"]=average_recent
    # get player's grade data from old api and mix it with the data from graphql
    res=requests.request("GET",endpoint_oldhttpapi.replace("$uid",uid),headers={"User-Agent":client_ua})
    res=res.json()
    f["profile"]["grade"]=res["grade"]
    return f
        