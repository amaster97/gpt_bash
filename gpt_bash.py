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
    """
    We always have it print out what command it directed into the python stream for debugging purposes.
    
    
    sample prompts that did well: 
    'what time is it'
    'change my directory to XXX'
    
    It can even do combo prompts:
    'make a copy of my test.txt file, then print out list of files of my directory, then print out what directory I am in'
    
    It also reasonably answers nonsense or wrong prompts by redirecting errors with shell=True
    'where is waldo'
    
    If there is an error, it will print out what the error was.
   
    We also save previous instances so it remembers.
    'make a copy of file.txt'
    'delete the file you just created'
    
    
    """
    
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
        