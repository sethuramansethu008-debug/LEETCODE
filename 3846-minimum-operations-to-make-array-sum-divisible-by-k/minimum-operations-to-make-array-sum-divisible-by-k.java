class Solution {
    public int minOperations(int[] nums, int k) {
        long s=0;
        for(int i=0;i<nums.length;i++)
        {

            s=s+nums[i];
        }
        return (int)s%k;
    }
}