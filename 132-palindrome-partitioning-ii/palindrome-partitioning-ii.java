class Solution {

    boolean isPalindrome(String s, int start, int end) {
        while (start <= end) {
            if (s.charAt(start) != s.charAt(end)) {
                return false;
            }
            start++;
            end--;
        }
        return true;
    }

    int f(String s, int index, int[] dp) {

        if (index == s.length()) {
            return 0;
        }

        if (dp[index] != -1) {
            return dp[index];
        }

        int minPartitions = Integer.MAX_VALUE;

        for (int j = index; j < s.length(); j++) {

            if (isPalindrome(s, index, j)) {

                int partitions = 1 + f(s, j + 1, dp);

                minPartitions = Math.min(minPartitions, partitions);
            }
        }

        return dp[index] = minPartitions;
    }

    public int minCut(String s) {

        int n = s.length();

        int[] dp = new int[n + 1];

        Arrays.fill(dp, -1);

        return f(s, 0, dp) - 1;
    }
}