print("Hola mundo desde GitHub")

password = int(input("Introdce tu contraseña: "))

passwordBase = {123: "José", 456: "María", 789: "Pedro"}

if password in passwordBase:
    print(f"Bienvenido {passwordBase[password]}")