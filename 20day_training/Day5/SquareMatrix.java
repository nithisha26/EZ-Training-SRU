public class SquareMatrix {
    public static void main(String[] args) {
        int n = 5; // Change this to your desired matrix size
        int[][] mat = generateSpiralMatrix(n);

        // Print the generated matrix
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(mat[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static int[][] generateSpiralMatrix(int n) {
        int[][] sq = new int[n][n];
        return fillSpiral(sq, n, n / 2, n - 1, 1);
    }

    public static int[][] fillSpiral(int[][] sq, int n, int i, int j, int num) {
        if (num > (n * n)) {
            return sq;
        }

        if (i <0 && j == n) {
            i = 0;
            j = n - 2;
        } else {
            if (i <0) {
                i = n - 1;
            }
            if (j == n) {
                j = 0;
            }
        }

        if (sq[i][j]!=0) {
            i = i + 1;
            j = j - 2;
            return fillSpiral(sq,n,i,j,num);
        }

        sq[i][j] = num;
        return fillSpiral(sq, n, i - 1, j + 1, num + 1);
    }
}
