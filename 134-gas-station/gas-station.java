class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int tot=0,st=0,tank=0;
        for(int i=0;i<gas.length;i++){
            int pro=gas[i]-cost[i];
            tot+=pro;
            tank+=pro;
            if(tank<0){
                st=i+1;
                tank=0;

            }
        }
        return tot<0?-1:st;
        

    }
}