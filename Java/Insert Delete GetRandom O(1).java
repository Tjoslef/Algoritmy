import java.util.ArrayList;
import java.util.Random;
import java.util.HashMap;
class RandomizedSet {
    private ArrayList<Integer> list;
    private HashMap<Integer,Integer> map;
    public RandomizedSet() {
        list = new ArrayList<>();
        map = new HashMap<>();

    }
    
    public boolean insert(int val) {
        if(map.containsKey(val)){
            return false;
        }
        else{
            list.add(val);
            map.put(val,list.size()-1);
            return true;
        }
    }
    

    public boolean remove(int val) {
        if(!map.containsKey(val)){
            return false;
        }
        else{
            int indexR = map.get(val);
            int lValue = list.get(list.size()-1);
            list.set(indexR,lValue);
            map.put(lValue, indexR);
            list.remove(lValue);
            map.remove(val);
            return true;
        }
    }
    
    public int getRandom() {
        Random random = new Random();
        int num = random.nextInt(0,list.size());
        return list.get(num);
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
