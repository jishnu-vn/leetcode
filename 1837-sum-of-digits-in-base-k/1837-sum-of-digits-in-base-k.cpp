class Solution {
public:
    int sumBase(int n, int k) {
        int answer=0;
        while (n>0){
            answer+=n%k;
            n=n / k;
        }
        return answer;
    }
};