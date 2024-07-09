import java.util.*;
import java.io.*;

public class Main {
    public static int[] arr;
    public static int n, m;

    public static void main(String[] args) throws IOException {
        input();
    }

    public static void find(int target) {
        int l = 0;
        int r = n-1;
        int minIdx = n;

        while(l <= r) {
            int mid = (l + r) / 2;
            if(arr[mid] >= target){
                r = mid -1;
                minIdx = Math.min(minIdx, mid);
            }
            else
                l = mid + 1;
        }
        System.out.println(minIdx == n ? -1 : minIdx+1);
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        arr = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

        int[] temp = Arrays.stream(br.readLine().split(" "))
                            .mapToInt(Integer::parseInt)
                            .toArray();

        for(int t : temp) {
            find(t);
        }
    }
}