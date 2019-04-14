import sys
import time
import json
import requests

def get_tweet(req_next):
    body = { "maxResults": 100, "query": "#ServicioPublico" }

    if req_next:
        body['next'] = req_next

    result = requests.post("https://api.twitter.com/1.1/tweets/search/30day/c4v.json", headers={"Content-Type": "application/json", "Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAAK2T9wAAAAAAp0w7aLB7A6PxNfqg%2Bpho6KtEgBY%3DPxTLZ7YBPMfa199padvQ2kLN8R7S0Q0MtLx6MOIgW31T5AW5sM"}, json=body)
    time.sleep(3)
    if result.ok:
        with open("../data/tweets_" + str(req_next) + ".json", 'w+') as output_file:
            print("Dumping file for index " + str(req_next))
            data = result.json()
            json.dump(data["results"], output_file)
            print("Done with file " + str(req_next))
            return data["next"]

    else:
        print(result)
        raise Exception("Something went wrong while processing " + str(req_next) + " " + str(result))



def main(req_next):
    while True:
        try:
            req_next = get_tweet(req_next)
        except:
            print("Probably being rate limited")
            time.sleep(10)
            req_next = get_tweet(req_next)

if __name__ == "__main__":
    main("eyJhdXRoZW50aWNpdHkiOiIxMmVlY2RiMWMxZTQyYzcxYWE1ODAyZTRiMTdlNmQ3Njk5NjViZGE4NDRiNjIxY2IwZWM4ZTcwODE2OGViZWIwIiwiZnJvbURhdGUiOiIyMDE5MDMxNTAwMDAiLCJ0b0RhdGUiOiIyMDE5MDQxNDE4NTkiLCJuZXh0IjoiMjAxOTA0MTQxODU5MDAtMTExNjcyMDg0OTk2MzM3NjY0MS0wIn0=")
