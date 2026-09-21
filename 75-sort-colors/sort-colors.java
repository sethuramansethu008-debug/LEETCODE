class Solution {
    public void sortColors(int[] nums) {
        int z=0,o=0,t=0;
        for(int a:nums)
        {
            if(a==0)
            z++;
            else if(a==1)
            o++;
            else
            t++;


        }
        for(int i=0;i<nums.length;i++)
        {
            if(z>0)
            {
                nums[i]=0;
                z--;
            }
            else if(o>0)
            {
                nums[i]=1;
                o--;

            }
            else
            {
                nums[i]=2;
                t--;
            }
        }
        
    }
}