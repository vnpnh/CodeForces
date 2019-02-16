#include <iostream>
#include <string>
using namespace std;


int main(){

    int n;
    cin >> n;
    string a[n];
    int sum = 0;
    int zero = 0;
    int one = 0;

    cin >> a[0];
    for(int i = 0;i< n;i++){
        if (a[0][i] == '1'){
            one+=1;
        }
        else{
            zero +=1;
        }


    }
    if(one > zero){
        sum = one - zero;
    }
    else if(zero > one){
        sum = zero-one;
    }


    cout << sum;




    return 0;
}
