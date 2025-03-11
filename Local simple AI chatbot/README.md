#Simple AI Chatbot using ctransformers

This project is a simple chatbot powered by the Llama-2-7B model using the ctransformers library. It maintains a short conversation history to provide context and ensure concise, relevant responses.

##Features

Loads the Llama-2-7B-Chat-GGUF model using ctransformers.

Maintains a conversation history, keeping track of the last three exchanges to provide better contextual responses.

Ensures responses are short, relevant, and filtered to avoid nonsensical outputs.

Runs in an interactive loop, allowing the user to chat with the AI until they decide to exit.

##Requirements

To use this chatbot, ensure you have the following:

Python 3.x installed on your system.

The ctransformers library installed.

A compatible Llama-2-7B-Chat-GGUF model file downloaded from Hugging Face or another trusted source.

##Installation

Install the required library:
```bash
pip install ctransformers
```

Download the model file:
You need to download the Llama-2-7B-Chat-GGUF model from Hugging Face or any other source that provides GGUF model files.

Ensure the model file path is correct:
Update the script if necessary to match the exact model filename.

Usage

To run the chatbot, execute the script:
```bash
python chatbot.py
```
Once started, the chatbot will engage in an interactive conversation where you can type in your queries, and the AI will respond accordingly.
To exit the chatbot, type any of the following: exit, quit, or bye.

Example Conversation
```bash
You: Hello!
AI: Hi! How can I help you today?

You: What's the capital of France?
AI: The capital of France is Paris.

You: exit
AI: Goodbye!
```
Customization Options

You can modify the chatbot's behavior according to your needs:

Change the AI's behavior: Modify the system_prompt string in the script to adjust the chatbot’s personality and response style.

Adjust conversation history length: The script keeps only the last three exchanges. You can change this value to keep more or less context.

Fine-tune response filtering: The script filters out responses that are too short or nonsensical. You can modify the filtering logic if needed.

##Troubleshooting

If you get an error related to loading the model, ensure the model file name and path are correct.

If the chatbot generates irrelevant or low-quality responses, consider adjusting the system_prompt to provide clearer instructions.

If performance is slow, ensure your hardware meets the requirements for running large language models efficiently.



