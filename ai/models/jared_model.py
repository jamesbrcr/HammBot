from supabase import Client, create_client
from dotenv import load_dotenv
import os
import pandas as pd
import json

load_dotenv()

supabase = create_client(
    supabase_key=os.getenv("SUPABASE_SECRET_KEY"),
    supabase_url=os.getenv("SUPABASE_URL"),
)


def query_all_from_table(table_name: str):
    """Returns all data from a given table in the supabase database."""
    all_data = []
    more = True
    offset = 0
    limit = 10000
    while more:
        list = (
            supabase.table(table_name)
            .select("*")
            .range(offset, offset + limit - 1)
            .execute()
            .data
        )
        all_data.extend(list)
        offset += limit
        if len(list) < limit:
            more = False
    return all_data

def find_categories(str: input) -> list:
    """
    Finds the most relevant categories given a user query.
    """
    from dotenv import load_dotenv
    import os
    from openai import OpenAI
    import ast

    load_dotenv()
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    client = OpenAI(api_key=OPENAI_API_KEY)
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are Jared Hamm Bot, an mimic to Jared Hamm, who tends to respond to text messages in weird ways.",
            },
            {
                "role": "user",
                "content": f"""Say something funny like Jared would! make sure the main topic of the conversation is about {str}""",
            },
        ],
        temperature=0.7,
    )
    response = completion.choices[0].message.content
    print(response)

    #return ast.literal_eval(response) ... yeah idk wtf this does so hopefully its not important

    return response

find_categories("im gonna touch you jack dawson, and im gonna touch you inappropriately while we eat corned beef!")