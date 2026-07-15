import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    history = []
    turn_count = 1
    print('Type exit to quit')
    personality_chosse = input("plesae choose the AI personality")
    system_message = f"Your name is xxoxo.{personality_chosse}."
    while True:
        user_input = input(f'[Turn({turn_count})]you:>> ')
        
        if user_input.lower() == 'exit':
            break
            
        if user_input.lower() == 'reset':
            history = []
            turn_count = 1
            print("Conversation history cleared. Starting fresh!")
            continue
            
        history.append({'role': 'user', 'content': user_input})
        response = client.messages.create(
            model='claude-3-5-haiku-20241022',
            max_tokens=300,
            temperature=0.7,
            system=system_message,
            messages=history
        )
        reply = response.content[0].text
        print(f'Claude: {reply}')
        history.append({'role': 'assistant', 'content': reply})
        turn_count += 1

run_chat()