<%-- 
    Document   : index
    Created on : 12/10/2023, 11:27:23 a. m.
    Author     : Luis
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <h1>Datos del Cliente</h1>
        <<form action="SvUsuarios" method="POST">
            <p><<label>DNI: </label> <input type="text" name="dni"></p>
            <p><<label>Name: </label> <input type="text" name="name"></p>
            <p><<label>Last Name: </label> <input type="text" name="lastname"></p>
            <p><<label>Tel: </label> <input type="text" name="tel"></p>
            <button type="submmit">Enviar</button>
        </form>
        
        <h1>Ver la lista de usuarios</h1>
        <<form action="SvUsuarios" method="GET">
            <button type="submit">Mostrar la lista de usuarios</button>
        </form>
        
    </body>
</html>
