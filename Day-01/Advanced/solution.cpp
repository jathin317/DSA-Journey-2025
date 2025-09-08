#include <vector>
using namespace std;

class Solution {
public:
    vector<int> getNoZeroIntegers(int n) {
        for(int i = 1; i < (n/2)+1; i++)
        {
            if(noZero(i) && noZero(n - i))
            {
                return {i, n - i};
            }
        }
        return {};
    }

    bool noZero(int n)
    {
        while(n != 0)
        {
            int k = n % 10;
            if(k == 0)
            {
                return false;
            }
            n /= 10;
        }
        return true;
    }
};
