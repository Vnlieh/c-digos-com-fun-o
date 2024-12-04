def casa():

    home = input("Digite um nome:")
    match home:
        case "harry potter"|"hermione granger"|"rony weasley":
            print("grifinória")
        case "draco malfoy":
            print("sonserina")
        case "luna lovegood":
            print("corvinal")
        case "cedric diggory":
            print("lufa-lufa")
        case _:
            print("personagem não encontrado")

casa()