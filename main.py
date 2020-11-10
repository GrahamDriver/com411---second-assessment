def gang():
  print("Loading gang...")
  friends=["Scooby Doo", "Shaggy Rogers", "Fred Jones", "Daphne Blake", "Velma Dinkley"]
  print(friends)
  print("...Done!")
  return(friends)

def phrases(friends):
  quotes={}
  for i in friends:
    print(f"What does {i} say?")
    quote = input()
    #print(quote)
    quotes[i] = quote
  return(quotes)

def save(quotes):
  with open("quotes.txt", "w") as f:
    for key, value in quotes.items():
      f.write(f"{key}:{value}\n")


friends=gang()
quotes=phrases(friends)
save(quotes)
print("the file contains...")
file=open("quotes.txt")
print(file.read())
file.close()