import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from openai import Client
from decouple import config
from .models import WebsiteType


class WebsiteParser:

    def __init__(self, domain):
        self.link = domain

    def extract_text_from_url(self):
        response = requests.get(self.link)
        response.raise_for_status()
        html_content = response.text

        soup = BeautifulSoup(html_content, 'html.parser')

        for script_or_style in soup(['script', 'style']):
            script_or_style.decompose()

        text = soup.get_text(' ')

        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        readable_text = '\n'.join(chunk for chunk in chunks if chunk)

        return readable_text

    def extract_type(self, extracted_page_text):
        client = Client(api_key=config("OPENAI_API_KEY"))

        website_types = list(map(lambda x: {
            "id": x.id,
            "type": x.title,
            "description": x.description,
        }, WebsiteType.objects.all()))

        messages = [
            {
                "role": "system",
                "content":
                    f"You are given a parsed website ({self.extract_netloc()}) page data. "
                    "Using this data and website domain, "
                    "you must specify this website's type from among given website types. "
                    "You must only respond with an id of the type and not any other text. "
                    "If no given website type suits that data, respond with the type id -1. "
                    f"< PAGE DATA STARTS >{extracted_page_text}< PAGE DATA ENDS >"
                    f"< WEBSITE TYPES STARTS >{website_types}< WEBSITE TYPES ENDS >"
            }
        ]

        chat_completion = client.chat.completions.create(
            messages=messages,
            model="gpt-4o",
        )

        print(chat_completion)
        return chat_completion.choices[0].message.content

    def extract_netloc(self):
        return urlparse(self.link).netloc