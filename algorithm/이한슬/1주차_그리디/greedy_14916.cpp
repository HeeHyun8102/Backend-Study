#include <iostream>
using namespace std;

int main() {
  int n;
  int cnt = 0;
  cin >> n;

  while (n > 0) {
    if (n % 5 == 0) {
      cnt += n / 5;
      break;
    }

    n -= 2;
    cnt++;
  }

  if (n < 0)
    cout << "-1" << endl;
  else
    cout << cnt << endl;
}