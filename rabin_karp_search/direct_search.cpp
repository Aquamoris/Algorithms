#include <iostream>

using namespace std;

bool directSearch(string s, string p, int n) {
    int lengthString = s.length();
    int lengthPattern = p.length();
    int count = 0;

    for(int i=0; i < lengthString - lengthPattern + 1; i++) {
        int k = 0;
        for(int j=i; j < i + lengthPattern; j++) {
            if (s[j] != p[k]) {
                break;
            }
            else {
                k++;
            }
            count++;
        }
    }
    if (count <= n) {
        return true;
    } else {
        return false;
    }
}

int main() {
    cout << directSearch("Aboba", "bo", 1) << endl;
    
    return 0;
}
