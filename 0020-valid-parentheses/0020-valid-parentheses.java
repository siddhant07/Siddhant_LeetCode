import java.util.*;
class Solution {
    public boolean isValid(String s) {
        Stack f1=new Stack();
        char temp=s.charAt(0);
        
        
        for(int i=0;i<s.length();i++){
            if(!f1.empty())
                temp=(char)f1.peek();
            if(s.charAt(i)=='(' || s.charAt(i)=='{' || s.charAt(i)=='[')
                f1.push(s.charAt(i));
            else if(s.charAt(i)=='}' && temp=='{' && !f1.empty())
                f1.pop();
            else if(s.charAt(i)==')' && temp=='(' && !f1.empty())
                f1.pop();
            else if(s.charAt(i)==']' && temp=='[' && !f1.empty())
                f1.pop();
            else
                return false;
        }
        
        if(f1.empty())
            return true;
        return false;
    }
}