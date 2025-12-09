import requests

API_URL = "https://api-colombia.com/api/v1/TypicalDish"

# Función obligatoria que deben usar los tests
def dish_fetch(num):
    response = requests.get(API_URL)
    data = response.json()
    for dish in data:
        if dish.get("id") == num:
            return {
                "id": dish.get("id"),
                "name": dish.get("name"),
                "description": dish.get("description", "No disponible"),
                "ingredients": dish.get("ingredients", "No disponible")
            }
    # Si no existe el plato, devolver un diccionario con claves requeridas
    return {
        "id": num,
        "name": f"Plato {num} no encontrado",
        "description": "No disponible",
        "ingredients": "No disponible"
    }

# Mostrar bienvenida y menú
print("Bienvenido al Restaurante El Colombianito, nuestro menú disponible es:\n")

response = requests.get(API_URL)
data = response.json()

# Mostrar todos los platos disponibles con su ID y nombre
for dish in data:
    print(f"{dish.get('id')}: {dish.get('name')}")

# Pedir al usuario que elija un plato
num = int(input("\nIngresa el ID del plato que quieres ver: "))

# Llamar a dish_fetch y mostrar solo descripción e ingredientes
dish = dish_fetch(num)
print("\nInformación del plato:")
for key in ["description", "ingredients"]:
    print(f"{key.capitalize()}: {dish.get(key)}")