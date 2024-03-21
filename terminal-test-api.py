from openai import OpenAI

def print_model_options():
    print("Model Options For llama2:")
    print("meta/llama-2-70b-chat")
    print("meta/llama-2-13b-chat")
    print("meta/llama-2-7b-chat")
    print("yorickvp/llava-13b")
    print("nateraw/salmonn\n")

    print("Model Options For blackbox:")
    print("blackbox-code")
    print("blackbox-chat\n")

    print("Model Options For Rowena:")
    print("GPT-3.5")

def chat_with_ai(model):
    client = OpenAI(base_url="http://127.0.0.1:5000/api", api_key="bearer nokey")
    conversation = []  # Store conversation history

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Exiting chat.")
            break

        # Add user input to the conversation history
        conversation.append({"role": "user", "content": user_input})

        completion = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                *conversation  # Include conversation history
            ]
        )

        assistant_response = completion.choices[0].message.content

        # Add assistant response to the conversation history
        conversation.append({"role": "assistant", "content": assistant_response})

        print("Assistant:", assistant_response)

if __name__ == "__main__":
    print_model_options()
    selected_model = input("Please choose a model: ")

    if selected_model:
        chat_with_ai(selected_model)
    else:
        print("No model selected. Exiting program.")
