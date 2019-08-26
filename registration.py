#!/usr/bin/python3
import cgi
print("Content-type:text/html\r\n\r\n")
print("<html><body><center>")
print("<h1>Registrazione studenti</h1>")
form = cgi.FieldStorage()

if form.getvalue("cognome") and form.getvalue("nome"):
    cognome = form.getvalue("cognome")
    nome = form.getvalue("nome")
    if form.getvalue("matricola"):
        matricola = form.getvalue("matricola")
    else:
        matricola = "N/A"
    libro = form.getvalue("libro")
    if libro == "on":
        libro = "si"
    else:
        libro = "no"
    with open("/stuff/studenti.csv", "a") as file:
        file.write(f"{cognome},{nome},{matricola},{libro}\n")
    print(f"<h4>{nome} {cognome} ({matricola}) aggiunto al registro</h4>")
else:
    print("<h3>Inserisci cognome e nome</h3>")

print("<form method='post' action='hello.py'>")
print("<p>Cognome: <input type='text' name='cognome'/></p>")
print("<p>Nome: <input type='text' name='nome'/></p>")
print("<p>Matricola: <input type='text' name='matricola'/></p>")
print("<input type='checkbox' name='libro'/>Libro")
print("<br><br><input type='submit' value='Submit'/>")
print("</form></center>")
print("</body></html>")
