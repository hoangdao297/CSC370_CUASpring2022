
package runlengthencodejava;

/**
 *
 * @author Hoang Dao
 */
public class RunLengthEncodeJava {

    public static String encode(String input){
        if (input.length()==0) return "\"\"";
        String result="";
        char currentchar=input.charAt(0);
        int currentcharcount=1;
        for (int i=1;i<input.length();i++){
            if (input.charAt(i)==currentchar){
                currentcharcount++;continue;
            }
            if (currentcharcount>4)result+="/"+((char)currentcharcount/10)+((char)currentcharcount%10)+currentchar;
            else{
                for (int j=0;j<currentcharcount;j++) result+=currentchar;
            }
            currentchar=input.charAt(i);
            currentcharcount=1;
        }
        if (currentcharcount>4)result+="/"+((char)currentcharcount/10)+((char)currentcharcount%10)+currentchar;
        else{
            for (int j=0;j<currentcharcount;j++) result+=currentchar;
        }
        return result;
    }
    
    public static String encode2(String input){
        if (input.length()==0) return "\"\"";
        String result="";
        char currentchar=input.charAt(0);
        int currentcharcount=1;
        String tempstr=""+currentchar;
        for (int i=1;i<input.length();i++){
            if (input.charAt(i)==currentchar){
                tempstr+=currentchar;currentcharcount++;continue;
            }
            if (currentcharcount>4)result+="/"+((char)currentcharcount/10)+((char)currentcharcount%10)+currentchar;
            else result+=tempstr;
            currentchar=input.charAt(i);
            currentcharcount=1;
            tempstr=""+currentchar;
        }
        if (currentcharcount>4)result+="/"+((char)currentcharcount/10)+((char)currentcharcount%10)+currentchar;
        else result+=tempstr;
        return result;
    }
    
    public static void main(String[] args) {
        String input="if(a){if(b){if(c){if(d){if(e){5 deeeeeeep}}}}}";
        System.out.println(encode(input));
        System.out.println(encode2(input));
        System.out.println(encode(""));
        System.out.println(encode2(""));
        System.out.println(encode("aaaa"));
        System.out.println(encode2("aaaa"));
        System.out.println(encode("aaaaa"));
        System.out.println(encode2("aaaaa"));
    }
    
}
