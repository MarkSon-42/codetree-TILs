import java.util.*;
import java.io.*;

public class Main {
    public static int n, k;
    public static int[] arr;
    public static int answer = 0;
    public static List<Integer> selectedNums = new ArrayList<>();

    public static Map<String, String> map = new HashMap<>();

    public static void main(String[] args) throws IOException{
        input();
        findCombi(0, 0);
        System.out.print(answer);
    }

    public static void findCombi(int idx, int cnt) {
        if(idx == n){
            if(cnt == 2){
                if(selectedNums.stream().mapToInt(Integer::intValue).sum() == k){
                    answer++;
                }
            }
            return;
        }

        selectedNums.add(arr[idx]);
        findCombi(idx + 1, cnt + 1);
        selectedNums.remove(selectedNums.size() - 1);
        findCombi(idx + 1, cnt);
    }

    public static void input() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        arr = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
    }
}