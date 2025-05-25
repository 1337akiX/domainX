import urllib.request
import json
import urllib.error  #Libreria para capturar diferentes errores HTTP.

link = "https://domainsdb.info/"

print("Buenas, esto es un proyecto que usa la API REST de DomainsDB, para consultar si el nombre de dominio esta en uso.")
print(f"Link: {link}\n")

Dominio = input('Introduzca el nombre del Dominio: ')

#endpoint url
url_Dominio = f"https://api.domainsdb.info/v1/domains/search?domain={Dominio}"

# Aunque no lo hemos visto en clase, uso el try y el except porque esta API, si el nombre del dominio
# no existe, urlopen, da error y te manda un 404.
try:
    with urllib.request.urlopen(url_Dominio) as datos:
        parseado = json.load(datos)

    #Este ejercicio no me funciono igual que el de open-meteo al momento de recibir lo que habia dentro
    #del diccionario parseado, asi que he usado .get(), para obtener todo lo que tiene esa "etiqueta".
    if parseado.get("domains"):
        #iteracion de veces que hay la palabra "domains".
        for dominio_info in parseado["domains"]:
            nombre = dominio_info.get("domain")
            is_dead = dominio_info.get("isDead")
            print(f"Dominio: {nombre}")
            print(f"isDead: {is_dead}\n")
    else:
        print(f"Buenas noticias!, el dominio {Dominio} no existe.")

#Cuando no se encuentra el dominio, te devuelve directamente un 404, asi que aqui lo compruebo.
except urllib.error.HTTPError as error:
    if error.code == 404:
        print(f"Buenas noticias!, el dominio {Dominio} no existe (not found, 404).")

# Otra excepcion, si por ejemplo en el dominio, le pones caracrteres que no lo reconoce, como podria ser un espacio.
except Exception as e:
    print(f"Error inesperado: {e}")

