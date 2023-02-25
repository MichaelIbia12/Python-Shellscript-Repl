import os
#import pyttsx3
import webbrowser
import time 

settings = {
    "responseTime": 0,
    "searchEngine": "http://www.google.com"
}

_main_memory = []
COMMAND_REFRENCE = [
    "open",
    "quit",
    "search",
    "help",
    "cl",
    "-m-memory.",
    "print",
    "settings"
]
def response(text:str, command:str):
        #engine = pyttsx3.init()
        print(command + " "+ text) 
        #engine.say(command +" "+text)
        #engine.runAndWait()

def handle_open(input:str):
    response(input, "opening")
    
    if os.system(input):
        os.system("microsoft"+input)
    

def handle_quit():
    print('bye')
    quit()

def handle_search(query:str):
    response(" ", "alright")
    webbrowser.open(f"{settings['searchEngine']}/search?q={query}")  

def handle_help():
    print(f"list of commands \n {COMMAND_REFRENCE}")

def handle_memory():
    for m in _main_memory:
        print(m)
        
def handle_clear():
    _main_memory.clear()

def handle_print(text:str):
    print(text)

def handle_settings():
    _settings_dicitonary_index = 0
    for items in settings:
        _settings_dicitonary_index += 1
        print(f"[{_settings_dicitonary_index}] - {items}")
    number = int(input("Pick a number -: "))
    print(f"{list(settings.keys())[number]} : {settings[list(settings.keys())[number]]}")
    
    verifictation_input = input("Do you want to change it (Y/n): ")
    if verifictation_input.lower() is y:
        new_settings = input("")
        if settings[list(settings.keys())[number]] 
             
#def handle_restart(type:str):
#    os.system(f" cmd /{type.lower()} C:/Users/Mars/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Mars/OneDrive/Documents/Language/Python/ShellProject/main.py")

def input_fun(command:str) -> list:
    global index_one
    global index_two
    index_one = 0
    index_two = 0
    _sleeptimer = 0
    if "and" in command or "then" in command:
        if "and" in command and "then" in command:
            _split_layer_one = command.split("and")
            _split_layer_two = [substring.split('then') for substring in _split_layer_one]
            for item in _split_layer_two:
                index_one += 1
                for _item_command in item:
                    index_two += 1
                    if index_two+index_one != len(_item_command)-1+len(item)-1 :
                        _sleeptimer += 2
                    else:
                        _sleeptimer = 0
                    _command  = _item_command.strip()
                    argument, *text =  _command.split()
                    arg = argument
                    txt = text
                    command_object = {
                        "_command_type": arg,
                        "_command_text":  txt
                    }
                                                            
                    # Timing function
                    _main_memory.append(command_object)
                    #print(_main_memory)
                    #return arg, txt
    if "and" in command or "then" in command:
        if "and" in command:
            _split_layer_one = command.split("and")
        else:
            _split_layer_one = command.split("then")
            

        for item in _split_layer_one:
            _sleeptimer = len(_split_layer_one) 
            _command  = item.strip()
            argument, *text =  _command.split()
            arg = argument
            txt = text
            command_object = {
                "_command_type": arg,
                "_command_text":  txt
            }
                                                    
            # Timing function
            _main_memory.append(command_object)
    else:
        command  =command.strip()
        argument, *text =  command.split()
        arg = argument
        txt = text
        command_object = {
            "_command_type": arg,
            "_command_text":  txt
        }
        _main_memory.append(command_object)
        
        return arg, txt
    
def run_command(list:list):
    for x in list:
        if x["_command_type"] in COMMAND_REFRENCE:
            command = x["_command_type"].lower()

            text = " ".join(x["_command_text"])
            match command:
                case "open":
                    handle_open(text)  
                    list.remove(x)  
                case "quit":
                    handle_quit()
                case "search":
                    handle_search(text)
                    list.remove(x)
                case "-m-memory.":
                    handle_memory()
                    list.remove(x)
                case "help":
                    handle_help()
                    print(list)
                    list.remove(x)
                case "cl":
                    handle_clear()
                    list.remove(x)
                case "print":
                    handle_print(f"-{text}")
                    list.remove(x)
                case "settings":
                    handle_settings()
                    list.remove(x)
                case _:
                    raise NotImplementedError(f"The command {command} dosen't exist")
                    list.remove(x)
        else:
            command = x["_command_type"]
            list.remove(x)           
            print(f"The command {command} dosen't exist")
        
            
    
def run():
    print("Hi my name is sirius, What can i for you \n")
    while True:
        try:
           command  = input("input:- ")
           input_fun(command)
           if len(_main_memory) != 0:
               while len(_main_memory) != 0:
                   run_command(_main_memory)
        except TypeError:
            print("error")
        except ValueError:
            print("empty string")
        except NotImplementedError:
            print("command dosen't exist")
        except KeyboardInterrupt:
            print("\n quiting program")
            quit()
        except IndexError:
            quit()
        finally:
          pass

if __name__ == "__main__":
    run()