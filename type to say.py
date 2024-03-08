import pyttsx3

def speak_text(text):
    say=pyttsx3.init()
    say.say(text)
    say.runAndWait()
while True:
    print("enter exit for exit")
    u_text=input("input your string :")
    
    if u_text=="exit":
        break
    else:
        speak_text(u_text)
