
import java.lang.Integer;
import java.util.Scanner;
import java.util.Random;

public class JavaStudy06 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        // Random rnd = new Random();

        int n_vote = sc.nextInt();
        int n_can = sc.nextInt();
        String[] name = sc.nextLine().split(" ");

        System.out.println("����" + n_vote);
        System.out.println("�־ȵ�." + n_can);
        System.out.println("�ٽ�.");

        for (int i = 0; i < name.length; i++) {
            System.out.println(name[i]);
        }

        sc.close();
    }

}
