user_input=input("Enter the phrase: ")
phrase=(user_input.replace('of','')).split()
phrase=(user_input.replace('and','')).split()
acronym=""
for word in phrase:
    acronym=acronym+word[0].upper()
print(f'Acronym of {user_input} is {acronym}')