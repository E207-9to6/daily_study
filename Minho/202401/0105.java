import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {

    public static class Pair {
        int x;
        int y;

        Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        //TIP Press <shortcut actionId="ShowIntentionActions"/> with your caret at the highlighted text
        // to see how IntelliJ IDEA suggests fixing it.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int ans = 0;

        int[][] board = new int[n][n];
        int[][] board2 = new int[n][n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }


        // 블록 그룹 파악
        while (true) {
            boolean judge = true;
            boolean[][] vis = new boolean[n][n];
            Queue<Pair> sv = new ArrayDeque<>();

            int ck1 = -1;
            int ck2 = -1;

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (vis[i][j]) continue;
                    if (board[i][j] == 0) continue; // 무지개 블록
                    if (board[i][j] == -1) continue; // 검은 블록
                    if (board[i][j] == -100) continue; // 비어있는 칸

                    int ck = board[i][j];
                    int cnt = 0;
                    int rainbow = 0;
                    // bfs
                    Queue<Pair> q = new ArrayDeque<Pair>();
                    Queue<Pair> q2 = new ArrayDeque<Pair>();

                    q.offer(new Pair(i, j));
                    q2.offer(new Pair(i, j));

                    vis[i][j] = true;
                    boolean[][] vis2 = new boolean[n][n];
                    vis2[i][j] = true;

                    if (board[i][j] != 0) vis[i][j] = true;

                    while (!q.isEmpty()) {
                        cnt++;
                        int x = q.peek().x;
                        int y = q.peek().y;

                        if (board[x][y] == 0) {
                            rainbow++;
                        }
                        q.poll();
                        for (int k = 0; k < 4; k++) {
                            int nx = x + dx[k];
                            int ny = y + dy[k];

                            if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
                            if (vis2[nx][ny] || board[nx][ny] == -1) continue;
                            if (board[nx][ny] != ck) {
                                if (board[nx][ny] != 0) continue;
                            }

                            vis2[nx][ny] = true;
                            if (board[nx][ny] != 0) vis[nx][ny] = true;
                            q.offer(new Pair(nx, ny));
                            q2.offer(new Pair(nx, ny));
                        }

                    }

                    if (cnt > 1) {
                        judge = false;
                        boolean judge2 = false;
                        if (ck1 < cnt) {
                            ck1 = cnt;
                            ck2 = rainbow;
                            judge2 = true;
                        } else if (ck1 == cnt) { // 크기 같은 그룹있을때 기준블록 파악
                            if (ck2 < rainbow) {
                                ck2 = rainbow;
                                judge2 = true;
                            } else if(ck2 == rainbow){
                                judge2 = true;
                            }
                        }

                        if (judge2) {
                            sv.clear();
                            while (!q2.isEmpty()) {
                                sv.offer(q2.peek());
                                q2.poll();
                            }

                        }
                    }

                }
            }

            if (judge) break;

            // 블록 터뜨림
            ans += sv.size() * sv.size();
            while (!sv.isEmpty()) {
                int x = sv.peek().x;
                int y = sv.peek().y;
                board[x][y] = -100;
                sv.poll();
            }

            // 중력작용
            for (int i = n - 2; i >= 0; i--) {
                for (int j = 0; j < n; j++) {
                    if (board[i][j] != -100) {
                        if (board[i][j] == -1) continue;
                        int tmp = board[i][j];
                        for (int k = i + 1; k < n; k++) {
                            if (board[k][j] == -100) {
                                board[k - 1][j] = -100;
                                board[k][j] = tmp;
                            } else {
                                break;
                            }
                        }
                    }
                }
            }

            // 반시계회전

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    board2[i][j] = board[i][j];
                }
            }

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    board[i][j] = board2[j][n - i - 1];
                }
            }

            // 중력작용
            for (int i = n - 2; i >= 0; i--) {
                for (int j = 0; j < n; j++) {
                    if (board[i][j] != -100) {
                        if (board[i][j] == -1) continue;
                        int tmp = board[i][j];
                        for (int k = i + 1; k < n; k++) {
                            if (board[k][j] == -100) {
                                board[k - 1][j] = -100;
                                board[k][j] = tmp;
                            } else {
                                break;
                            }
                        }
                    }
                }
            }

        }

        System.out.println(ans);
    }
}