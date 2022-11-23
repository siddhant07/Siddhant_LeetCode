class Solution {
    public boolean areAlmostEqual(String s1, String s2) {
        if(s1.length()==s2.length()){
            char[] check=new char[4];
            int k=0, j=0;
            
            for(int i=0;i<s1.length();i++){
                if(s1.charAt(i)!=s2.charAt(i)&&j<4){
                    check[j]=s1.charAt(i);
                    j++;
                    check[j]=s2.charAt(i);
                    j++;
                }
                else if(s1.charAt(i)!=s2.charAt(i)&&j>=4)
                    return false;
            }
            
            System.out.println(check);
            if(check[0]==check[3]&&check[1]==check[2])
                return true;
        }
        return false;
    }
}