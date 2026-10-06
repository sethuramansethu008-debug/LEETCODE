class Solution {
    public int jump(int[] nums) {
        int mj=0;
        int steps=0;
        int prev=0;
        for(int i=0;i<nums.length-1;i++){
            mj=Math.max(mj,i+nums[i]);
            if(i==prev){
                steps+=1;
                prev=mj;

            }
            
        }
        return steps;
        
    }
}