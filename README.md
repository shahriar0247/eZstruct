# eZstruct
<br>
Since I wanted the perfect way to print out tables in python, by not using modules, i made this<br>
I also updated it to be able to handle structs easily, coz i donno why



```py
└─$ python3 -i eZstruct.py 
>>> lol = eZstruct("4s20s")
>>> lol._pack("1)","hi")
>>> lol._pack("2)","hello")
>>> lol._pack("3)","hasdsad")
>>> lol._get()
[['1)  ', 'hi                  '], ['2)  ', 'hello               '], ['3)  ', 'hasdsad             ']]
>>> for a in lol._get():
...     print(*a)
... 
1)   hi                  
2)   hello               
3)   hasdsad    
```
if you are importing form another file
```py
form eZstruct import eZstruct
lol = eZstruct("4s20s")
```
best of luck ;)
<h2>Star this thing</h2>
