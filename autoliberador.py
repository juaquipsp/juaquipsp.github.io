version_actual = "6.7"
import colorama
from colorama import Fore, Style, Back
import time
import os
import sys
import requests
def limpiar_pantalla():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')
# Inicializar colorama
colorama.init(autoreset=True)
limpiar_pantalla()
print(Fore.CYAN + Style.BRIGHT + Back.BLACK + "=" * 60)
print(Fore.YELLOW + Style.BRIGHT + "Bienvenid@ a Autoliberador PSP V6 JuaquiSoft 2024")
print(Fore.CYAN + Style.BRIGHT + Back.BLACK + "=" * 60 + "\n")

print(Fore.GREEN + Style.BRIGHT + "Estoy comprobando que tengas la última versión del Autoliberador V6")
control_version = [
        "=======================================================",
        "=======================================================",
        "======================================================="        
    ]

for control in control_version:
    print(Fore.MAGENTA + "- " + Fore.WHITE + control)
    time.sleep(0.5)



# URL del archivo que contiene la última versión
url = "https://juaquipsp.github.io/version"

# Descargar la última versión desde la URL
response = requests.get(url)

# Verificar que la solicitud fue exitosa
if response.status_code == 200:
    # Guardar el valor de la última versión en una variable y eliminar espacios en blanco
    ultima_version = response.text.strip()

    # Comparar las versiones
    if version_actual < ultima_version:
       print(Fore.CYAN + Style.BRIGHT + Back.BLACK + "Tu versión no es la última. Voy a proceder a actualizarla\n")
    else:
        print(Fore.CYAN + Style.BRIGHT + Back.BLACK + "Enhorabuena. Tienes la última versión del Autoliberador V6\n")
else:
    print("Error al descargar el archivo. Código de estado:", response.status_code)




exit()


# URLs de los archivos a descargar
url_CIPL_Flasher = {
    "ipl_update.prx": "https://juaquipsp.github.io/PSP/GAME/CIPL_Flasher/ipl_update.prx",
    "EBOOT.PBP": "https://juaquipsp.github.io/PSP/GAME/CIPL_Flasher/EBOOT.PBP",
    "kpspident.prx": "https://juaquipsp.github.io/PSP/GAME/CIPL_Flasher/kpspident.prx"
}
url_FastRecovery = {    
    "EBOOT.PBP": "https://juaquipsp.github.io/PSP/GAME/FastRecovery/EBOOT.PBP"    
}
url_PROUPDATE = {    
    "EBOOT.PBP": "https://juaquipsp.github.io/PSP/GAME/PROUPDATE/EBOOT.PBP"    
}
url_UPDATE1 = {    
    "EBOOT.PBP.part1.rar": "https://juaquipsp.github.io/PSP/GAME/UPDATE/EBOOT.PBP.part1.rar"  
}
url_UPDATE2 = {    
    "EBOOT.PBP.part2.rar": "https://juaquipsp.github.io/PSP/GAME/UPDATE/EBOOT.PBP.part2.rar"  
}
url_recovery_es = {    
    "recovery_es.txt": "https://juaquipsp.github.io/seplugins/recovery_es.txt"  
}
url_satelite_es = {    
    "satelite_es.txt": "https://juaquipsp.github.io/seplugins/satelite_es.txt"  
}
url_Standard = {    
    "Standard.pf": "https://juaquipsp.github.io/seplugins/fonts/Standard.pf"  
}
# Función para mostrar el mensaje inicial
def mostrar_mensaje():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

    print(Fore.CYAN + Style.BRIGHT + Back.BLACK + "=" * 60)
    print(Fore.YELLOW + Style.BRIGHT + "Bienvenid@ a Autoliberador PSP V6 JuaquiSoft 2024")
    print(Fore.CYAN + Style.BRIGHT + Back.BLACK + "=" * 60 + "\n")

    print(Fore.GREEN + Style.BRIGHT +
          "El procedimiento de liberacion no sobreescribe ningún archivo existente en la memoria Flash1,\n" 
          "con lo que el riesgo de brick es escaso.\n")

    print(Fore.YELLOW + Style.BRIGHT + "Recomendaciones iniciales:")

    recomendaciones = [
        "1.- La batería de la PSP debe estar al máximo de su capacidad ya que de apagarse en mitad del proceso se produciría un brick.",
        "2.- No debes apagar la PSP durante el proceso ya que se obtendría el mismo resultado que en la recomendación anterior.",
        "3.- La tarjeta de memoria de tu PSP no debe contener ningún archivo para que la liberación se realice correctamente.",
        "4.- La PSP debe estar conectada al PC mediante cable USB o lector de tarjeta y ejecutar esta aplicación en la raíz de la tarjeta de memoria."
    ]

    for recomendacion in recomendaciones:
        print(Fore.MAGENTA + "- " + Fore.WHITE + recomendacion)
        time.sleep(0.5)

    print(Fore.CYAN + "\nPulsa " + Fore.YELLOW + "Intro " + Fore.CYAN + "para continuar o " + Fore.RED + "CTRL+C " + Fore.CYAN + "para salir de la aplicación.")

# Función para limpiar la pantalla


# Función para realizar la pregunta sobre el firmware
def preguntar_firmware():
    print(Fore.CYAN + Style.BRIGHT + Back.BLACK + "=" * 60)
    print(Fore.YELLOW + "Ahora te haré unas sencillas preguntas acerca de tu PSP a fin de configurar")
    print("el autoliberador conforme a las respuestas dadas.\n")
    print(Fore.CYAN + "Indica el Firmware de tu PSP (Ajustes del Sistema - Información del Sistema):")
    print(Fore.WHITE + "1. Es 6.61")
    print("2. Es inferior a 6.61")
    
    firmware = input(Fore.GREEN + "Selecciona una opción (1 o 2): ")
    return firmware

# Función para crear estructura de carpetas y descargar archivos
def configurar_autoliberador():
    print(Fore.CYAN + Style.BRIGHT + Back.BLACK + "=" * 60)
    print(Fore.YELLOW + "Selecciona el modelo de tu PSP")
    
    print(Fore.WHITE + "1. Es una PSP modelo FAT")
    print("2. Es una PSP modelo SLIM con DataCode inferior a 8C")
    print("3. Es una PSP modelo SLIM con DataCode 8C o superior, PSP 3000, PSP GO o PSP STREET")    
    modelo = input(Fore.GREEN + "Selecciona una opción: ")
    if modelo == "1" or modelo == "2":
        base_dir = os.getcwd()    
        ruta_seplugins = os.path.join(base_dir, "seplugins")
        os.makedirs(ruta_seplugins, exist_ok=True)
        print(Fore.GREEN + "Estructura de carpetas creada en:", ruta_seplugins)
        
        for nombre, url in url_recovery_es.items():
            archivo_path = os.path.join(ruta_seplugins, nombre)
            try:
                print(Fore.CYAN + f"Descargando {nombre}...")
                respuesta = requests.get(url)
                respuesta.raise_for_status()  # Verificar si la solicitud fue exitosa
                with open(archivo_path, "wb") as archivo:
                    archivo.write(respuesta.content)
                print(Fore.GREEN + f"{nombre} descargado correctamente.")
            except Exception as e:
                print(Fore.RED + f"Error al descargar {nombre}: {e}")
        for nombre, url in url_satelite_es.items():
            archivo_path = os.path.join(ruta_seplugins, nombre)
            try:
                print(Fore.CYAN + f"Descargando {nombre}...")
                respuesta = requests.get(url)
                respuesta.raise_for_status()  # Verificar si la solicitud fue exitosa
                with open(archivo_path, "wb") as archivo:
                    archivo.write(respuesta.content)
                print(Fore.GREEN + f"{nombre} descargado correctamente.")
            except Exception as e:
                print(Fore.RED + f"Error al descargar {nombre}: {e}") 

        ruta_fonts = os.path.join(base_dir, "seplugins", "fonts")
        os.makedirs(ruta_fonts, exist_ok=True)
        print(Fore.GREEN + "Estructura de carpetas creada en:", ruta_fonts)
        for nombre, url in url_Standard.items():
            archivo_path = os.path.join(ruta_fonts, nombre)
            try:
                print(Fore.CYAN + f"Descargando {nombre}...")
                respuesta = requests.get(url)
                respuesta.raise_for_status()  # Verificar si la solicitud fue exitosa
                with open(archivo_path, "wb") as archivo:
                    archivo.write(respuesta.content)
                print(Fore.GREEN + f"{nombre} descargado correctamente.")
            except Exception as e:
                print(Fore.RED + f"Error al descargar {nombre}: {e}") 
                
        ruta_PROUPDATE = os.path.join(base_dir, "PSP", "GAME", "PROUPDATE")
        os.makedirs(ruta_PROUPDATE, exist_ok=True)
        print(Fore.GREEN + "Estructura de carpetas creada en:", ruta_PROUPDATE)

        # Descargar los archivos
        for nombre, url in url_PROUPDATE.items():
            archivo_path = os.path.join(ruta_PROUPDATE, nombre)
            try:
                print(Fore.CYAN + f"Descargando {nombre}...")
                respuesta = requests.get(url)
                respuesta.raise_for_status()  # Verificar si la solicitud fue exitosa
                with open(archivo_path, "wb") as archivo:
                    archivo.write(respuesta.content)
                print(Fore.GREEN + f"{nombre} descargado correctamente.")
            except Exception as e:
                print(Fore.RED + f"Error al descargar {nombre}: {e}")
                
        ruta_FastRecovery = os.path.join(base_dir, "PSP", "GAME", "FastRecovery")
        os.makedirs(ruta_FastRecovery, exist_ok=True)
        print(Fore.GREEN + "Estructura de carpetas creada en:", ruta_FastRecovery)

        # Descargar los archivos
        for nombre, url in url_FastRecovery.items():
            archivo_path = os.path.join(ruta_FastRecovery, nombre)
            try:
                print(Fore.CYAN + f"Descargando {nombre}...")
                respuesta = requests.get(url)
                respuesta.raise_for_status()  # Verificar si la solicitud fue exitosa
                with open(archivo_path, "wb") as archivo:
                    archivo.write(respuesta.content)
                print(Fore.GREEN + f"{nombre} descargado correctamente.")
            except Exception as e:
                print(Fore.RED + f"Error al descargar {nombre}: {e}")        
        
        ruta_CIPL_Flasher = os.path.join(base_dir, "PSP", "GAME", "CIPL_Flasher")    
        os.makedirs(ruta_CIPL_Flasher, exist_ok=True)
        print(Fore.GREEN + "Estructura de carpetas creada en:", ruta_CIPL_Flasher)
        # Descargar los archivos
        for nombre, url in url_CIPL_Flasher.items():
            archivo_path = os.path.join(ruta_CIPL_Flasher, nombre)
            try:
                print(Fore.CYAN + f"Descargando {nombre}...")
                respuesta = requests.get(url)
                respuesta.raise_for_status()  # Verificar si la solicitud fue exitosa
                with open(archivo_path, "wb") as archivo:
                    archivo.write(respuesta.content)
                print(Fore.GREEN + f"{nombre} descargado correctamente.")
            except Exception as e:
                print(Fore.RED + f"Error al descargar {nombre}: {e}")
        
        time.sleep(5)
        
        if os.name == 'posix':
            os.system('clear')
        elif os.name == 'nt':
            os.system('cls')
       ########################################################################
        #print(Fore.CYAN + Style.BRIGHT + Back.BLACK + "=" * 60)
        print(Fore.GREEN + "La tarjeta de memoria ya está preparada para comenzar con la liberacion.")
        
        print(Fore.WHITE + "1. Desconecta la PSP del PC\n2. Accede al menu Juegos de la PSP.\n3. Entra en ProUpdate e instalalo pulsando X.\n4. Cuando termine, haz lo mismo con FastRecovery.\n5. Por ultimo ejecuta CIPL_Flasher\n")
        print(Fore.GREEN + "Al tener una PSP sin Placa Maldita la liberación será permanente")
        input("Pusa Enter para salir")
    elif modelo == "3": 
        base_dir = os.getcwd()    
        ruta_seplugins = os.path.join(base_dir, "seplugins")
        os.makedirs(ruta_seplugins, exist_ok=True)
        print(Fore.GREEN + "Estructura de carpetas creada en:", ruta_seplugins)
        
        for nombre, url in url_recovery_es.items():
            archivo_path = os.path.join(ruta_seplugins, nombre)
            try:
                print(Fore.CYAN + f"Descargando {nombre}...")
                respuesta = requests.get(url)
                respuesta.raise_for_status()  # Verificar si la solicitud fue exitosa
                with open(archivo_path, "wb") as archivo:
                    archivo.write(respuesta.content)
                print(Fore.GREEN + f"{nombre} descargado correctamente.")
            except Exception as e:
                print(Fore.RED + f"Error al descargar {nombre}: {e}")
        for nombre, url in url_satelite_es.items():
            archivo_path = os.path.join(ruta_seplugins, nombre)
            try:
                print(Fore.CYAN + f"Descargando {nombre}...")
                respuesta = requests.get(url)
                respuesta.raise_for_status()  # Verificar si la solicitud fue exitosa
                with open(archivo_path, "wb") as archivo:
                    archivo.write(respuesta.content)
                print(Fore.GREEN + f"{nombre} descargado correctamente.")
            except Exception as e:
                print(Fore.RED + f"Error al descargar {nombre}: {e}") 

        ruta_fonts = os.path.join(base_dir, "seplugins", "fonts")
        os.makedirs(ruta_fonts, exist_ok=True)
        print(Fore.GREEN + "Estructura de carpetas creada en:", ruta_fonts)
        for nombre, url in url_Standard.items():
            archivo_path = os.path.join(ruta_fonts, nombre)
            try:
                print(Fore.CYAN + f"Descargando {nombre}...")
                respuesta = requests.get(url)
                respuesta.raise_for_status()  # Verificar si la solicitud fue exitosa
                with open(archivo_path, "wb") as archivo:
                    archivo.write(respuesta.content)
                print(Fore.GREEN + f"{nombre} descargado correctamente.")
            except Exception as e:
                print(Fore.RED + f"Error al descargar {nombre}: {e}") 
                
        ruta_PROUPDATE = os.path.join(base_dir, "PSP", "GAME", "PROUPDATE")
        os.makedirs(ruta_PROUPDATE, exist_ok=True)
        print(Fore.GREEN + "Estructura de carpetas creada en:", ruta_PROUPDATE)

        # Descargar los archivos
        for nombre, url in url_PROUPDATE.items():
            archivo_path = os.path.join(ruta_PROUPDATE, nombre)
            try:
                print(Fore.CYAN + f"Descargando {nombre}...")
                respuesta = requests.get(url)
                respuesta.raise_for_status()  # Verificar si la solicitud fue exitosa
                with open(archivo_path, "wb") as archivo:
                    archivo.write(respuesta.content)
                print(Fore.GREEN + f"{nombre} descargado correctamente.")
            except Exception as e:
                print(Fore.RED + f"Error al descargar {nombre}: {e}")
                
        ruta_FastRecovery = os.path.join(base_dir, "PSP", "GAME", "FastRecovery")
        os.makedirs(ruta_FastRecovery, exist_ok=True)
        print(Fore.GREEN + "Estructura de carpetas creada en:", ruta_FastRecovery)

        # Descargar los archivos
        for nombre, url in url_FastRecovery.items():
            archivo_path = os.path.join(ruta_FastRecovery, nombre)
            try:
                print(Fore.CYAN + f"Descargando {nombre}...")
                respuesta = requests.get(url)
                respuesta.raise_for_status()  # Verificar si la solicitud fue exitosa
                with open(archivo_path, "wb") as archivo:
                    archivo.write(respuesta.content)
                print(Fore.GREEN + f"{nombre} descargado correctamente.")
            except Exception as e:
                print(Fore.RED + f"Error al descargar {nombre}: {e}")
        time.sleep(5)
        limpiar_pantalla()
        print(Fore.CYAN + Style.BRIGHT + Back.BLACK + "=" * 60)
        print(Fore.GREEN + "La tarjeta de memoria ya está preparada para comenzar con la liberacion.")
        print(Fore.WHITE + "1. Desconecta la PSP del PC\n2. Accede al menu Juegos de la PSP.\n3. Entra en ProUpdate e instalalo pulsando X.\n4. Cuando termine, haz lo mismo con FastRecovery.\n")
        print(Fore.GREEN + "Al tener una PSP con Placa Maldita, cada vez que la apagues completamente, tendrás que ejecutar el archivo FastRecovery para que vuelva a tener un Custom Firmware")
        input("Pusa Enter para salir")
    else:
        print("Opción inválida")
  
# Lógica principal
try:
    mostrar_mensaje()
    input()  # Esperar a que el usuario presione Intro

    limpiar_pantalla()

    respuesta_firmware = preguntar_firmware()
    if respuesta_firmware == "1":
        limpiar_pantalla()
        configurar_autoliberador()
    elif respuesta_firmware == "2":
        limpiar_pantalla()               
        base_dir = os.getcwd()
        ruta_UPDATE = os.path.join(base_dir, "PSP", "GAME", "UPDATE")
        os.makedirs(ruta_UPDATE, exist_ok=True)
        print(Fore.GREEN + "Estructura de carpetas creada en:", ruta_UPDATE)

        # Descargar los archivos
        for nombre, url in url_UPDATE1.items():
            archivo_path = os.path.join(ruta_UPDATE, nombre)
            try:
                print(Fore.CYAN + f"Descargando {nombre}...")
                respuesta = requests.get(url)
                respuesta.raise_for_status()  # Verificar si la solicitud fue exitosa
                with open(archivo_path, "wb") as archivo:
                    archivo.write(respuesta.content)
                print(Fore.GREEN + f"{nombre} descargado correctamente.")
            except Exception as e:
                print(Fore.RED + f"Error al descargar {nombre}: {e}")
                
        for nombre, url in url_UPDATE2.items():
            archivo_path = os.path.join(ruta_UPDATE, nombre)
            try:
                print(Fore.CYAN + f"Descargando {nombre}...")
                respuesta = requests.get(url)
                respuesta.raise_for_status()  # Verificar si la solicitud fue exitosa
                with open(archivo_path, "wb") as archivo:
                    archivo.write(respuesta.content)
                print(Fore.GREEN + f"{nombre} descargado correctamente.")
            except Exception as e:
                print(Fore.RED + f"Error al descargar {nombre}: {e}")
        
        import os
        import rarfile

        # Configura la ruta a unrar.exe
        rarfile.UNRAR_TOOL = 'UnRAR.exe'

        # Rutas de los archivos RAR (usa rutas absolutas)
        part1 = "PSP/GAME/UPDATE/EBOOT.PBP.part1.rar"
        part2 = "PSP/GAME/UPDATE/EBOOT.PBP.part2.rar"

        # Carpeta de destino para descomprimir los archivos
        dest_dir = "PSP/GAME/UPDATE/"

        # Verifica la existencia de los archivos
        if not os.path.isfile(part1):
            print(f"Error: No se encontró {part1}")
        if not os.path.isfile(part2):
            print(f"Error: No se encontró {part2}")
        if not os.path.isfile(rarfile.UNRAR_TOOL):
            print(f"Error: No se encontró {rarfile.UNRAR_TOOL}")

        # Intenta descomprimir
        try:
            with rarfile.RarFile(part1) as rf:
                rf.extractall(dest_dir)
            print("Archivos descomprimidos con éxito.")
        except Exception as e:
            print(f"Ocurrió un error al descomprimir: {e}")     


        # Borrar los archivos .part.rar
        if os.path.exists(part1):
            os.remove(part1)
            print(f"{part1} ha sido borrado.")

        if os.path.exists(part2):
            os.remove(part2)
            print(f"{part2} ha sido borrado.")
        time.sleep(5)    
        limpiar_pantalla()
        print(Fore.CYAN + Style.BRIGHT + Back.BLACK + "=" * 60)
        print(Fore.GREEN + "La tarjeta de memoria está lista para actualizar al firmware 6.61")
        print("Para ello accede al menú Game de la PSP y lanza la actualización.\n")
        print("Una vez que hayas terminado, vuelve a conectar la PSP al PC y pulsa intro.\n")
        input(Fore.YELLOW + "Presiona Enter para continuar...")
        configurar_autoliberador()          
       
    else:
        print(Fore.RED + "No se realizará ninguna acción adicional para firmware inferior a 6.61.")

except KeyboardInterrupt:
    print(Fore.RED + "\nAplicación cerrada por el usuario.")
    sys.exit()
