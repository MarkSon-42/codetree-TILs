import java.util.*;
import java.io.*;

public class Main {
    public static Map<String, String> map = new HashMap<>();

    public static void main(String[] args) throws IOException{
        input();
    }

    public static void input() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        for(int i = 1; i <= n; i++){
            String str = br.readLine();
            map.put(str, Integer.toString(i));
            map.put(Integer.toString(i), str);
        }

        for(int i = 0; i < m; i++){
            String temp = br.readLine();

            System.out.println(map.get(temp));
        }
    }
}