#Crie um dicionário onde as chaves são os nomes dos contatos e os valores são tuplas
# contendo o número de telefone e o e-mail do contato. Permita que o usuário adicione novos
# contatos, visualize todos os contatos e procure por um contato específico.

#https://www.w3schools.com/python/python_lists.asp
#https://www.w3schools.com/python/python_tuples.asp
#https://www.w3schools.com/python/python_sets.asp
#https://www.w3schools.com/python/python_dictionaries.asp

lucas = (1612345, "lucas@gmail.com")
maria = (1612346, "maria@gmail.com")
pedro = (1612347, "pedro@gmail.com")

contacts = {
    "Lucas" : lucas,
    "Maria" : maria,
    "Pedro" : pedro
}
x = contacts.items()
print(x)

contactName = input("Add the name: ")
contactData = input("Add the number and email: ")


newContact = {
    contactName : contactData
}

contacts.update(newContact)

x = contacts.items()
print(x)
