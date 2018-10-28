#include <stdio.h>


int main(){

    int a,b;
    scanf("%d%d",&a,&b);
    int i;
    int check = 0;
    int arr[100];
    int checks;
    for(i = 0;i < a;i++){
        scanf("%d",&arr[i]);
        if (i+1 == b){
            checks = arr[i];
            printf("ini nilai i=%d dan ini nilai check=%d",i,checks);
        }
    }
    int c = arr[b-1];
    printf("\nini nilai c  = %d\n",c);



    for(i = 0;i < a;i++){
        if (arr[i]>=checks && arr[i] > 0){
            check++;
        }



    }
    printf("%d",check);

    return 0;
}
