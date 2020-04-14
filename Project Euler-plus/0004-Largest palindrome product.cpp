#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

#include <bits/stdc++.h>

using namespace std;

bool isPalindrome(int n)
{
    string num = to_string(n);
    for(int i = 0; i < num.size() / 2; ++i)
        if(num[i] != num[num.size()-1-i])
            return false;
    return true;
}

void generatePalindromes(set<int> &s)
{
    for(int i = 100; i < 1000; ++i)
        for(int j = 100; j < 1000; ++j)
            if(isPalindrome(i*j))
                s.insert(i*j);
}

int main()
{
    cin.tie(nullptr);
    cout.tie(nullptr);
    ios::sync_with_stdio(false);
    set<int> s;
    int t;
    cin >> t;
    generatePalindromes(s);
    while(t--)
    {
        int x;
        cin >> x;
        cout << *(--s.lower_bound(x)) << endl;
    }
    return 0;
}