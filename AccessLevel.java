
package accesslevel;

/**
 *
 * @author Hoang Dao
 */
public class AccessLevel {

    public static String canAccess(int[] rights, int minPermissions ){
        if (rights.length==0) return "\"\"";
        String result="";
        for (int i=0;i<rights.length;i++){
            if (rights[i]<minPermissions) result+="D";
            else result+="A";
        }
        return result;
    }
    public static void main(String[] args) {
        int[] rights={0,1,2,3,4,5};
        int[] rights2={};
        int minPer=2;
        System.out.println(canAccess(rights,minPer));
        System.out.println(canAccess(rights2,minPer));
    }
    
}
