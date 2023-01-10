import java.util.Scanner;

public class BackJoon {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); //거스름돈 (1<= n <= 100000)
        int count = 0; //동전

        while(true){
            if(n%5 == 0){ //거스름돈이 5의 배수이면
                count += n/5; // coin = coin + n/5 거스름돈을 모두 5원으로 지급
                break;
            }else { //거스름돈이 5의 배수가 아니라면
                n -= 2; // n = n-2
                count++; // count = count + 1
            }

            if(n<0){ //거스름돈을 거슬러 줄수 없다면
                System.out.println("거스름돈=" + -1);
                return;
            }
            System.out.println("count=" +count+ ", n=" +n);

        }
    }
}

