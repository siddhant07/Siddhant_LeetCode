class Solution {
    public int romanToInt(String s) {
        Map<String,Integer> map=new HashMap<>();
        map.put("I",1);
        map.put("V",5);
        map.put("X",10);
        map.put("L",50);
        map.put("C",100);
        map.put("D",500);
        map.put("M",1000);
        int val=0;
        
        if(s.length()>1){
            for(int i=0;i<s.length()-1;i++){
                String ith=String.valueOf(s.charAt(i));
                String i1th=String.valueOf(s.charAt(i+1));
            
                if(map.get(ith)<map.get(i1th)){
                    val+=map.get(i1th)-map.get(ith);
                    i++;
                }
                else
                    val+=map.get(ith);
            }
            String Last_Second_Element=String.valueOf(s.charAt(s.length()-2));
            String Last_Element=String.valueOf(s.charAt(s.length()-1));
        
            if(map.get(Last_Second_Element)>=map.get(Last_Element))
                val+=map.get(Last_Element);
            return val;
        }
        else if(s.length()==1)
            return map.get(s);
        return 0;    
    }
}