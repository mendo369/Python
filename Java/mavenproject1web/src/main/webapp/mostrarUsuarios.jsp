<%-- 
    Document   : mostrarUsuarios
    Created on : 12/10/2023, 12:25:36 p. m.
    Author     : Luis
--%>

<%@page import="java.util.List"%>
<%@page import="logica.usuario"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
    <h1>Lista De Usuarios</h1>
    
    <%
        List<usuario> usuariosList = (List) request.getSession().getAttribute("listaUsuarios");

        int cont = 1;
        for (usuario usu : usuariosList) {
    %>
    <p><b>Usuarios N° <%=cont%></b></p>
    <p>DNI: <%=usu.getDni()%></p>
    <p>Name: <%=usu.getName()%></p>
    <p>Last Name: <%=usu.getLastname()%></p>
    <p>Tel: <%=usu.getTel()%></p>
    <p>__________________________</p>
    <%
        cont++;
    }
    %>
</body>
</html>
