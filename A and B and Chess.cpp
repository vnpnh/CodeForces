#include <iostream>
#include <string>

using namespace std;

int main(){
    int black = 0;
    int white = 0;

    string game[8];
    for(int i = 0;i <8;i++){
        cin >> game[i];
    }
    char a;

    for(int i = 0;i <8;i++){
        //cout << game[i].size()<<endl;


        for (int j = 0;j < 8;j++){
                char a = game[i][j];
                //cout<<a<<endl;
                //black
                if(a == 'q'){
                        black+=9;

                }
                if(a == 'r'){
                        black+=5;

                }
                if(a == 'b'){
                        black+=3;

                }
                if(a == 'n'){
                        black+=3;

                }
                if(a == 'p'){
                        black+=1;

                }
                if(a == 'k'){
                        black+=0;

                }

                //white
                if(a == 'Q'){
                        white+=9;

                }
                if(a == 'R'){
                        white+=5;

                }
                if(a == 'B'){
                        white+=3;

                }
                if(a == 'N'){
                        white+=3;

                }
                if(a == 'P'){
                        white+=1;

                }
                if(a == 'K'){
                        white+=0;

                }


                if (j == 8){
                    break;
                }


        }
        if(i == 8){
            break;
        }
    }
    if(black > white){
        cout << "Black";
    }
    else if(white > black){
        cout << "White";
    }
    else{
        cout << "Draw";
    }


    return 0;
}
