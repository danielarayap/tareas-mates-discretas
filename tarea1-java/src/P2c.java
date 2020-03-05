import java.util.Scanner;

public class P2c{

    /*
    Este metodo recibe un matriz y la entrega invertida, es decir, si m(i,j)=1 entonces matrizInversa(j,i) sera 1
     */
    static private int[][] invMatrix(int[][]m){
        int[][]matInv = new int[m.length][m.length];
        for (int i = 0; i < m.length; i++)
            for (int j = 0; j < m.length; j++)
                if(m[i][j]==1)
                    matInv[j][i]=1;
        return matInv;
    }

    /*
    Este metodo compara celda a celda dos matrices de igual tamano, si ambas metrices tienen un 1 en la misma
    celda entonces el valor en esa celda de la matriz resultante es 1; en cualquier otro caso es 0.
     */
    static private int[][] intersect(int[][]a, int[][]b){
        int[][]res = new int[a.length][a.length];
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < a.length; j++) {
                if (a[i][j]==1 && b[i][j]==1)
                    res[i][j] = 1;
            }
        }
        return res;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese el tamano del conjunto:");
        int n = sc.nextInt();
        int [][] matrix = new int[n][n];
        System.out.println("Ingrese relacion de seudo-orden (matriz):");
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                matrix[i][j] = sc.nextInt();
            }
        }
        sc.close();
        System.out.println();
        int[][]res = intersect(matrix, invMatrix(matrix));//intersecta la matriz con su inverso
        System.out.println("Mayor relacion de equivalencia=");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(res[i][j]);
            }
            System.out.println();
        }
    }

}
