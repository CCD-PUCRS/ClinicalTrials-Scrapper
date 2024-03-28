from transformers import pipeline
from bs4 import BeautifulSoup
import wikipedia
import urllib.request
import json

context = None

# Examples
# Links: "http:www.google.com"
# Clinical Trial: "clinical heart attack"
# Wikipedia "Dinosaur"

while not context:
    print('Select a link, Clinical Trial or Wikipedia entry:')
    try:
        entry = input().strip()
        if entry.startswith('http'):
            uf = urllib.request.urlopen(entry)
            print(uf.read())
            soup = BeautifulSoup(uf.read(), 'html.parser')
            context = soup.find('body').get_text()
        elif entry.startswith('clinical '):
            entry = entry.split(' ')
            entry.pop(0)
            url = "https://classic.clinicaltrials.gov/api/query/full_studies?expr=" + "+".join(entry) + "&min_rnk=1&max_rnk=&fmt=json"
            uf = urllib.request.urlopen(url)
            data = json.loads(uf.read())
            context = data["FullStudiesResponse"]["FullStudies"][0]["Study"]["ProtocolSection"]["DescriptionModule"]["BriefSummary"]
        else:
            context = wikipedia.page(entry).content
    except Exception:
        print('Not found, try again.')

print(context)

model_name = 'deepset/roberta-base-squad2'
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)

while True:
    print('Make your question:')
    question = input()
    response = nlp({'context': context, 'question': question})
    if response['score'] > 0.40:
        print(response['answer'])
    else:
        print(response)
        print('Not sure...')
