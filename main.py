name, age, country = input("Enter your name, age, country: ").split(' ')
words = (f"Hello {name}, are you {age} years old?, what can you tell me about {country} " )
print(words)

 ###########Types of data############
 ##str = string
word = "Word"
##int = integer
number = 4
##float = decimal
decimal = 4.8
##boolean = True or False
married = True
print(f"Are you married? {married}")

promedio = float(input("Ingrese un promedio: ")) #Its important to define the type of data that the input will be
print(type(promedio))

#dictionary
address = {"Country":"Mexico", "City":"CDMX", "ZipCode": 12345}
print(address)
print(type(address))

#list
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(type(fruits))

#tuple
colors = ("red", "blue", "green")
print(colors)
print(type(colors))
#set
animals = {"dog", "cat", "bird"}
print(animals)
print(type(animals))
