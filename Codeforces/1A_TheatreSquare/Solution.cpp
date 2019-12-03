#include <iostream>

using namespace std;

int main() {
    long long n;
    long long m;
    long long a;
    cin >> n >> m >> a;
    long long nflagstones = n / a;
    if(n % a != 0) {
        nflagstones++;
    }
    long long mflagstones = m / a;
    if(m % a != 0) {
        mflagstones++;
    }
    cout << nflagstones * mflagstones;
    return 0;
}