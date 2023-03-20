import openai
import re


# AI-Coder
# By @moaltaie

#######################################

# Set the OpenAI API key
openai.api_key = "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"

# Set the model engine to use
model_engine = "code-davinci-002"

# Function to convert text to a question using English interrogative expressions
def make_question(text):
    # Remove any unnecessary symbols or punctuation from the text
    text = re.sub(r'[^\w\s]', '', text)
    # Convert the text to lowercase
    text = text.lower()
    # Add the interrogative expression
    return "What is " + text + "?"

# Function to ask the question and get the answer
def ask_question(question):
    # Convert the question to the text format required by the OpenAI API
    prompt = question + "\nAnswer:"
    # Call the OpenAI API to get the answer
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    # Retrieve the answer from the response returned by the OpenAI API
    answer = response.choices[0].text.strip()
    return answer

# Start the interaction with ChatGPT
while True:
    # Get the input from the user
    input_text = input("Enter your question here: ")
    # Convert the text to a question using the make_question function defined above
    question = make_question(input_text)
    # Ask the question and get the answer using the ask_question function defined above
    answer = ask_question(question)
    # Display the answer to the user
    print(answer)

