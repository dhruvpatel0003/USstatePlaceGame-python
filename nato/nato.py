import pandas as pd
data = pd.read_csv("nato_phonetic_alphabet.csv")
format_data = pd.DataFrame(data)
# print(format_data.to_dict())
data = format_data["letter"]
new_dict = {value.letter:value.code for key,value in format_data.iterrows()}
print(new_dict)

def function():
    user_input = input("Enter the name here ... ").upper()
    user = list(user_input)
# print(new_dict[user[0]])
    try:
        user_mean = [new_dict[word] for word in user]

    except KeyError:
        print("Enter the letter only!")
        function()
    else:
        print(user_mean)

function()