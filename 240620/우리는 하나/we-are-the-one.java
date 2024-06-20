import java.util.*;
import java.io.*;

public class Main {
    public static int n, k, u, d;
    public static int[][] grid;
    public static List<int[]> cities = new ArrayList<>();
    public static boolean[][] visited;
    public static int[] dr = {-1, 1, 0, 0};
    public static int[] dc = {0, 0, -1, 1};
    public static int answer = 0;

    public static void main(String[] args) throws IOException {
        input();
        findMaxCities(0, 0, new ArrayList<>());
        System.out.print(answer);
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        u = Integer.parseInt(st.nextToken());
        d = Integer.parseInt(st.nextToken());

        grid = new int[n][n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                grid[i][j] = Integer.parseInt(st.nextToken());
                cities.add(new int[]{i, j});
            }
        }
    }

    public static void findMaxCities(int start, int count, List<int[]> selectedCities) {
        if (count == k) {
            answer = Math.max(answer, calculateReachableCities(selectedCities));
            return;
        }
        for (int i = start; i < cities.size(); i++) {
            selectedCities.add(cities.get(i));
            findMaxCities(i + 1, count + 1, selectedCities);
            selectedCities.remove(selectedCities.size() - 1);
        }
    }

    public static int calculateReachableCities(List<int[]> selectedCities) {
        visited = new boolean[n][n];
        int totalReachable = 0;
        for (int[] city : selectedCities) {
            if (!visited[city[0]][city[1]]) {
                totalReachable += bfs(city[0], city[1]);
            }
        }
        return totalReachable;
    }

    public static int bfs(int r, int c) {
        Deque<int[]> queue = new ArrayDeque<>();
        queue.add(new int[]{r, c});
        visited[r][c] = true;
        int reachableCount = 1;

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int cr = current[0], cc = current[1];
            for (int i = 0; i < 4; i++) {
                int nr = cr + dr[i], nc = cc + dc[i];
                if (inRange(nr, nc) && !visited[nr][nc] && heightPossible(cr, cc, nr, nc)) {
                    visited[nr][nc] = true;
                    queue.add(new int[]{nr, nc});
                    reachableCount++;
                }
            }
        }
        return reachableCount;
    }

    public static boolean inRange(int r, int c) {
        return r >= 0 && r < n && c >= 0 && c < n;
    }

    public static boolean heightPossible(int r, int c, int nr, int nc) {
        int heightDiff = Math.abs(grid[r][c] - grid[nr][nc]);
        return heightDiff >= u && heightDiff <= d;
    }
}