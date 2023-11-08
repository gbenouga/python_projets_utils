#coding:utf-8
#!/usr/local/bin/python3
import cgitb
cgitb.enable
print("Content-type: text/html; charset=utf-8\n")

html = """<!DOCTYPE html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title></title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="">
    </head>
    <body>
        <h1>Bonjour</h1>
        <script src="" async defer></script>
    </body>
</html>"""
print(html)