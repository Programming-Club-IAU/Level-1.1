import java.util.Scanner;
public class task2 {
    public static void main(String[] args){
        Scanner enter=new Scanner(System.in);
        System.out.println("Enter the first number");
        int first= enter.nextInt();
        System.out.println("Enter the second number");
        int second= enter.nextInt();
        if(first>second)
            System.out.println(first+" is grater than "+second );
        else if(second>first)
            System.out.println(second+" is grater than "+first );
        else
            System.out.println("The two numbers are equal");  
    }
}
