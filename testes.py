import hashlib


senha = input("Digite uma senha: ")

senha = hashlib.sha256(senha.encode()).hexdigest()

print(senha)



# 03cd7125d