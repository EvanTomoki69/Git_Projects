#Podemos gestionar nuestros entornos mediante el listado de nuestros paquetes o librerias instalados
#Deberemos reactivar nuestro entorno virtual 
#Escribiremos pip freeze y desplegara un listado de las dependencias que instalamos y que se instalaron al momento de la creacion de nuestro ambiente 
#Por buenas practicas es aconsejable que crees un archivo para listar todos estos cambios en caso de querer reconstruir nuestro proyecto
#Esto se hace mediante pip freeze > requirements.txt
#El nombre de archivo se da por buenas practicas
#De este modo, cuando deseemos recrear un proyecto, en lugar de hacer todo el proceso manualmente, podemos ocupar el archivo requirements mediante C:...>pip install -r requirements.txt
#Recuerda siempre que al tener tu proyecto construido, haras el pip freeze, seguido del pip freeze > requirements.txt y para reconstruirlo posteriormente usaras pip install -r requirements.txt