class Solution {
    public int longestSubstring(String s, int k) {
        int n=s.length();
        Map<Character,Integer> freq=new HashMap<>();
        for(char ch:s.toCharArray())
        {
            freq.put(ch,freq.getOrDefault(ch,0)+1);

        }
        for(char ch:freq.keySet())
        {
            if(freq.get(ch)<k){
                int maxlen=0;
                for(String sub:s.split(String.valueOf(ch))){
                    maxlen=Math.max(maxlen,longestSubstring(sub,k));


                }return maxlen;
                
            }
        }return n;
        
    }
}   