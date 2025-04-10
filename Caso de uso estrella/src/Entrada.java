
import java.util.ArrayList;
import java.util.Scanner;

public class Entrada {
    
 private static ArrayList<Nino> listaEntradas = new ArrayList<>();
    private static Scanner scanner = new Scanner(System.in);

    public static void registrarEntrada() {
        System.out.print("Ingrese el nombre del alumno: ");
        String nombre = scanner.nextLine();
        
        //Verifica el nombre del niño no este vacio
        if (nombre.equals("") || nombre.equals(" ")) { 
            System.out.println("El nombre del alumno esta vacio, vuelva a intentarlo");
            registrarEntrada();
        }
        
        System.out.print("Ingrese el identificador del tutor: ");
        String idTutor = scanner.nextLine();
        
        //Verifica el idTutor no este vacio
        if (idTutor.equals("") || idTutor.equals(" ")) { 
            System.out.println("El identificador del tutor esta vacio, vuelva a intentarlo");
            registrarEntrada();
        }else if (idTutor.length()<4) {
            System.out.println("El identificador del tutor es de pequeño a lo establecido(ingresa 4 digitos).");
            registrarEntrada();
        }else if (idTutor.length()>4) {
           System.out.println("El identificador del tutor es de más a lo establecido(ingresa 4 digitos).");
            registrarEntrada();
        }
        
        listaEntradas.add(new Nino(nombre, idTutor));
        System.out.println("Entrada registrada correctamente para " + nombre );
    }

    public static void mostrarListaEntradas() {
        if (listaEntradas.isEmpty()) {
            System.out.println("No hay entradas registradas.");
            return;
        }
        
        System.out.println("Lista de alumnos que ingresaron a la escuela:");
        for (Nino nino : listaEntradas) {
            System.out.println("- " + nino.nombre + " (ID Tutor: " + nino.idTutor + ")");
        }
    }   
}
