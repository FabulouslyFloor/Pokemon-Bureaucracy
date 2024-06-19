import re

def main():    
    #r".*-" - Does the name contain a hyphen?
    #r"\w+\-(hisui|alola|galar|paldea)\.*" - Does the name contain one of these regions?
    #box = re.compile(r"\w+\-(hisui|alola|galar|paldea|mega|gmax)\.*")
    
    sentence = input("Enter a sentence: ")
    #result = box.search(sentence)
    result = sentence.find("-")
    #newString = result[0]
    print(result)
    if result == None:
        print("Your word does not match your regular expression.")
    else:
        print("Your word matches your regular expression.")
        
    
    
main()