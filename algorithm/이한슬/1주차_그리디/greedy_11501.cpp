#include <iostream>
#include <vector>
using namespace std;

int main() {
  ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
  vector<long> result;
  
  int t;
  cin >> t;
  
  for(int i = 0; i < t; i++) {
    int n;
    int price[1000000];
    cin >> n;
    result.push_back(0);
    for(int j = 0; j < n; j++) {
      cin >> price[j];
    }
    int curMax = price[n-1];
    for(int j = n-1; j >= 0; j--) {
      if(price[j] > curMax) {
        curMax = price[j];
        continue;
      }
      result[i] += curMax - price[j];
    }
  }

  for(int i = 0; i < t; i++) {
    cout << result[i] << endl;
  }
  
}