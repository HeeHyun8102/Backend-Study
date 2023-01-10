#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int n;

int main() {
  ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
  
  cin >> n;

  vector<pair<int, int>> v(n);
  priority_queue <int, vector<int>, greater<int>> pq;
  
  for(int i = 0; i < n; i++) {
    cin >> v[i].first >> v[i].second;
  }

  sort(v.begin(), v.end());
  pq.push(v[0].second);

  int j = n;
  
  for(int i = 1; i < n; i++) {
    if(v[i].first >= pq.top()) {
      pq.pop();
      pq.push(v[i].second);
    } else {
      pq.push(v[i].second);
    }
  }
  
  cout << pq.size() << endl;
  
}