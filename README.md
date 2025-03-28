# SANmax
# Este es un Sistema de Almacenamiento Naval utilizando los MAXs para analizar las fotos de la tierra
## Problema:
###  Nuestro Sistema de Almacenamiento No funciona bien ya que las fotos que manda La UA son muchas y ninguna de repente estos saltos provocan que el Sistema no sea compatible con el lento proceso que tarda analizar las fotos los MAX
## Necesidad:
### Tenemos que crear un Sitema en python que nos resuelva las condiciones del problema. 
### Para ello los cientificos han creado el *SANmax* un programa que utiliza programacion paralela para que las imagenes sean analizadas concurentemente.
## Solucion:
### La gran solucion que encontraron los cientificos fue crear dos Mutex y utilizar hilos.
### Esto es debido a la compatibilidad que tienen los hilos en compartir memoria de cada foto que le mandemos y los Mutex para que sea eficiente el Sistema de Almacenamiento Naval y no provocar condiciones de carreara
## Funcionamiento:
### El programa es sencillo:
### va creando fotos de 5 o 1 foto por segundo en generar fotos de una forma aleatoria.
### Estas fotos pasan por un Mutex para que solo haya una foto en la SAN cada vez.
### Luego otro Mutex deja que esta imagen sea cogida solo por un Max
### Finalmente te devuelve las imagenes que fueron creadas las que estan siendo analizadas y las que ya han terminado
## link: https://github.com/Alfonso18Feb/SANmax/tree/main
