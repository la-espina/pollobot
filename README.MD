Food (any product) Watcher Script 🍗
===

This is a *quickly* made, product watcher script build with [scrapy](https://scrapy.org/) framework. Basically use the search box from:
+ [Tuenvio.cu Carlos Tercero](https://www.tuenvio.com/carlos3) 
+ [Tuenvio.cu 4 Caminos](https://www.tuenvio.com/4caminos) 
+ [5ta y 42](https://https://5tay42.xetid.cu/) 

for looking up products matching with a defined keywords list. The scrapped data is exported to a (**data.jl**) file.  

---
#### Dependecies

+ scrapy
+ win10toast (Windows only)
+ telepot 
  
For installing the dependencies just run

```
pip install scrapy telepot

```

#### Runing the script

Once you have installed the dependencies, just run:

```python
python start.py

```

❗ Feel free to mod, comment, share, distribute and contribute for improvement if you want. 

*It's recommendable to run the script from cronjob or windows task manager for auto running.*

#### Telegram 
 Añadimos la conexión con un bot de Telegram y modificamos el scrapper para que buscara en todos los departamentos de las tiendas   en vez de solo palabras clave

Usamos [telepot](https://telepot.readthedocs.io/en/latest/index.html) para la interacción con telegram 

#### Para correrlo
```python
python start.py
python foodwatch/pollocubaBot.py
```

