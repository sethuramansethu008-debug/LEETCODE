class Solution {
    public String minRemoveToMakeValid(String s) {
        Deque<Integer> stack=new ArrayDeque<>();
        boolean[] remove=new boolean[s.length()];

        for(int i=0;i<s.length();i++){
            char c=s.charAt(i);

            if(c=='('){
                stack.push(i);
            }
            else if(c==')'){
                if(stack.isEmpty()){
                    remove[i]=true;
                }
                else{
                    stack.pop();
                }
            }
        }

        while(!stack.isEmpty()){
            remove[stack.pop()]=true;
        }

        StringBuilder ans=new StringBuilder();

        for(int i=0;i<s.length();i++){
            if(!remove[i]){
                ans.append(s.charAt(i));
            }
        }

        return ans.toString();
    }
}