# Portée des variables
Il est important lorsque l'on utilise des fonctions de savoir où les variables sont visibles dans le programme. Les variables créées dans une fonction restent **locales** à la fonction. C'est-à-dire qu'elles ne sont pas visibles à l'extérieur de la fonction.

```{.python .extra-class #id linenums="1"}
    from microbit import *
    >>> def ma_fonction():
    ...     x = 2
    ...     print(f"x vaut {x} dans la fonction")
    ...
    >>> ma_fonction()
    x vaut 2 dans la fonction
    >>> print(x)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    NameError: name 'x' is not defined
```

Lorsque le code de la fonction est exécuté, Python connaît le contenu de la variable `x`. Par contre, de retour dans le programme principal, elle lui est inconnue ce qui génère le message d'erreur.

De la même façon, une variable passée en argument est **locale** à la fonction:

```{.python .extra-class #id linenums="1"}
    from microbit import *
    >>> def ma_fonction(x):
    ...     print(f"x vaut {x} dans la fonction")
    ...
    >>> ma_fonction(2)
    x vaut 2 dans la fonction
    >>> print(x)
    Traceback (most recent call last):
    File "<stdin>", line 1, in ?
    NameError: name 'x' is not defined
```

Lorsqu'une variable est déclarée dans le programme principal, elle est visible dans celui-ci ainsi que dans toutes les fonctions. On a vu qu'on parlait de variable **globale** :

```{.python .extra-class #id linenums="1"}
    from microbit import *
    >>> def ma_fonction():
    ...     print(x)
    ...
    >>> x = 3
    >>> ma_fonction()
    3
    >>> print(x)
    3
```

Dans ce cas, la variable `x` est visible dans le module principal et dans toutes les fonctions du module. Toutefois, Python ne permet pas la modification d'une variable globale dans une fonction:

```{.python .extra-class #id linenums="1"}
    from microbit import *
    >>> def ma_fonction():
    ...     x = x + 1
    ...
    >>> x = 1
    >>> ma_fonction()
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 2, in fct
    UnboundLocalError: local variable 'x' referenced before assignment
```
L'erreur renvoyée montre que Python pense que `x` est une variable locale qui n'a pas été encore assignée. Si on veut vraiment modifier une variable globale dans une fonction, il faut utiliser le mot-clé `global` :

```{.python .extra-class #id linenums="1"}
    from microbit import *
    >>> def ma_fonction():
    ...     global x
    ...     x = x + 1
    ...
    >>> x = 1
    >>> ma_fonction()
    >>> x
    2
``` 
Dans ce dernier cas, le mot-clé `global` a forcé la variable `x` à être globale plutôt que locale au sein de la fonction.