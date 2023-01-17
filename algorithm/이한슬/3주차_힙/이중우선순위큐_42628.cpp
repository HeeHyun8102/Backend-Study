#include <string>
#include <deque>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<string> operations) {
    vector<int> answer;
    deque<int> dq;
    
    for(auto op: operations) {
        if(op[0] == 'I') {
            dq.push_back(stoi(op.substr(2, op.size()-2)));
            sort(dq.begin(), dq.end());
        } else if(op[2] == '-' && !dq.empty()) {
            dq.pop_front();
        } else if(!dq.empty()) {
            dq.pop_back();
        }
    }
    
    if(dq.size() > 0) {
        answer.push_back(dq.back());
        answer.push_back(dq.front());
    } else {
        answer.push_back(0);
        answer.push_back(0);
    }
    
    return answer;
}

////////////////////////다른 사람 코드 1. multiset 사용: 중복가능한 set////////////////////////
#include <string>
#include <vector>
#include <set>

using namespace std;

vector<int> solution(vector<string> arguments) {
    vector<int> answer;
    multiset<int> que;
    multiset<int>::iterator iter;
    string sub;

    for(auto s : arguments) {
        sub =s.substr(0, 2);
        if(sub=="I ") que.insert(stoi(s.substr(2,s.length()-2))); 
        else if(s.substr(2,1)=="1"&&que.size()>0) { que.erase(--que.end()); }
        else if(que.size()>0) { que.erase(que.begin()); }
    }

    if(que.size()==0) { answer.push_back(0); answer.push_back(0); }
    else { 
        iter = --que.end(); answer.push_back(*iter); 
        iter = que.begin(); answer.push_back(*iter);
    }

    return answer;
}


///////////////////////////////////////////////////////////////////////////////////////
//다른 방법 - 우선순위 큐, 최대힙&최소힙 사용 등
