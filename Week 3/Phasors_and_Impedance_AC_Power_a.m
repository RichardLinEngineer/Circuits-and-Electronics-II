clc;
clear;
close all;

% Problem 1: Phasor and Impedance, AC Power (a)
% A capcitor in series with a parallel combination of an inductor and a resistor

% Cos(2pi*100*10^3t)
V_tot = 1; %[V]
omega = 2*pi*100*10^3;

R = 4000;    %[Ω]
L = 3*10^-3; %[H]
C = 1*10^-9; %[F]

%Impedance
Z_R = R;
Z_L = 1i*omega*L;
Z_C = 1/(1i*omega*C);

%Converstion
base_to_mili = 1000; %[1 base unit is 1000 mili unit]


%Finding Z_ab
Z_ab = (Z_C) + (Z_L*Z_R)/(Z_R+Z_L) %[ohms]

%Find Re{Z_ab} [Ω]
Z_ab_real = real(Z_ab)

%Find Im{Z_ab} [Ω]
Z_ab_img = imag(Z_ab)

%Find the amplitude of Time domain current [mA]
mag_Z_ab = sqrt((Z_ab_real)^2 + (Z_ab_img)^2); %[Ω]
I_tot = (V_tot/mag_Z_ab); %[A]
I_tot_mA = I_tot*base_to_mili %[mA]

%Find the Phasor angle of Time domain current i(t) [deg]
theta_Z = atan2(Z_ab_img, Z_ab_real);
theta_I = -theta_Z;
theta_I_deg = rad2deg(theta_I) %[deg]

%Find the amplitude of Time domain current i_L(t) [mA]
Z_LR = (Z_L*Z_R)/(Z_R+Z_L);
I_tot_phasor = I_tot*exp(1i*theta_I);
V_LR = I_tot_phasor*Z_LR; %[V]
I_L = V_LR/Z_L; %[A]
I_L_mag = abs(I_L); %[A]
I_L_mag_mA = I_L_mag*base_to_mili %[mA]

%Find the phase angle of Time domain current i_L(t) [deg]
theta_L_rad = atan2(imag(I_L), real(I_L));
theta_L_deg = rad2deg(theta_L_rad) %[deg]
%Find the amplitude of Time domain voltage v(t) [V]
V_LR_mag = abs(V_LR)

%Find the phase of Time domain voltage [deg]
theta_V_LR_deg = rad2deg(angle(V_LR))

%Find the rms voltage of the voltage source cos(2pi*100*10^3t)
V_rms_source = V_tot/(sqrt(2)) %[V]

%Find the rms voltage of Time domain voltage v(t) [V]
V_rms_LR = V_LR_mag/(sqrt(2))

%Find the rms current of Time domain current i_L(t) [mA]
I_L_rms = I_L_mag/(sqrt(2)) %[A]
I_L_rms_mA = I_L_rms*base_to_mili %[mA]


%Find the rms current of Time domain current i(t) [mA]
I_tot_rms = I_tot/(sqrt(2)); %[A]
I_tot_rms_mA = I_tot_rms*base_to_mili %[mA]


%Find the average power consumed [mW] by equivalent impedance Z_ab
P_cons = (I_tot_rms^2)*Z_ab_real;
P_cons_mW = P_cons*base_to_mili

%Find the average power supplied [mW] by  the voltage source Note we are using passive sign convention. So should power of a source be positive or negative? Check your results in MultiSim.
P_supp = -P_cons;
P_supp_mW = -P_cons_mW

%End of File