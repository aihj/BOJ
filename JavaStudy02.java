import java.util.Scanner;

public class JavaStudy02 {
    public static void main(String[] args) {
        int payment = 0;
        int cashBack = 0;
        Scanner sc = new Scanner(System.in);

        System.out.println("[캐시백 계산]");
        System.out.print("결제 금액을 입력해 주세요.(금액):");

        payment = sc.nextInt();
        cashBack = payment / 10;

        if (cashBack >= 300) {
            cashBack = 300;
        } else if (cashBack < 100) {
            cashBack = 0;
        } else if (cashBack < 200) {
            cashBack = 100;
        } else if (cashBack < 300) {
            cashBack = 200;
        }
        System.out.println("결제 금액은 " + payment + "원이고, 캐시백은 " + cashBack + "원 입니다.");

    }
}