package Hash;

import java.util.HashMap;
import java.util.Map;

class PhoneBook {
    public boolean solution(String[] phoneBook) {
        Map<String, Integer> map = new HashMap<>();

        //모든 전화번호를 HashMap에 넣기
        for (int i = 0; i < phoneBook.length; i++)
            map.put(phoneBook[i], i);

        //모든 전화번호의 substring이 HashMap에 존재하는지 확인
        for (int i = 0; i < phoneBook.length; i++)
            for (int j = 0; j < phoneBook[i].length(); j++)
                if (map.containsKey(phoneBook[i].substring(0, j)))
                    return false;

        return true;
    }
}