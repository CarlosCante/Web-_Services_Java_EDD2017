
package edd.practica2_201314448;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;


public class Graphivs {
    
    public void CargarDatosLista(String Datos) throws IOException{
    String ruta = "C:\\prueba\\Lista.txt";
        File archivo = new File(ruta);
        BufferedWriter bw;
           if(archivo.exists()) {
            bw = new BufferedWriter(new FileWriter(archivo));
            bw.write(Datos);
        } else {
            bw = new BufferedWriter(new FileWriter(archivo));
            bw.write(Datos);
        }
        bw.close();
        graficarLista();
    }
    
     public void CargarDatosCola(String Datos) throws IOException{
    String ruta = "C:\\prueba\\Cola.txt";
        File archivo = new File(ruta);
        BufferedWriter bw;
           if(archivo.exists()) {
            bw = new BufferedWriter(new FileWriter(archivo));
            bw.write(Datos);
        } else {
            bw = new BufferedWriter(new FileWriter(archivo));
            bw.write(Datos);
        }
        bw.close();
        graficarCola();
    }
     
      public void CargarDatosPila(String Datos) throws IOException{
    String ruta = "C:\\prueba\\Pila.txt";
        File archivo = new File(ruta);
        BufferedWriter bw;
           if(archivo.exists()) {
            bw = new BufferedWriter(new FileWriter(archivo));
            bw.write(Datos);
        } else {
            bw = new BufferedWriter(new FileWriter(archivo));
            bw.write(Datos);
        }
        bw.close();
        graficarPila();
    }
    
    
 public void graficarLista(){
 
    try {
      
      String dotPath = "C:\\Program Files (x86)\\Graphviz2.38\\bin\\dot.exe";
      System.out.println("Hola Mundo");
      String fileInputPath = "C:\\prueba\\Lista.txt";
      String fileOutputPath = "C:\\prueba\\Lista.jpg";
      
      String tParam = "-Tjpg";
      String tOParam = "-o";
        
      String[] cmd = new String[5];
      cmd[0] = dotPath;
      cmd[1] = tParam;
      cmd[2] = fileInputPath;
      cmd[3] = tOParam;
      cmd[4] = fileOutputPath;
                  
      Runtime rt = Runtime.getRuntime();
      
      rt.exec( cmd );
      
    } catch (Exception ex) {
      ex.printStackTrace();
        System.out.println(ex);
    } finally {
    }
 }   
 public void graficarCola(){
 
    try {
      
      String dotPath = "C:\\Program Files (x86)\\Graphviz2.38\\bin\\dot.exe";
      System.out.println("Hola Mundo");
      String fileInputPath = "C:\\prueba\\Cola.txt";
      String fileOutputPath = "C:\\prueba\\Cola.jpg";
      
      String tParam = "-Tjpg";
      String tOParam = "-o";
        
      String[] cmd = new String[5];
      cmd[0] = dotPath;
      cmd[1] = tParam;
      cmd[2] = fileInputPath;
      cmd[3] = tOParam;
      cmd[4] = fileOutputPath;
                  
      Runtime rt = Runtime.getRuntime();
      
      rt.exec( cmd );
      
    } catch (Exception ex) {
      ex.printStackTrace();
        System.out.println(ex);
    } finally {
    }
 } 
 public void graficarPila(){
 
    try {
      
      String dotPath = "C:\\Program Files (x86)\\Graphviz2.38\\bin\\dot.exe";
      System.out.println("Hola Mundo");
      String fileInputPath = "C:\\prueba\\Pila.txt";
      String fileOutputPath = "C:\\prueba\\Pila.jpg";
      
      String tParam = "-Tjpg";
      String tOParam = "-o";
        
      String[] cmd = new String[5];
      cmd[0] = dotPath;
      cmd[1] = tParam;
      cmd[2] = fileInputPath;
      cmd[3] = tOParam;
      cmd[4] = fileOutputPath;
                  
      Runtime rt = Runtime.getRuntime();
      
      rt.exec( cmd );
      
    } catch (Exception ex) {
      ex.printStackTrace();
        System.out.println(ex);
    } finally {
    }
 } 
}

