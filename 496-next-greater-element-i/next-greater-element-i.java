class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int[] ans=new int[nums1.length];
        for (int i=0;i<nums1.length;i++) {
            int j=0;
            while (nums2[j]!=nums1[i]) {
                j++;
            }
            ans[i]=-1;
            for (int k=j+1;k<nums2.length;k++) {
                if (nums2[k]>nums2[j]) {
                    ans[i]=nums2[k];
                    break;
                }
            }
        }

        return ans;
    }
}