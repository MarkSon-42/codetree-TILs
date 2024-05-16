import java.util.*;
import java.io.*;

public class Main {
    public static int N;
    public static int[] arr;
    public static int answer = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        input();
        recursion(0, 0);
        if(answer == Integer.MAX_VALUE){
            System.out.print(-1);
        } else {
            System.out.print(answer);
        }
    }

    public static void recursion(int idx, int cnt){
        // System.out.println("현재 인덱스 = " + idx);
        // System.out.println("현재 점프 횟수 = " + cnt);
        if(idx >= N-1){
            answer = Math.min(answer, cnt);
            return;
        }

        int jumpable = arr[idx];
        for(int i = 1; i <= jumpable; i++){
            recursion(idx+i, cnt+1);
        }
        
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        arr = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
    }
}