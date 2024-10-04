#Python posee un estilo de codificacion particular
#Existe una guia de estilo para poder codificar en Python de forma que nos apeguemos a ciertos estandares, este estandar de codificacion se llama PEP-8

#Las clases seguiran la nomenclatura camel case, si el nombre de la clase se conforma de dos o mas palabras las uniremos y el nombre de cada palabras sera en mayuscula
class ComputerUser():

#Cada indentacion tendra cuatro espacios de largo
     #Las variables que definamos como parametros tambien seran espaciadas para mejorar su lectura
     def __init__(self, username, password=''):
          self.username = username
          self.password = password

     def set_password(self):
          pass

#Las variables deben seguir la nomenclatura snake case, todos los nombres de las variables deben estar en minusculas y si son dos o mas nombres, vamos a unirlas por guiones bajos
tomoki_user = ComputerUser('Evan Tomoki')  #Tambien es necesario usar espacios entre variables, operadores y valores, para mejorar la legibilidad del codigo 
#Incluso entre comentarios, pues debes dejar 2 espacios en blanco cuando desees comentar una linea de tu codigo
#
#Hay que dejar un espacio de una linea, el codigo no puede quedar al ras, esto por la misma normativa de codificacion en Python