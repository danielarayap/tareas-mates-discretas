import java.util.Scanner;

public class P1d {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("¿Cantidad de monedas?");
        int k = sc.nextInt(); // k monedas
        int [] monedas = new int [k]; //en este arreglo se guardaran los valores m1,...,mk
        int [] cantidades = new int[k]; // en este se guardará la cantidad de monedas mi necesarias para el vuelto
        monedas[0] = 1; // m1 = 1
        for (int i = 1; i < k; i++){
            System.out.println("Ingrese valor de la moneda " +(i+1));
            monedas[i]=sc.nextInt(); //se ingresan los valores m1,...mk
        }
        System.out.println("¿Vuelto?");
        int x = sc.nextInt(); //vuelto a entregar
        sc.close();
        int j =k-1;
        while (true){ //se implementa el algoritmo de la P1a
            if (x >= monedas[j]){
                cantidades[j]++;
                x -= monedas[j];
            }
            if (x < monedas [j]){
                j--;
            }
            if (x <= 0) break;
        }
        System.out.println("Respuesta:");
        for (int i = 0; i < k; i++) {
            if (cantidades[i] != 0) //imprime sólo si la cantidad no es 0
                System.out.println(cantidades[i] + " monedas de "+monedas[i]);
        }
    }
}
