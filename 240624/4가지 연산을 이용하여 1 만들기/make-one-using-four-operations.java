import java.util.*;
import java.io.*;

public class Main {
    public static int n;
    public static int[] visited = new int[1000002];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        Deque<int[]> q = new ArrayDeque<>();
        q.add(new int[]{n, 0});
        visited[0] = 1;

        while(!q.isEmpty()){
            int[] temp = q.poll();
            int num = temp[0];
            int cnt = temp[1];

            if(num == 1){
                System.out.print(cnt);
                break;
            }

            if(visited[num-1] == 0) {
                q.add(new int[]{num-1, cnt+1});
                visited[num-1] = visited[num] + 1;
            }
            if(visited[num+1] == 0) {
                q.add(new int[]{num+1, cnt+1});
                visited[num+1] = visited[num] + 1;
            }

            if(num % 2 == 0 && visited[num/2] == 0) {
                q.add(new int[]{num/2, cnt+1});
                visited[num/2] = visited[num] + 1;
            }
            if(num % 3 == 0 && visited[num/3] == 0) {
                q.add(new int[]{num/3, cnt+1});
                visited[num/3] = visited[num] + 1;
            }
        }
    }
}