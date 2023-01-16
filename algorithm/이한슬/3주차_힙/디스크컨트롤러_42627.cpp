#include <string>
#include <queue>
#include <deque>
#include <algorithm>
using namespace std;

struct comp {
    bool operator()(pair<int, int> job1, pair<int, int> job2)
    {
        if (job1.second > job2.second)
            return true;
        else if(job1.second == job2.second)
            return job1.first > job2.first;
        return false;
    }
};

// shortest job first
int solution(vector<vector<int>> jobs) {
    int answer = 0;
    
    deque<pair<int, int>> dq;   // 현재 수행중인 일이 끝날때까지 아직 요청오지 않을 일들
    priority_queue<pair<int,int>,vector<pair<int,int>>, comp> pq; //현재 일 처리중인데 요청 들어오는 일들(짧은 순으로 정렬)
    
    for(auto job: jobs) dq.push_back({job[0], job[1]});
    sort(dq.begin(), dq.end());
    
    
    int cur_job_start_time, cur_job_req_time, cur_job_duration;
    while (dq.size() + pq.size()>0) {
        
        if(pq.empty()) {
            //우선순위 큐 비어있다면 요청 시간 가장 빠른 일 시작
            cur_job_start_time = cur_job_req_time = dq.front().first;
            cur_job_duration = dq.front().second;
            dq.pop_front();
        } else { 
            //우선순위 큐 비어있지 않다면 우선순위 큐에 들어있는 것중 가장 짧은 일 처리
            cur_job_req_time = pq.top().first;
            
            if(cur_job_start_time < cur_job_req_time)
                cur_job_start_time = cur_job_req_time;
            
            cur_job_duration = pq.top().second;
            pq.pop();
        }
        
        while(dq.size()>0 && dq.front().first <= cur_job_start_time + cur_job_duration) {
            //현재 일 처리중에 요청이 들어오는 일이 있다면 우선순위 큐에 넣음
            pq.push(dq.front());
            dq.pop_front();
        }
        
        //현재 일 종료. 여기까지 시간 계산.
        answer += (cur_job_start_time + cur_job_duration) - cur_job_req_time;
        
        //다음 일 계산을 위해 일 시작시간 초기화
        cur_job_start_time = cur_job_start_time + cur_job_duration;
    }
    
    
    return answer / jobs.size();
}