#include <iostream>
#include <string>

using namespace std;


int main(){

    int row,col;
    int color = 0;
    int bw = 0;
    cin >> row >> col;


    string photo[row][col];
    for(int i = 0;i < row;i++){
        for(int j = 0;j < col;j++){
            cin >> photo[i][j];
            if(photo[i][j] == "B" || photo[i][j] == "W" || photo[i][j] == "G"){
                bw +=1;
            }
            else{
                color+=1;
            }
        }
    }

    if(color == 0 && bw > 0){
        cout << "#Black&White";
    }
    else{
        cout << "#Color";
    }




    return 0;
}
