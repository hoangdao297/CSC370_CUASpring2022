package lexicalanalyzer;
import java.io.FileReader;  
import java.io.IOException;
import java.util.Arrays;
/**
 *
 * @author Hoang Dao
 */

public class LexicalAnalyzer {
    /*Global declarations*/
    /*Variables*/
    public static int charClass;
    public static char[] lexeme=new char[100];
    public static char nextChar;
    public static int lexLen;
    public static int token;
    public static int nextToken;
    public static FileReader fr;
    /*Character classes*/
    final static int LETTER=0;
    final static int DIGIT=1;
    final static int UNKNOWN=99;
    /*Token codes*/
    final static int INT_LIT=10;
    final static int IDENT=11;
    final static int ASSIGN_OP=20;
    final static int ADD_OP=21;
    final static int SUB_OP=22;
    final static int MULT_OP=23;
    final static int DIV_OP=24;
    final static int LEFT_PAREN=25;
    final static int RIGHT_PAREN=26;
    final static int EOF=-1;
    /*main driver*/
    public static void main(String[] args) {
        try {   
            fr=new FileReader("C:\\demo\\demofile.txt");   
            getChar();
            do{
                lex();
            } while (nextToken!=EOF);
        }  
        catch(IOException e)  
        {
            System.out.println("Error with opening file");
        }  
    }
    /* lookup - a function to lookup operators and parenthese and return the token */
    public static int lookup(char ch){
        switch (ch) {
            case '(' -> {
                addChar();
                nextToken = LEFT_PAREN;
                break;
            }
            case ')' -> {
                addChar();
                nextToken = RIGHT_PAREN;
                break;
            }
            case '+' -> {
                addChar();
                nextToken = ADD_OP;
                break;
            }
            case '-' -> {
                addChar();
                nextToken = SUB_OP;
                break;
            }
            case '*' -> {
                addChar();
                nextToken = MULT_OP;
                break;
            }
            case '/' -> {
                addChar();
                nextToken = DIV_OP;
                break;
            }
            default -> {
                addChar();
                nextToken = EOF;
                break;
            }
        }
        return nextToken;
    }
    /* addChar - a function to add nextChar to lexeme */
    public static void addChar(){
        if (lexLen <= 98) {
            lexeme[lexLen++] = nextChar;
            lexeme[lexLen] = 0;
        }
        else System.out.printf("Error - lexeme is too long \n");
    }
    /* getChar - a function to get the next character of input and determine its character class */
    public static void getChar() throws IOException{
        int r;  
        if ((r=fr.read())!=-1) {
            nextChar=(char)r;
            if (Character.isLetter(nextChar))
            charClass = LETTER;
            else if (Character.isDigit(nextChar))
            charClass = DIGIT;
            else charClass = UNKNOWN;
        }
        else
            charClass = EOF;
    }
    /* getNonBlank - a function to call getChar until it returns a non-whitespace character */
    public static void getNonBlank() throws IOException{
        while (Character.isSpaceChar(nextChar))
            getChar();
    }
    /* lex - a simple lexical analyzer for arithmetic expressions */
    public static int lex() throws IOException{
        lexLen = 0;
        getNonBlank();
        switch (charClass) {
        /* Parse identifiers */
            case LETTER:
                addChar();
                getChar();
                while (charClass == LETTER || charClass == DIGIT) {
                    addChar();
                    getChar();
                }   
            nextToken = IDENT;
            break;
            /* Parse integer literals */
            case DIGIT:
                addChar();
                getChar();
                while (charClass == DIGIT) {
                    addChar();
                    getChar();
                }      
            nextToken = INT_LIT;
            break;
            /* Parentheses and operators */
            case UNKNOWN:
                lookup(nextChar);
                getChar();
                break;
            /* EOF */
            case EOF:
                nextToken = EOF;
                lexeme[0] = 'E';
                lexeme[1] = 'O';
                lexeme[2] = 'F';
                lexeme[3] = 0;
                break;
        } /* End of switch */
        System.out.printf("Next token is: %d, Next lexeme is %s\n",nextToken, Arrays.toString(lexeme));
        return nextToken;
    }
}
