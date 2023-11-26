# gpt_bash
script to do bash commands with chat-gpt


Features:
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
