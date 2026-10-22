
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> x(n), r(n);

    for (int i = 0; i < n; i++) {
        cin >> x[i] >> r[i];
    }

    // Sort billboards by position
    vector<pair<int, int>> billboards(n);

    for (int i = 0; i < n; i++) {
        billboards[i] = {x[i], r[i]};
    }

    sort(billboards.begin(), billboards.end());

    vector<int> dp(n + 1, 0);

    for (int i = 1; i <= n; i++) {
        int pos = billboards[i - 1].first;
        int revenue = billboards[i - 1].second;

        // Find the last compatible billboard
        int j = i - 2;

        while (j >= 0 &&
               pos - billboards[j].first <= 5) {
            j--;
        }

        // Option 1: Skip current billboard
        int skip = dp[i - 1];

        // Option 2: Select current billboard
        int take = revenue + dp[j + 1];

        dp[i] = max(skip, take);
    }

    cout << "Maximum revenue: " << dp[n] << '\n';

    return 0;
}

