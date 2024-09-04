import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
merged_nato = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()
nato_word = [merged_nato[letter] for letter in word]
print(nato_word)
