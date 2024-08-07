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
        int cnt = -1;

        while(l <= r) {
            int mid = (l + r) / 2;
            if(arr[mid] == target){
                cnt = mid+1;
                break;
            }

            if(arr[mid] > target)
                r = mid - 1;
            else
                l = mid + 1;
        }
        System.out.println(cnt);
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        arr = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

        for(int i = 0; i < m; i++){
            int target = Integer.parseInt(br.readLine());
            find(target);
        }
    }
}