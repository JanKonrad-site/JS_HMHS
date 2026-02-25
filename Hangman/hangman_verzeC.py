import random

word_list = ["camel", "baboon", "aardvark"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
gameOver = False
lives = 3


print(f"Zvolené slovo (debug): {chosen_word}")

# 1) placeholder (zatím jen ukázka, klidně ho jen vypiš)
placeholder = ""
for _ in range(word_length):
    placeholder += "_"
print("Placeholder:", placeholder)

# 2) hádání
while not gameOver:
    
    guess = input("Hádej písmeno: ").lower()

    # 3) display s písmeny a podtržítky
    display = ""
    for i in range(word_length):
        letter = chosen_word[i]
        if letter == guess or placeholder[i] == letter:
            display += letter
        else:
            display += "_"

    if guess not in chosen_word:
        lives -= 1
    if guess in display:
        print("už jsi to jednou zadal!")
        
        print("Špatně",lives)
    print("Display:", display)
    placeholder = display

    if "_" not in display:
        gameOver = True
        print("Vyhrál jsi!")
    elif lives == 0:
        print("Prohrál jsi!")
        print("Hledané slovo bylo", chosen_word)
        gameOver = True