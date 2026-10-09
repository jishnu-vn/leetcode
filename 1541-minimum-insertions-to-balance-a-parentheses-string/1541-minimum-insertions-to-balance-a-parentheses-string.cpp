class Solution {
public:
    int minInsertions(string s) {
        int ans=0;
        int need=0;
        for(char ch:s){
            if (ch=='('){
                need+=2;
                if (need%2==1){
                    ans++;
                    need--;
                }}
                else{
                    need--;
                    if(need==-1){
                        ans+=1;
                        need=1;
                    }
                }
            
            }
        
        return ans+need;
    }
};