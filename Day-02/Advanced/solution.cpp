class Solution {
public:
    int peopleAwareOfSecret(int n, int delay, int forget) {
        vector<long> dp(n + 1, 0);
        dp[1] = 1;
        for(int i = 1; i < n; i++)
        {
            for(int j = i + delay; j < i + forget && j <= n; j++)
            {
                dp[j] = (dp[j] + dp[i]) % (int)(1e9 + 7);
            }
        }
        long people = 0;
        for(int i = n - forget + 1; i <= n; i++)
        {
            if(i >= 1)
            {
                people = (people + dp[i]) % (int)(1e9 + 7);
            }
        }
        return people;
    }
};