#include <string>
#include <iostream>
#include <vector>
using namespace std;

bool solution(string s)
{
    vector<char> stack;
    
    for(int i = 0; i< s.size();i++) {
        if(s[i] == '(')
            stack.push_back(s[i]);
        else
            if(stack.size()>0)
                stack.pop_back();
            else
                // 언더플로우
                return false;
    }
    
    if(stack.size() > 0) 
        // 스택에 남은게 있다면
        return false;
    else 
        return true;
}


//////////////////////////////////////////////////////////////////////////////////////////////
// 벡터의 v.size()>0 는 v.empty()로 확인할 수 있다.
// empty() 함수는 모든 STL로 구현된 container들 모두에 대하여 O(1)이다.
// size() 함수는 특정 container(std::list)는 STL 구현에 따라 O(n)이 될 수 있으므로 앞으로 empty()를 사용하자.

//////////////////////////////////////////////////////////////////////////////////////////////
// 홀수나 )로 시작하는 경우는 처음 예외처리를 통해 시간 절약
