from dotenv import load_dotenv
import openai
from openai import error
import os
from time import sleep, time

from elephant_news.llm.log import Log


load_dotenv()  # load the OpenAI API key from a .env file
openai.api_key = os.getenv("OPENAI_API_KEY")


# rate limiter
last_call: float = time()


def llm_api(log: Log) -> str:
    global last_call
    if time() - last_call < 1:
        sleep(1)
        last_call = time()
    model = log.model
    temperature = log.temperature
    try:
        if model in [
            "gpt-4",
            "gpt-4-0314",
            "gpt-4-32k",
            "gpt-4-32k-0314",
            "gpt-3.5-turbo",
            "gpt-3.5-turbo-0301",
        ]:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {
                        "role": m.speaker,
                        "content": m.content
                    }
                    for m in log.messages
                ],
                temperature=temperature,
                frequency_penalty=0,
                presence_penalty=0
            )
            return response.choices[0].message.content
        elif model in [
            "text-davinci-003",
            "text-davinci-002",
            "text-curie-001",
            "text-babbage-001",
            "text-ada-001",
            "davinci",
            "curie",
            "babbage",
            "ada",
        ]:
            response = openai.Completion.create(
                model=model,
                prompt="\n".join([f"{m.speaker}: {m.content}" for m in log.messages]) + "assistant: ",
                temperature=temperature,
                max_tokens=100,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
            )
            return response.choices[0].text
        else:
            return str(f"Specified unknown model {model}.")
    except error.APIConnectionError as e:
        return str(e.user_message)
