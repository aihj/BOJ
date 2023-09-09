
import java.lang.Integer;
import java.util.Scanner;
import java.util.Random;

public class JavaStudy04 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        String year = sc.next();
        String month = sc.next();
        String day = sc.next();
        String gender = sc.next();

        Random rnd = new Random();


        System.out.println("[주민등록번호 계산]");
        System.out.println("출생년도를 입력해 주세요:(yy)" + year);
        System.out.println("출생월을 입력해 주세요:(mm)" + month);
        System.out.println("출생일을 입력해 주세요:(dd)" + day);
        System.out.println("성별을 입력해주세요(m/f):" + gender);

        if (gender.equals("m")) {
            gender = "3";
        } else {
            gender = "4";
        }

        int backnum = rnd.nextInt(1000000);
        String number = year.substring(2) + month + day + "-" + gender + Integer.toString(backnum);

        sc.close();

        System.out.println(number);
    }

}
