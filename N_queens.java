import java.util.Scanner;

public class N_queens{
    static int count = 0;

    static boolean isSafe(char[][] board, int row, int col, int n) {
        for (int i = 0; i < row; i++) {
            if (board[i][col] == 'Q') {
                return false;
            }
        }

        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] == 'Q') {
                return false;
            }
        }

        for (int i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++) {
            if (board[i][j] == 'Q') {
                return false;
            }
        }

        return true;
    }

    static void solve(char[][] board, int row, int n, char[][][] solutions) {
        if (row == n) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    solutions[count][i][j] = board[i][j];
                }
            }
            count++;
            return;
        }

        for (int col = 0; col < n; col++) {
            if (isSafe(board, row, col, n)) {
                board[row][col] = 'Q';
                solve(board, row + 1, n, solutions);
                board[row][col] = '.';
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the value of N: ");
        int n = sc.nextInt();

        if (n <= 0) {
            System.out.println("N must be greater than 0.");
            sc.close();
            return;
        }

        char[][] board = new char[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                board[i][j] = '.';
            }
        }

        int maxSolutions = 1;
        for (int i = 1; i <= n; i++) {
            maxSolutions *= i;
        }

        char[][][] solutions = new char[maxSolutions][n][n];

        solve(board, 0, n, solutions);

        System.out.println("Total Solutions: " + count);

        for (int k = 0; k < count; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    System.out.print(solutions[k][i][j]);
                }
                System.out.println();
            }
            System.out.println();
        }

        sc.close();
    }
}
