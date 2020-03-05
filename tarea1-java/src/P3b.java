import java.util.Scanner;

public class P3b {

    /*
    Metodo que calcula el numero de fibonacci Fn para el indice n
     */
    private static int fib(int n) {
        if (n == 0) return 1;
        int f[] = new int[n+1];
        f[0] = f[1] = 1;
        for (int i = 2; i < n + 1; i++)  f[i] = f[i-1] + f[i-2];
        return f[n];
    }

    /*
    Este metodo entrega el indice i de la secuencia de fibonacci tal que fib(i) es el mayor numero de la secuencia
    que es menor a n
     */
    private static int fibMenorQue (int n){
        int i = 1;
        while(fib(i) < n) i++;
        return i;
    }

    /*
    Este metodo elimina el '0' en la primera posicion en caso que corresponda, y convierte el SB a String
     */
    private static String limpiar(StringBuilder code){
        if (code.charAt(0) == '0') code.deleteCharAt(0);
        return code.toString();
    }

    /*
    Metodo que retorna la "representacion fibonacci" de un entero n
     */
    private static String fibcode(int n){
        if (n == 1) return "1";
        StringBuilder code = new StringBuilder();
        for (int k = fibMenorQue(n); k > 0; k--){
            if (n >= fib(k)){
                n -= fib(k);//si n es mayor que fib(k) restarlo de n y colocar un '1' en el SB
                code.append("1");
            }else{
                code.append("0");
            }
        }
        return limpiar(code);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese un entero positivo:");
        int n = sc.nextInt();
        sc.close();
        System.out.println("fibcode(" + n + ")= " + fibcode(n));
    }

}
