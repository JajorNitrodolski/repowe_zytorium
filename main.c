#include <stdio.h>
#include <math.h>
#include <time.h>

/* zadek 1
short minimum(short tab[], short n){
    short min=50;
    for(short i=0; i<n; i++) if(tab[i]<min) min=tab[i];
    return min;
}
void wyswietl(short tab[], short n){
    for(short i=0; i<n; i++) printf("%d ",tab[i]);
    printf("\n");
}
void generuj(short tab[], short n){
    for(short i=0; i<n; i++) tab[i]=rand()%100-49;
}
int main(){
    srand(time(0));
    const short N=500;
    short n=rand()%50+1;
    short tab[n];
    generuj(tab,n);
    wyswietl(tab,n);
    printf("Minimalna: %d",minimum(tab,n));
    return 0;
}*/

/* zadek 2
int pierwszaCyfra(int n){
    if(n>=0) while(n>9) n/=10;
    else while(n<-9) n/=10;
    return abs(n);
}
int main(){
    int liczba=-213769420;
    printf("Liczba: %d\nPierwsza jej cyfra: %d",liczba,pierwszaCyfra(liczba));
    return 0;
}*/

/* zadek 3
void zamieniarka(int *prw, int *drg){
    int temp;
    if(*drg<*prw){
        temp=*prw;
        *prw=*drg;
        *drg=temp;
    }
}
int main(){
    int prw=15;
    int drg=9;
    printf("Przed podmianka: %d, %d\n",prw,drg);
    zamieniarka(&prw,&drg);
    printf("i po: %d, %d",prw,drg);
    return 0;
}*/
