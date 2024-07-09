import java.util.*;
import java.io.*;

public class Main {
    public static int[] dotArr;
    public static int[][] lineArr;
    public static int n, m;

    public static void main(String[] args) throws IOException {
        input();
    }

    public static int find(int start, int end, int target) {
        int l = start;
        int r = end;

        while(l <= r) {
            int mid = (l + r) / 2;
            if(mid == target){
                return 1;
            }
            if(target < mid)
                r = mid - 1;
            else
                l = mid + 1;
        }
        return 0;
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        dotArr = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

        lineArr = new int[m][2];

        for(int i = 0; i < m; i++){
            lineArr[i] = Arrays.stream(br.readLine().split(" "))
                                .mapToInt(Integer::parseInt)
                                .toArray();
            
            int start = lineArr[i][0];
            int end = lineArr[i][1];

            int cnt = 0;

            for(int target : dotArr){
                cnt += find(start, end, target);
            }
            System.out.println(cnt);
        }
    }
}