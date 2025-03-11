from ctransformers import AutoModelForCausalLM 


llm = AutoModelForCausalLM.from_pretrained(
    "TheBloke/Llama-2-7B-Chat-GGUF",  # Change this if your model is named differently
    model_file="llama-2-7b-chat.Q4_K_M.gguf",  # Make sure the file matches your downloaded model
    model_type="llama"
)

conversation_history = []  # Stores conversation context

def ask_ai(prompt):
    global conversation_history

    # Keep only the last 3 exchanges for better context
    conversation_history.append(f"User: {prompt}")
    if len(conversation_history) > 3:
        conversation_history = conversation_history[-3:]

    # Create a structured prompt
    system_prompt = "You are a helpful AI assistant. Keep responses short and relevant."
    full_prompt = f"{system_prompt}\n" + "\n".join(conversation_history) + "\nAI:"

    # Generate AI response
    response = llm(full_prompt, max_new_tokens=5000).strip()

    # Filter nonsense responses
    if len(response.split()) < 3:
        response = "I'm not sure what to say."

    conversation_history.append(f"AI: {response}")  # Store AI response
    return response

# Start chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("AI: Goodbye!")
        break
    response = ask_ai(user_input)
    print("AI:", response)
