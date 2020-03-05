import java.util.Scanner;

public class P2a {

    /*
    Una relacion refleja en la representacion del enunciado puede considerarse como una matriz en la que todos
    los valores en la diagonal son 1.
     */
    private static boolean esRefleja(int[][] m, int n){
        for(int i = 0; i < n; i++){
            if(m[i][i] == 0) return false;
        }
        return true;
    }

    /*
    Una relacion transitiva se representa como una matriz R tal que si R(i,j)=1, con i!=j; y R(j,k)=1, con j!=k
    entonces R(i,k) debe ser 1
     */
    private static boolean esTransitiva(int[][] m, int n){
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if(i!=j && m[i][j]==1)
                    for (int k = 0; k < n; k++) {
                        if(j!=k && m[j][k]==1)
                            if(m[i][k]==0)
                                return false;
                    }
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese el tamano del conjunto:"); //la cantidad de filas(o columnas) de la matriz
        int n = sc.nextInt();
        int [][] m = new int[n][n];
        System.out.println("Ingrese relacion (matriz):");
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                m[i][j] = sc.nextInt();
            }
        }// guarda la matriz ingresada en m
        sc.close();
        System.out.println();
        if(esRefleja(m, n) && esTransitiva(m, n)) System.out.println("Relacion de cuasi-orden.");
        else System.out.println("Relacion no es cuasi-orden.");
    }
}
