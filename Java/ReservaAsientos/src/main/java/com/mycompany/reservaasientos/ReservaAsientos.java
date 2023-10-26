/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.reservaasientos;

import java.util.Scanner;

/**
 *
 * @author Luis
 */
public class ReservaAsientos {

    public static void main(String[] args) {
        //bandera
        boolean bandera = false;
        
        //la entrada del usuario
        Scanner teclado = new Scanner(System.in);
        
        //fila y asiento
        int fila, asiento;
        
        //respuesta
        String respuesta;
        
        //inicialisamos los asientos
        char asientos [][] = new char[10][10];
        
        //seteamos todos los asientos como libres
        for (int f=0;f<10;f++){
            for (int c=0;c<10;c++){
                asientos[f][c]='L';
            }
        }
        
        System.out.println("Bienvenidos al sistemea de reserva de asientos");
    
        while(bandera!=true){
            System.out.println("ingrese fila y saiento a reservar");
            System.out.print("Fila entre 0 y 9: ");
            fila = teclado.nextInt();
            
            System.out.print("Asiento entre 0 y 9: ");
            asiento = teclado.nextInt();
            
            if(asientos[fila][asiento] == 'L'){
                asientos[fila][asiento] = 'X';
                System.out.println("El asiento fue reservado");
                bandera = true;
            }
            else{
                System.out.println("El asiento está ocupado");
            }
            System.out.println("¿Desea Seguir en la reserva de asientos? S:sI N:No");
            respuesta = teclado.next();
            //equalsIgnoreCase
            if(respuesta.equalsIgnoreCase("N")){
                bandera=true;
            }
        }
    }
}
