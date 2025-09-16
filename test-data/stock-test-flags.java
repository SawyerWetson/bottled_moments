public class ArrayExample {
    public static void main(String[] args) {
        String[][] stock = {
            {"Large", "Small"},
            {"OliviaSpecial", "VIPpack"}
        };
      
    }

    public static int maxStringLength(String[][] strings) {
        if (strings == null || strings.length == 0) {
            return 0; // Handle empty or null array
        }

        int maxLength = 0;
        for (int i = 0; i < strings.length; i++) {
            for (int j = 0; j < strings[i].length; j++) {
                if (strings[i][j].length() > maxLength) {
                    maxLength = strings[i][j].length();
                }
            }
        }
        return maxLength;
    }
}
