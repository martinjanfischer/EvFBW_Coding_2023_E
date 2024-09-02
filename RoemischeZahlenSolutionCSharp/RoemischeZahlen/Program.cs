namespace Programmierkurs
{
    public class Program
    {
        /*#
         * Kommentar
         */
        // Kommentar
        public static string berechne_roemische_zahl(int arabische_zahl)
        {
            string roemische_zahl = "";
            // 101 bis 1000
            if (arabische_zahl >= 1000)
            {
                roemische_zahl += "M";
                arabische_zahl -= 1000;
            }
            if (arabische_zahl >= 900)
            {
                roemische_zahl += "CM";
                arabische_zahl -= 900;
            }
            if (arabische_zahl >= 500)
            {
                roemische_zahl += "D";
                arabische_zahl -= 500;
            }
            if (arabische_zahl >= 400)
            {
                roemische_zahl += "CD";
                arabische_zahl -= 400;
            }
            while (arabische_zahl >= 100)
            {
                roemische_zahl += "C";
                arabische_zahl -= 100;
            }
            //10 bis 100
            if (arabische_zahl >= 100)
            {
                roemische_zahl += "C";
                arabische_zahl -= 100;
            }
            if (arabische_zahl >= 90)
            {
                roemische_zahl += "XC";
                arabische_zahl -= 90;
            }
            if (arabische_zahl >= 50)
            {
                roemische_zahl += "L";
                arabische_zahl -= 50;
            }
            if (arabische_zahl >= 40)
            {
                roemische_zahl += "XL";
                arabische_zahl -= 40;
            }
            while (arabische_zahl >= 10)
            {
                roemische_zahl += "X";
                arabische_zahl -= 10;
            }

            //1 bis 9
            if (arabische_zahl >= 9)
            {
                roemische_zahl += "IX";
                arabische_zahl -= 9;
            }
            if (arabische_zahl >= 5)
            {
                roemische_zahl += "V";
                arabische_zahl -= 5;
            }
            if (arabische_zahl >= 4)
            {
                roemische_zahl += "IV";
                arabische_zahl -= 4;
            }
            while (arabische_zahl >= 1)
            {
                roemische_zahl += "I";
                arabische_zahl -= 1;
            }

            return roemische_zahl;
        }
        public static void Main(string[] args)
        {
            int[] array1 = new int[50];
            for (int i = 0; i < array1.Length; i++)
            {
                array1[i] = i;
            }
            for (int i = 0; i < array1.Length; i++)
            {
                if (array1[i] == 49)
                    System.Console.WriteLine("gefunden");
            }

            int n = 756;
            float pi = 3.14f;
            double dpi = 3.14;
            string name = "Lars";
            string roemische_zahl = "";
            roemische_zahl = berechne_roemische_zahl(n);

            /*
            foreach (string arg in args)
            {
                Console.WriteLine(arg);
            }
            */

            System.Console.WriteLine("Die römische Zahl von {0} lautet {1}", n, roemische_zahl);
        }
    }
}