import java.util.*;
import java.io.*;
import java.util.stream.Collectors;

public class Main {
    public static List<Integer> list = new ArrayList<>();
    public static int n;
    public static int[][] grid;
    public static int[][] visited;
    public static int[] dr = {-1, 1, 0, 0};
    public static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException{
        input();
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(grid[i][j] == 1 && visited[i][j] == 0){
                    int temp = dfs(i, j, 1);
                    list.add(temp);
                }
            }
        }
        print();
    }

    public static void print() {
        Collections.sort(list);
        System.out.println(list.size());
        for(int i = 0; i < list.size(); i++){
            System.out.println(list.get(i));
        }
    }

    public static boolean inRange(int r, int c) {
        return r >= 0 && r < n && c >= 0 && c < n;
    }

    public static boolean canGo(int r, int c) {
        if(grid[r][c] == 0){
            return false;
        } else if(visited[r][c] == 1){
            return false;
        }
        return true;
    }

    public static int dfs(int r, int c, int nums) {
        visited[r][c] = 1;
        int people = nums;
        for(int i = 0; i < 4; i++){
            int nr = r + dr[i];
            int nc = c + dc[i];

            if(!inRange(nr, nc) || !canGo(nr, nc)){
                continue;
            }
            people = dfs(nr, nc, nums+1);
        }
        return people;
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;;
        n = Integer.parseInt(br.readLine());
        grid = new int[n][n];
        visited = new int[n][n];

        for(int i = 0; i < n; i++){
            grid[i] = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
        }
    }
}