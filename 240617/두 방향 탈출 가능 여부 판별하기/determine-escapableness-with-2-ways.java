import java.util.*;
import java.io.*;

public class Main {
    public static int n, m;
    public static int[][] grid;
    public static int[][] visited;
    public static int[] dr = {-1, 1, 0, 0};
    public static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        input();
        int answer = dfs(0, 0);
        System.out.print(answer);
    }

    public static boolean inRange(int r, int c){
        return r >= 0 && r < n && c >= 0 && c < n;
    }

    public static int dfs(int r, int c) {
        visited[r][c] = 1;
        if(r == n && c == m)
            return 1;
        
        for(int i = 0; i < 4; i++){
            int nr = r + dr[i];
            int nc = c + dc[i];

            if(!inRange(nr, nc) || grid[nr][nc] == 0 || visited[nr][nc] == 1){
                continue;
            }

            dfs(nr, nc);
        }

        return 0;
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        grid = new int[n][m];
        visited = new int[n][m];

        for(int i = 0; i < n; i++){
            int[] temp = Arrays.stream(br.readLine().split(" "))
                            .mapToInt(Integer::parseInt)
                            .toArray();
            grid[i] = temp;
        }
    }
}