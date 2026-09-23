class Solution {
    public int equalSubstring(String s, String t, int maxCost) {
        int n=s.length();
        int start=0;
        int cost=0;
        int maxlength=0;
        for(int i=0;i<n;i++)
        {
            cost+=Math.abs(s.charAt(i)-t.charAt(i));
            while(cost>maxCost){
                cost-=Math.abs(s.charAt(start)-t.charAt(start));
                ++start;
            }
            maxlength=Math.max(maxlength,i-start+1);
        }
        return maxlength;
    }
}