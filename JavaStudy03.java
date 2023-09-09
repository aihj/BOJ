
import java.util.Scanner;

public class JavaStudy03 {

    public static void main(String[] args) {

        int age = 0;
        int entryTime = 0;

        int fee = 10000;

        Scanner sc = new Scanner(System.in);

        age = sc.nextInt();
        entryTime = sc.nextInt();
        String ifMerit = sc.next();
        String ifCard = sc.next();
        sc.close();

        if (ifMerit.equals("y") || ifCard.equals("y")) {
            fee -= 8000;
        }

        else if (age < 13 || entryTime >= 17) {
            fee -= 4000;
            if (age < 3) {
                fee = 0;
            }
        }

        System.out.println("[입장권 계산]");
        System.out.println("나이를 입력해주세요.(숫자):" + age);
        System.out.println("입장시간을 입력해 주세요.(숫자입력):" + entryTime);
        System.out.println("국가유공자 여부를 입력해 주세요:(y/n)" + ifMerit);
        System.out.println("복지카드 여부를 입력해주세요(y/n):" + ifCard);
        System.out.println("입장료: " + fee);
    }
}