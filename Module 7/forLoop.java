public class forLoop {
    public static void main(String[] args) {
        for(int i = 0; i < 10; i++){ // Similar like for i in range(10) but not with a "range" sequence
            System.out.println("i = " + i);
        }

        // If we try to do the same with a "while" loop...
        int i = 0;

        while(i < 10){
            System.out.println("i = " + i);
            i++;
        }
    }
}
