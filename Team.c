#include <stdio.h>

int main(){

    int n;
    scanf("%d",&n);
    int i,j;
    int num[3];
    int total = 0;
    int last = 0;
    for(i = 0;i < n;i++){
        for(j = 0;j< 3;j++){
            scanf("%d",&num[j]);
            total += num[j];
        }
            if(total >= 2){
                last +=1;
            }
            total =0;


        }

    printf("%d",last);


    return 0;
}
