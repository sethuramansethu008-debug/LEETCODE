class Solution {
    public int longestConsecutive(int[] nums) {
        if(nums.length==0)
        return 0;
    Set<Integer> h=new HashSet<>();
    for(int num:nums)
    h.add(num);
    int lstreak=0;
    for(int num:h)
    if(!h.contains(num-1)){
        int numm=num;
        int cstreak=1;
        while(h.contains(numm+1)){
            numm++;
            cstreak++;

        }
        lstreak=Math.max(lstreak,cstreak);

    }
    return lstreak;
    }
}