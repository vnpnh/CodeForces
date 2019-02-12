#include <iostream>

using namespace std;

int main(){

    int n,c,check = 0;
    cin >> n >> c;
    int t[n];
    for(int i = 0 ;i < n;i++){
        cin >> t[i];
    }

    for(int i = 0;i < n-1;i++){
        if(abs(t[i]-t[i+1])<= c){
            //cout<<"oi " << abs(t[i]-t[i+1]) <<endl;
           check+=1;
            }
        if(abs(t[i]-t[i+1])> c){
            check = 0;
            //cout <<"masuk "<<abs(t[i]-t[i+1]) <<endl;


            }
    }
    cout << check+1;




    return 0;
}
