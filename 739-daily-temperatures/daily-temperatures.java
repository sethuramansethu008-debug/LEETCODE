class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n=temperatures.length;
        int[] answer=new int[n];
        int[] stack=new int[n];
        int top=-1;
        for(int i=0;i<n;i++){
            while(top>=0 && temperatures[i]>temperatures[stack[top]]){
                int previndex=stack[top--];
                answer[previndex]=i-previndex;
            }
            stack[++top]=i;

        }
        return answer;
        
    }
}