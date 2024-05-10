import java.util.*;
import java.io.*;

public class Main {
    public static int N, K;
    public static List<Integer> list = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        input();
        recursion(0);
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        K = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
    }

    public static void print() {
        for(int i = 0; i < list.size(); i++){
            System.out.print(list.get(i) + " ");
        }
    }

    public static boolean check() {
        int temp1 = list.get(0);
        int temp2 = list.get(1);
        int temp3 = list.get(2);

        for(int i = 2; i < list.size(); i++){
            if(temp1 == temp2 && temp1 == temp3)
                return false;
            temp1 = temp2;
            temp2 = temp3;
            temp3 = list.get(i);
        }
        return true;
    }

    public static void recursion(int num){
        if(num == N){
            if(N < 3){
                print();
                System.out.println();
                return;
            } else {
                if(check()){
                    print();
                    System.out.println();
                    return;
                }
            }
        }

        for(int i = 1; i <= K; i++){
            if(list.size() >= 3 && check()){
                continue;
            }
            list.add(i);
            recursion(num + 1);
            list.remove(list.size()-1);
        }
    }
}