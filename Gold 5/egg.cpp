#include <iostream>
using namespace std;

int eggs;
int dur[8];
int weight[8];
int broken[8];

int num;
int max_num;
void f(int n) {
    if(n == eggs - 1) {
        if(max_num < num) {
            max_num = num;
        }
        return;
    }
    
    if(broken[n] == 1) {
        f(n + 1);
    }
    
    for(int i = 0; i < eggs; i++) {
        int n = 0;
        
        if(n == i || broken[i] == 1) {
            continue;
        }
        
        dur[n] -= weight[i];
        dur[i] -= weight[n];
        
        if(dur[n] < 0) {
            n++;
            broken[n] = 1;
        }
        
        if(dur[i] < 0) {
            n++;
            broken[i] = 1;
        }
        num += n;
        f(n + 1);
        
        dur[n] += weight[i];
        dur[i] += weight[n];
        num -= n;
        broken[n] = 0;
        broken[i] = 0;
    }
}

int main() {
    cin >> eggs;
    for(int i = 0; i < eggs; i++) {
        cin >> dur[i] >> weight[i];
    }
    
    f(0);
    
    cout << max_num;
}