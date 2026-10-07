class Solution {
    List<String> ans=new ArrayList<>();

    public List<String> removeInvalidParentheses(String s) {
        int left=0,right=0;

        for(char c:s.toCharArray()){
            if(c=='(') left++;
            else if(c==')'){
                if(left>0) left--;
                else right++;
            }
        }

        solve(s,0,left,right,0,"");
        return ans;
    }

    void solve(String s,int i,int left,int right,int open,String str){
        if(i==s.length()){
            if(left==0&&right==0&&open==0&&!ans.contains(str))
                ans.add(str);
            return;
        }

        char c=s.charAt(i);

        if(c=='('){
            if(left>0)
                solve(s,i+1,left-1,right,open,str);
            solve(s,i+1,left,right,open+1,str+c);
        }
        else if(c==')'){
            if(right>0)
                solve(s,i+1,left,right-1,open,str);
            if(open>0)
                solve(s,i+1,left,right,open-1,str+c);
        }
        else{
            solve(s,i+1,left,right,open,str+c);
        }
    }
}