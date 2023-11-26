from openai import OpenAI
import os
import subprocess
api = XXX
os.environ["OPENAI_API_KEY"] = api
client = OpenAI()

mes=[
        {"role": "system", "content": "You will translate my prompts into bash commands.  I just want the command string that I will put into subprocess.run in python. Remove leading and trailing ', `, and \n"}]

while True:
    prompt = input('>')
    new_prompt = {"role": "user", "content": prompt}
    mes.append(new_prompt)
    
    response = client.chat.completions.create(
      model="gpt-4-1106-preview",
      messages=mes
    )
    p = response.choices[0].message.content
    
    print('Command:', p)
    new_response = {'role': "assistant", "content": p}
    mes.append(new_response)
    
    result = subprocess.run(p, shell=True, capture_output=True, text=True)
    print(result.stdout)
    
    if result.stderr != '':
        print('Error', result.stderr)
        
