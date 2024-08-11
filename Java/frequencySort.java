import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
public class frequencySort {
    public static String frequencySort(String s) {
    HashMap<Character,Integer> freg = new HashMap<>();
    for(char c: s.toCharArray()){
        freg.put(c,freg.getOrDefault(c, 0)+1); 
        }
        List<Map.Entry<Character, Integer>> sortedEntries = new ArrayList<>(freg.entrySet());
        sortedEntries.sort((a, b) -> b.getValue().compareTo(a.getValue()));

        // Step 3: Build the result string
        StringBuilder sortedString = new StringBuilder();
        for (Map.Entry<Character, Integer> entry : sortedEntries) {
            char character = entry.getKey();
            int count = entry.getValue();
            for (int i = 0; i < count; i++) {
                sortedString.append(character);
            }
        }

        return sortedString.toString();

    }
}

    
