import java.util.*;
import java.io.*;

public class Main {
    public static int n, k;
    public static long[] arr;
    public static int answer = 0;
    public static List<Integer> selectedNums = new ArrayList<>();

    public static Map<Long, Integer> map = new HashMap<>();

    public static void main(String[] args) throws IOException{
        input();
        find();
        System.out.print(answer);
    }

    public static void find() {
        for(int i = 0; i < n; i++){
            long diff = k - arr[i];

            if(map.containsKey(diff)){
                answer += map.get(diff);
            }

            if(!map.containsKey(arr[i])){
                map.put(arr[i], 1);
            } else {
                map.put(arr[i], map.get(arr[i])+1);
            }
        }
    }

    public static void input() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        arr = Arrays.stream(br.readLine().split(" "))
                    .mapToLong(Long::parseLong)
                    .toArray();
    }
}