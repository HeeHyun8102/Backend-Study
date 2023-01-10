#include <string>
#include <vector>

using namespace std;

int pop_work(vector<int> &progresses, vector<int> &speeds, int done_works_num) {
    progresses.erase(progresses.begin());
    speeds.erase(speeds.begin());
    return done_works_num+1;
}

int calculate_days_left(int progress, int speed) {
    int days_left = (100 - progress) / speed;
    if((100 - progress) % speed > 0) days_left++;
    return days_left;
}

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    
    while(progresses.size() > 0) {
        int days_left = calculate_days_left(progresses[0], speeds[0]);
    
        int done_works_num = pop_work(progresses, speeds, 0);
        
        int left_works_num = progresses.size();
        for(int i=0; i < left_works_num; i++) {
            if(progresses[0] + days_left*speeds[0] < 100) break;
            
            done_works_num = pop_work(progresses, speeds, done_works_num);
        }
        
        answer.push_back(done_works_num);
        
    }
    
    return answer;
}


//////////////////////////// 굿코드 ///////////////////////////////
vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;

    int day;
    int max_day = 0;
    for (int i = 0; i < progresses.size(); ++i)
    {
        day = (99 - progresses[i]) / speeds[i] + 1;

        if (answer.empty() || max_day < day)
            answer.push_back(1);
        else
            ++answer.back();

        if (max_day < day)
            max_day = day;
    }

    return answer;
}