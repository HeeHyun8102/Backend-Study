#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer;

    for(int i=0; i<arr.size();i++) {
        if(answer.size() != 0 && answer.back() == arr[i]) 
            continue;
        answer.push_back(arr[i]);
    }
    
    return answer;
}


//////////////////////////////////// 굿코드 //////////////////////////////////////////
vector<int> solution(vector<int> arr) 
{
    arr.erase(unique(arr.begin(), arr.end()),arr.end());

    vector<int> answer = arr;
    return answer;
}