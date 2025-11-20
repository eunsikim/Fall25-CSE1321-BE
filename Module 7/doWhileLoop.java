import java.util.Scanner;

public class doWhileLoop {
    public static void main(String[] args) {
        boolean loop = true;

        Scanner sc = new Scanner(System.in);

        do{
            System.out.println("1. To print \"Hello World\"");
            System.out.println("2. To Exit");
            System.out.print("> ");
            char option = sc.nextLine().charAt(0);

            if(option == '1'){
                System.out.println("Hello World");
            }
            else if(option == '2'){
                loop = false;
                System.out.println("Shutting off...");
            }
            else{
                System.out.println("Incorrect Option, try again!\n");
            }
        }
        while(loop);
    }
}
