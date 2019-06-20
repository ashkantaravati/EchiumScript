# Introduction
EchiumScript, a simple templating language useful for generating a file by combining different text files (any extension).

# Usage
To use EchiumScript, currently you need to make a directory names `src` and put a `render.ech` file under it. Also your text files should be located in the `src` directory and then the outputed file will be saved their as well. Of course you can easily change this behavior in the `echium.py` file. Then you can run `python echium.py`.

# EchiumScript Syntax
The is currently nothing supported as comments. It is also case-sensitive!

* Importing a text file: `content nameForTextFile = 'filename.extension';`
* Defining a variable: `var nameForVariable = anIntegerValue;`
* The Render Box: `render {}`
* Calling a text file: `@nameForTextFile*nameForVariable;`


# Example
Here we want to build an html file by combining two text files:
```
var xy = 20;
var y = 12;
content body = 'file.txt'
content footer = 'file2.txt'


render {
    <html>
    <body>
    @body*xy;
    @body*;
    <footer>
    @footer*y;
    </footer>
    </body>
    </html>
}
```
`@body*;` means that we want to render body here but it won't be repeated.