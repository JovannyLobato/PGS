import java.util.Scanner;

public class CasoDeUsoEstrella {   
    
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        Entrada enter = new Entrada();
        int opcion;
        do {
            System.out.println("\nSistema de Registro de Entradas - PGS");
            System.out.println("1. Registrar entrada de nino");
            System.out.println("2. Mostrar lista de entradas");
            System.out.println("3. Salir");
            System.out.print("Seleccione una opcion: ");
            
            opcion = scanner.nextInt();
            scanner.nextLine(); // Limpiar buffer

            switch (opcion) {
                case 1:
                    enter.registrarEntrada();
                    break;
                case 2:
                    enter.mostrarListaEntradas();
                    break;
                case 3:
                    System.out.println("Saliendo del sistema...");
                    break;
                default:
                    System.out.println("Opción no válida. Intente nuevamente.\n");
            }
        } while (opcion != 3);
    }
}