# KEYWORD ARGUMENTS = AN ARGUMENT PRECEDED BY An identifier
#                     helps with readability
#                     order of arguments doesn't matter

#def hello(greetings,title,first,last):
#    print(f"{greetings} {title} {first} {last}")

#hello("Hello",first="kaidehara",last="kazuha",title="Mr.")

def get_num(country,first,last):
    return f"+{country}-{first}{last}"

phone_num=get_num(country="977",first="98613",last="66712")

print(phone_num)