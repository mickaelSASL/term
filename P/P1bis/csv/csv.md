==! "Lecture fichier csv"

    ```{.python .extra-class #id linenums="1"}
        import csv
        with open('eggs.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                print(', '.join(row))
        Spam, Spam, Spam, Spam, Spam, Baked Beans
        Spam, Lovely Spam, Wonderful Spam
    ```


== "Ecriture fichier csv"

    ```{.python .extra-class #id linenums="1"}
        import csv
        with open('eggs.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
            spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
    ```

== "Lecture fichier csv à l'aide d'un dictionnaire"

    ```{.python .extra-class #id linenums="1"}
        import csv
        with open('names.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row['first_name'], row['last_name'])

        Eric Idle
        John Cleese
    ```

    ```{.python .extra-class #id linenums="1"}
        >>> print(row)
        {'first_name': 'John', 'last_name': 'Cleese'}
    ```

== "Ecriture fichier csv à l'aide d'un dictionnaire"

    ```{.python .extra-class #id linenums="1"}
        import csv

        with open('names.csv', 'w', newline='') as csvfile:
            fieldnames = ['first_name', 'last_name']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
            writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
            writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
    ```


Exemples issus de la <a href="https://docs.python.org/fr/3/library/csv.html" target="_blank">documentation python
https://icons.iconarchive.com/icons/icons8/windows-8/24/Programming-External-Link-icon.png)</a><br>