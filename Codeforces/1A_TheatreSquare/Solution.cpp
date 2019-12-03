#include <iostream>

using namespace std;

int main() {
    long n;
    long m;
    long a;
    cin >> n >> m >> a;
    long nflagstones = n / a;
    if(n % a != 0) {
        nflagstones++;
    }
    long mflagstones = m / a;
    if(m % a != 0) {
        mflagstones++;
    }
    cout << nflagstones * mflagstones;
    return 0;
}