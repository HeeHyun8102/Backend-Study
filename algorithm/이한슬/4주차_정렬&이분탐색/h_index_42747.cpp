#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> citations) {
    int h_index = 0;
    
    sort(citations.begin(), citations.end(), greater<>());
    
    if (citations[0] == 0) return 0; 
    
    for(int i =0; i < citations.size(); i++) {
        
        if (citations[i] >= i+1 ) {
            h_index++;
        } else {
            break;
        }
    }
    
    return h_index;
}