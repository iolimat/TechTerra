from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
from Fetch_Page import fetchPage
from Google_Search import *
from Fetch_Page import *
from De_duplicate import *

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to the list of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Change this to the list of allowed HTTP methods
    allow_headers=["*"],  # Change this to the list of allowed HTTP headers

)

class UserInput(BaseModel):
    context:str


client = OpenAI(api_key='sk-proj-bAs3yyVgvjmfK6b5rDGbT3BlbkFJao9wD6SjpMYhoIPclUKX')

system_message = '''
You are a helpful assistant in field of data collection for artificial intelligence.
Your job is to understand the user requierment like in what filed does the data the user needs, What type of data the user need (text, video, images).
Your job is to translate the user requierment into a an understandable key words that we can base our upon.
**Return only the key words sperated by a comma.**
**Only return three key words.**
You will get a chat log as a list of dictionaries each dictionary is a turn in the converstion.
There are two rols:
1 - system: which is the large language model response.
2 - user: which is the user response.
'''

conv_log = [
     {"role": "system", "content": system_message},
     # {"role": "assistant", "content": "Developed by internal pointer team at menadevs"},
]

def home(context):
  user_input = context
  conv_log.append({"role": "user", "content": user_input })
  response = client.chat.completions.create(
  model="gpt-4-1106-preview",
  # model="gpt-4",

  messages=conv_log,
    stream = False
  )

  conv_log.append({"role": "assistant", "content": response})
  return response.choices[0].message.content

@app.post("/api/user_request", status_code=status.HTTP_202_ACCEPTED)
async def create_user_response(input: UserInput):
    # Perform validation or processing based on the user input
    print(input)
    context = input.context

    keywords = ""
    # Example: Check if the context is valid
    if not context:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Context cannot be empty")
    try:
        keywords = home(context) #gwt gbt
    except:
        raise HTTPException(code=401, detail="i am not sure")
    keywords = keywords.split(',')
    data = []
    for key in keywords:
        data.append(scrap(key))
    
    return data
    # Example: Return a response with processed data


# def process_url(url: str):
#     # Placeholder function for processing URLs
#     # Example: Fetch content from URL, analyze data, etc.
#     return f"Processed data for URL: {url}"


# @app.post("/api/extract_key_words",status_code=status.HTTP_200_OK)
# async def get_keywords(conv_log):
#     system_message = '''
#     You are a helpful assistant in field of data collection for artificial intelligence.
#     Your job is to translate the user requierment into a an understandable key words that we can base our upon.
#     Return only the key words sperated by a comma.
#     Only return three key words.
#     You will get a chat log as a list of dictionaries each dictionary is a turn in the converstion.
#     There are two rols:
#     1 - system: which is the large language model response.
#     2 - user: which is the user response.
#     '''
#     response = client.chat.completions.create(
#     model="gpt-4-1106-preview",
#     # model="gpt-4",
#     messages=[
#         {"role": "system", "content": system_message},
#         {"role": "user", "content": conv_log},
#     ],
#     stream = False
#     )
#     # response  = response['choices'][0]['message']['content']
#     return response.choices[0].message.content

def scrap(keywords):
    query = keywords
    print(keywords)
    # num_results = int(input("Enter the number of search results to fetch: "))
    while True:
        try:
            num_results = 2
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    while True:
        try:
            num_depth = 1
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    visitedSite.clear()
    links = [(i,num_depth) for i in scrape_google_search(query,num_results)]
    collection = []

    for (link, depth) in links:
        try:
            paragraphs, pagelinks = fetchPage(link, depth)
        except Exception as e:
            continue

        paragraphs = check_similarty_between_two_collections(paragraphs, paragraphs)
        collection = check_similarty_between_two_collections(collection, paragraphs)

        if pagelinks != None:
            for i in pagelinks:
                links.append((i,depth-1))
                
    return {"mylist" : collection}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0",port=8000)
