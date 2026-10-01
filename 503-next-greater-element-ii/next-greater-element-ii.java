class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int n=nums.length;
        int[] res=new int[n];
        Deque<Integer> st=new ArrayDeque<>();
        Arrays.fill(res,-1);
        for(int i=2*n-1;i>=0;i--){
            int curr_val=nums[i%n];
            while(!st.isEmpty() && st.peek()<=curr_val){
                st.pop();
            }
            if(i<n && !st.isEmpty()){
            res[i]=st.peek();
            }
            st.push(curr_val);

        }
        return res;
        
    }
}