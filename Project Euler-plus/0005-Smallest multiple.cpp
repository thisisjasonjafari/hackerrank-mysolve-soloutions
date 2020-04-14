#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

typedef long long ll;

int logarithm(int base, int x) {
    return static_cast<int>(log(x)/log(base)); 
}

int main() {
    int t,n;
    ll sol;
    int sieve[51] = {0};
    vector<int> primes;

    for (int i = 2; i<=50;i++) {
        if (sieve[i] == 0) {
            primes.push_back(i);
            for (int j = i*i; j<=50; j+=i) {
                sieve[j] = 1;
            }
        }
    }

    cin >> t;

    while(t--) {
        cin >> n;
        sol = 1;
        for (vector<int>::iterator i = primes.begin(); i != primes.end(); ++i) {
            if (*i > n) {break;}
            sol *= pow(*i,logarithm(*i,n));
        }

        cout << sol << endl;
    }
}