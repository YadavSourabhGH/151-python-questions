# 9. Dictionary - Looks up word definitions
def lookup_word(word):
    import requests
    
    try:
        # Get definition from dictionary API
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        response = requests.get(url)
        data = response.json()
        
        # Return first definition found
        return data[0]['meanings'][0]['definitions'][0]['definition']
    except:
        return "Word not found"