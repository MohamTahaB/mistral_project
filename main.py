from dotenv import load_dotenv
from colorama import Fore, Style
from mistralai import Mistral
import os
import sys


def chat_wrapper(api_key, messages):
    print(Style.BRIGHT + Fore.RED + "Mistral: " +
          Style.RESET_ALL, end="", flush=True)
    model = "mistral-large-latest"

    client = Mistral(api_key=api_key)

    stream_response = client.chat.stream(
        model=model,
        messages=messages
    )
    response = list()
    for chunk in stream_response:
        response.append(chunk.data.choices[0].delta.content)
        print(response[-1], end="", flush=True)

    print()
    return "".join(response)


def main():
    # Load .env vars
    load_dotenv()

    api_key = os.getenv("MISTRAL_API_KEY")
    if len(api_key) == 0:
        sys.exit("No api key found")

    messages_history = list()

    try:
        while True:
            print(Style.BRIGHT + Fore.GREEN + "User: " +
                  Style.RESET_ALL, end="", flush=True)
            user_input = input("")
            messages_history.append({
                "role": "user",
                "content": user_input,
            })
            response = chat_wrapper(api_key, messages_history)
            messages_history.append({
                "role": "assistant",
                "content": response,
            })
    except KeyboardInterrupt:
        print(Fore.RED + "\n### Session ended ###" + Style.RESET_ALL)


if __name__ == "__main__":
    main()
