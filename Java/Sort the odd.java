import java.util.ArrayList;
import java.util.Collections;
public class Sort the odd {
    public static int[] sortArray(int[] array) {
        ArrayList<Integer> odds = new ArrayList<>();
        
        // Step 1: Collect the odd numbers
        for (int i = 0; i < array.length; i++) {
            if (array[i] % 2 != 0) { // Check if the number is odd
                odds.add(array[i]);
            }
        }
        
        // Step 2: Sort the collected odd numbers
        Collections.sort(odds);
        
        // Step 3: Replace the odd numbers in the original array with the sorted odd numbers
        int index = 0;
        for (int i = 0; i < array.length; i++) {
            if (array[i] % 2 != 0) { // Check if the number is odd
                array[i] = odds.get(index);
                index++;
            }
        }
        
        return array;
      }
    
    }
