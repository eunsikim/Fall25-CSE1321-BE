// This is the same as a regular python "for" loop
public class forEachLoop {
    public static void main(String[] args) {
        String message = "Hello World";

        for(char c : message.toCharArray()){
            System.out.println(c);
        }
    }
}
