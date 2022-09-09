===! "T1"
    ```{.python .extra-class #id linenums="1"}
    import hello_world
    ```

=== "T2"
    ``` yaml 
    --8<-- "docs\Algo_arbres.py"

    ```


``` diagram
graph TD
    A[Hard] -->|Text| B(Round)
    B --> C{Decision}
    C -->|One| D[Result 1]
    C -->|Two| E[Result 2]
```