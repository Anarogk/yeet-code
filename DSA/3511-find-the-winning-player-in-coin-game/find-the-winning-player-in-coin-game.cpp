class Solution {
public:
    string losingPlayer(int x, int y) {
        bool cnt = 0;
        while (x>=1 && y >=4) {
            x-=1;
            y-=4;
            cnt = !cnt;
        }
        if (cnt) return "Alice"; 
        return "Bob";
    }
};