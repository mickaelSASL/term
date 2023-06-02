
url : https://www.lecluse.fr/blog/microbiot/

```css
/* add your css Here */
#cercle {
    width: 300px;
    height: 300px;
    border-radius:20px;
    background: green;
    position: absolute;
    top: 400px;
    left: 400px;
    z-index: 10;
}

#parent {
  position: relative;
  top: 20px;
  
}


#fond {
   position: absolute;
   top: 10px;
   left: 0px;
   z-index: 0;
}
```
```html
<div id="parent">
  
  <img id="fond" src="307.png" />
  <div id="cercle"></div>
</div>

```