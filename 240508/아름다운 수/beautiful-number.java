import java.util.*;
import java.io.*;

public class Main {
    public static List<Integer> list = new ArrayList<>();
    public static int N;
    public static int answer = 0;

    public static void main(String[] args) throws IOException {
        input();
        recursion(0);
        System.out.print(answer);
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
    }

    public static boolean check() {
        for(int i = 0; i < N; i += list.get(i)){
            int num = list.get(i);
            if(i + list.get(i) - 1 >= n)
                
            int cnt = 1;
            while(i <= N-2) {
                if(list.get(i+1) != num)
                    break;
                cnt++;
                i++;
            }
//            if(list.get(i) != 1 && list.get(i) == num)
//                cnt++;
            if(cnt % num != 0)
                return false;
        }

        return true;
    }

    // 순열을 만들어주는 재귀
    public static void recursion(int num){
        if(num == N){
            if(check())
                answer++;
            return;
        }

        for(int i = 1; i <= 4; i++){
            list.add(i);
            recursion(num+1);
            list.remove(list.size()-1);
        }
    }
}