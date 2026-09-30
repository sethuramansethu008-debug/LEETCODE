class Solution {
    public int countQuadruplets(int[] nums) {
        int c=0;

for(int i=0;i<nums.length;i++){
    for(int j=i+1;j<nums.length;j++){
        for(int k=j+1;k<nums.length;k++){
            for(int l=k+1;l<nums.length;l++){
                if(nums[i]+nums[j]+nums[k]==nums[l]){
                    c++;
                }
            }
        }
    }
}

return c;
        
    }
}