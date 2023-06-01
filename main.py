# This is a sample Python script.
import openai as openai


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#

def ask_question(question):
    response = openai.Completion.create(
        engine='davinci-codex',  # Use the GPT-3.5 "davinci-codex" model
        prompt=question,
        max_tokens=100,  # Adjust the maximum number of tokens in the response as needed
        temperature=0.7,  # Adjust the temperature parameter for more or less randomness in the response
        n=1,  # Generate a single response
        stop=None,  # Optional stop sequence to end the response
    )
    return response.choices[0].text.strip()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    question = input("Ask a question: ")
    answer = ask_question(question)
    print("Answer:", answer)