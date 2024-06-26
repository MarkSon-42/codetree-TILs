import java.util.*;
import java.io.*;

public class Main {
    public static int N, M;
    public static int[] nums;
    public static int answer = 0;

    public static void main(String[] args) throws IOException {
        input();

        recursion(0, 0, 0);
        System.out.print(answer);
    }

    public static void recursion(int lastNum, int cnt, int idx){
        if(cnt == M){
            answer = Math.max(answer, lastNum);
            return;
        }

        if(idx == N)
            return;

        // idx에 있는 숫자를 선택하지 않은 경우
        recursion(lastNum, cnt, idx+1);

        // idx에 있는 숫자를 선택한 경우
        recursion(lastNum ^ nums[idx], cnt+1, idx+1);
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        nums = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
    }
}