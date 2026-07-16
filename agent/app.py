import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    history = []
    turn_count = 1
    print('Type exit to quit')
    role_chosse = input("plesae choose the AI role(who he is):")
    job_chosse = input("plesae choose the AI job(what he dos):")
    alwaysrule1_chosse = input("plesae choose what the AI always do rule 1/2(who he is):")
    alwaysrule2_chosse = input("plesae choose what the AI always do rule 2/2(who he is):")
    neverrule1_chosse = input("plesae choose what the AI never do(who he is):")
    #system=system_message lab 0.3=my agent loses its identity and instructions, reverting to a generic, plain AI assistant that forgets its name is "xxoxo" and that its job is to be a motivational running coach for students.
    system_message =f"""
        You are xoxo, a {role_chosse}.

        Your job is to {job_chosse}.

        Rules:
        - Always {alwaysrule1_chosse}
        - Always {alwaysrule2_chosse}
        - Never {neverrule1_chosse}

        Response format:
        - Start with a one-sentence summary of what the user said.
        - Then give your response.
        - End with one follow-up question.
        """

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
            model='claude-haiku-4-5-20251001',
            max_tokens=500,
            temperature=1,
            system=system_message,
            messages=history
        )
        reply = response.content[0].text
        print(f'Claude: {reply}')
        history.append({'role': 'assistant', 'content': reply})
        turn_count += 1

run_chat()