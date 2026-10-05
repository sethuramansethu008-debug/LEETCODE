class Solution {
    public int largestRectangleArea(int[] arr) {

        int n=arr.length;
        int maxa=0;
        Deque<Integer> st=new ArrayDeque<>();
        for(int i=0;i<=n;i++){
            int curr=(i==n)?0:arr[i];
            while(!st.isEmpty() && arr[st.peek()]>=curr){
                int h=arr[st.pop()];
                int pse=st.isEmpty()?-1:st.peek();
                int nse=i;
                int wid=nse-pse-1;
                maxa=Math.max(maxa,h*wid);

            }
            if(i<n) st.push(i);
        }
        return maxa;        
            
        

        
    }
}