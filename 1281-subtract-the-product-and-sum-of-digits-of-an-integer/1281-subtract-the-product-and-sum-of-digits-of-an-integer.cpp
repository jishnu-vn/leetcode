class Solution {
public:
    int subtractProductAndSum(int n) {
        int sum=0,prod=1,digit=0;
        while(n>0){
            digit=n%10;
            sum+=digit;
            prod=prod*digit;
            n=n/10;
        }
        return prod-sum;
    }
};