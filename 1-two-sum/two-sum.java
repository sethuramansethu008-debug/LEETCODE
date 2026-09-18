class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer>m=new HashMap<>();
        for(int i=0;i<nums.length;i++)
        {
            int v=target-nums[i];
            if(m.containsKey(v)){
                return new int[]{m.get(v),i};
            }
            
            m.put(nums[i],i);

        }
        return new int[]{};
    }
}