import java.util.*;
import java.io.*;

public class Main {
    public static int N, M;
    public static List<Integer> list = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        input();
        recursion(1, 0);
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
    }

    public static void print() {
        for(int i = 0; i < list.size(); i++){
            System.out.print(list.get(i) + " ");
        }
        System.out.println();
    }

    public static void recursion(int currNum, int cnt) {
        if(currNum == N+1){
            if(cnt == M){
                print();
            }
            return;
        }

        list.add(currNum);
        recursion(currNum+1, cnt+1);
        list.remove(list.size()-1);

        recursion(currNum+1, cnt);
    }

}