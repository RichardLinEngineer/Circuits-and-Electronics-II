public class Complex_Number_Review{
    public static void main(String[] args){
        if(args.length < 3){
            System.err.println("Usage:");
            System.err.println("java Complex_Number_Review <form> <a/A> <b/angle in deg>");
            System.err.println("<form>: r = rectangular, p = phasor");
            return;
        }
        String form = args[0];

        //Check which form is given
        switch(form){
            case "r" ->{
                double a = Double.parseDouble(args[1]);
                double b = Double.parseDouble(args[2]);

                //Calculate Magnitude of Complex Number (Z)
                double mag_Z = Math.sqrt((Math.pow(a,2)+Math.pow(b,2)));
                System.out.printf("|Z| = %.2f\n", mag_Z);
                
                //Calculate Angle of Complex Number (Z)
                double angle_Z = Math.toDegrees(Math.atan2(b, a));
                System.out.printf("∠Z = %.2f°\n", angle_Z);

                //Calculate real of Complex Number (Z)
                System.out.printf("Re{z} = %.2f\n", a);

                //Calculate imaginary of Complex Number (Z)
                System.out.printf("Im{z} = %.2f\n", b);

            }case "p" -> {
                double A = Double.parseDouble(args[1]);
                double angle_deg = Double.parseDouble(args[2]);
                double angle_rad = Math.toRadians(angle_deg);

                //Calculate Magnitude of Complex Number (Z)
                System.out.printf("|Z| = %.2f\n", A);
                
                //Calculate Angle of Complex Number (Z)
                System.out.printf("∠Z = %.2f°\n", angle_deg);

                //Calculate real of Complex Number (Z)
                double real = A*Math.cos(angle_rad);
                System.out.printf("Re{z} = %.2f\n", real);

                //Calculate imaginary of Complex Number (Z)
                double img = A*Math.sin(angle_rad);
                System.out.printf("Im{z} = %.2f\n", img);
            }
            default -> System.err.println("Invalid form. Use r or p.");
        }
    }
}