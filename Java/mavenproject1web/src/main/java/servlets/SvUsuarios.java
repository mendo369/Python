/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/JSP_Servlet/Servlet.java to edit this template
 */
package servlets;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import logica.usuario;

/**
 *
 * @author Luis
 */
@WebServlet(name = "SvUsuarios", urlPatterns = {"/SvUsuarios"})
public class SvUsuarios extends HttpServlet {

    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        List<usuario> listaUsuarios = new ArrayList<>();
        listaUsuarios.add(new usuario("1231", "Luis", "mendoza", "300"));
        listaUsuarios.add(new usuario("1232", "Luis2", "mendoza", "300"));
        listaUsuarios.add(new usuario("1233", "Luis3", "mendoza", "300"));
        listaUsuarios.add(new usuario("1234", "Luis4", "mendoza", "300"));

        HttpSession misesion = request.getSession();
        misesion.setAttribute("listaUsuarios", listaUsuarios);

        response.sendRedirect("mostrarUsuarios.jsp");
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String dni = request.getParameter("dni");
        String name = request.getParameter("name");
        String lastname = request.getParameter("lastname");
        String tel = request.getParameter("tel");

        System.out.println(dni);
        System.out.println(name);
        System.out.println(lastname);
        System.out.println(tel);

    }

    @Override
    public String getServletInfo() {
        return "Short description";
    }// </editor-fold>

}
