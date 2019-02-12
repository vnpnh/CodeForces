#include <iostream>

using namespace std;


int main(){

    int n1,n2,k1,k2;
    cin >> n1 >> n2 >> k1 >> k2;
    int c = n1,d = n2;
    int check1 = 0, check2 = 0;


    for (int i = 0;i < k1;i++){
        if(i+1 == k1 && c>1){
            check1 +=c;
        }
        else{
        c-=1;
        check1+=1;
        }
        if(c <= 0){
            break;
        }

    }

    for (int i = 0;i < k2;i++){
        if(i+1 == k2 && c>1){
            check2 +=d;
        }
        else{
        d-=1;
        check2+=1;
        }
        if(d <= 0){
            break;
        }
    }
    if (check1 > check2){
        cout << "First";
    }
    else{
        cout << "Second";
    }


    return 0;
}
