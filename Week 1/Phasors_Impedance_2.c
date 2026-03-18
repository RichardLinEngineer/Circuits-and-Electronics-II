#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <complex.h>

/*
Used to Calculate the impedance of a capacitor in series with a parallel combination of an inductor and a resistor

Compile using:
gcc -std=c11 -Wall -o Phasors_Impedance_2 Phasors_Impedance_2.c -lm
*/


int main(int argc, char *argv[]){
    if (argc < 4){
        printf("Usage: %s <R value in kilohms> <L in millihenry> <C value in  nanofarad>", argv[0]);
        return 1;
    }
    
    double R = atof(argv[1])*1e3;     //Ohms
    double L = atof(argv[2])*1e-3;    //Henries
    double C = atof(argv[3])*1e-9;    //Farads

    double f = 100*1e3;
    double w = 2 * acos(-1) * f;

    double _Complex Z_R = R;
    double _Complex Z_C = 1/(I*w*C);
    double _Complex Z_L = I*w*L;

    double _Complex Z_ab = ((Z_R*Z_L)/(Z_L+Z_R))+Z_C;

    printf("Real part: %.2f\n", creal(Z_ab));
    printf("Imaginary part: %.2f\n", cimag(Z_ab));

    return 0;
}
//End of file