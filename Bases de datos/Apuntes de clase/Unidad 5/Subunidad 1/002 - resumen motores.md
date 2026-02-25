InnoDB - Cell level locking
MyISAM = row level locking

## MERGE_MYISAM = Distribuir una base de datos a lo largo
de multiples servidores
Cada servidor tiene un cacho de la base de datos

## MEMORY - Memoria RAM
Mucha más velocidad de acceso
Mucho menos espacio (en RAM que en disco duro)
Cuidado porque es volátil

## Archive - Comprimido
Comprime la información de la tabla
Ocupa menos espacio en disco
El acceso a la información es más lento que con los otros motores

## Blackhole - agujero negro
Hay ocasiones en las que necesitas tablas intermediarias para operaciones temporales
En ese caso blackhole no deja rastro

## CSV - Comma separated values
