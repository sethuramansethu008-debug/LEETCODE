class Solution {
    public String simplifyPath(String path) {
        Deque<String> stack=new ArrayDeque<>();
        for(String part:path.split("/")){
            if(part.equals(".")||part.equals("")) continue;
            if(part.equals("..")){
                if(!stack .isEmpty()) stack.pop();
            }
            else stack.push(part);

        }
        StringBuilder res=new StringBuilder();
        while(!stack.isEmpty()){
            res.append("/").append(stack.removeLast());

        }
        return res.length()==0?"/":res.toString();

        
        
    }
}