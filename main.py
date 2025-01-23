from fastapi import FastAPI

app = FastAPI()

@app.get("/api/reverse")
def reverse_text(text: str):
    reversed_text = text[::-1]
    print(f"Reversed text: {reversed_text}")
    return {"reversed": reversed_text}

@app.get("/api/disemvowel")
def disemvowel_text(text: str):
    vowels = "aeiouAEIOU"
    disemvoweled_text = ''.join([char for char in text if char not in vowels])
    print(f"Disemvoweled text: {disemvoweled_text}")
    return {"disemvoweled": disemvoweled_text}

@app.get("/api/palindrome")
def is_palindrome(text: str):
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    is_palindrome = cleaned_text == cleaned_text[::-1]
    print(f"Is palindrome: {is_palindrome}")
    return {"palindrome": is_palindrome}