story = """In the <adjective1> land of <place>, a <animal> was feeling <emotion>. The <animal> had lost its <object>.

Suddenly, a <character> appeared. 'I will help you find your <object>,' they said.

Together, they journeyed through <terrain> and faced the <weather_condition>. Finally, they found the <object> in a <place2>. The <animal> was so <emotion2> and thanked the <character>. They lived <adverb> ever after."""

with open("story.txt", "w") as f:
    f.write(story)

with open("story.txt", "r") as f:
    story = f.read()

print(story)

start_word = "<"
end_word = ">"
start_word_index = -1

words = set()

for i, char in enumerate(story):
    if char == start_word:
        start_word_index = i

    if char == end_word and start_word_index != -1:
        word = story[start_word_index : i + 1]
        words.add(word)
        start_word_index = -1

print(words)

answers = {}

for word in words:
    answer = input("Enter the value of the " + word + ": ")
    answers[word] = answer

print(answers)

for word in words:
    story = story.replace(word, answers[word])

print(story)
