from ddgs import DDGS

def search(query:str) ->str:
    """
        You are a fn tool used as search engine like google if the agent dont know the answer u search the web and give the answer to it  
        You will get a string query as the input it is the question that is asked by the user
        You need to return a string after using DDGS with query as a parameter
    """
    return str(DDGS().text(query,maxresult=3))