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
 


 int main()
{

    long int t,n;
    long int lar=2, fact=2;
    long int sqroot;
    int flag;

    cin >> t;

    for(long int i=0;i<t;i++)
    {
        cin >> n;
        
        lar=2, fact=2;
        sqroot = sqrt(n);
        flag = 0;
        while(n>1)
        {
            if((fact > sqroot) && (flag == 0))
            {
                cout << n << endl;
                break;
            }
            if(n%fact == 0)
            {
                flag = 1;
                lar = fact;
                while(n%fact == 0)
                    n = n/fact;
            }
            fact++;
        }
        if(flag == 1)
            cout << lar << endl;
    }
}