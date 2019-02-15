#include <iostream>
#include <string>

using namespace std;


int main(){

    int n;
    bool check = false;


    cin >> n;
    string a[n];
    for(int i = 0;i < n;i++){
        cin >>a[i];

    }
    for(int i = 0;i < n;i++){
        int checker = 0;
        for(int j = 0;j <=5;j++){
            if (a[i][j] == 'O'){
                checker +=1;
            }
            else{
                checker = 0;
            }

            if(checker == 2){
                a[i][j] = '+';
                a[i][j-1] = '+';
                check = true;
                break;
            }
        }
        if (check == true){
            break;
        }
    }
    if(check == true){
        cout<<"YES"<<endl;
        for(int i =0;i < n;i++){
            cout << a[i]<<endl;
        }
    }
    else{
        cout << "NO"<<endl;
    }






    return 0;
}
