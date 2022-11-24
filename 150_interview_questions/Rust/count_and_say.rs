// The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

//     countAndSay(1) = "1"
//     countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.

// To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

// For example, the saying and conversion for digit string "3322251"

fn sol(n: i32) -> String {
    ///Solution Performance: Runtime 6 ms Beats 45.88% Memory 2.3 MB Beats 12.69%
    fn write_to_new_sf(next_sf: &mut String, tracker: u8, counter: &i32) {
        let addition = format!("{}{}", counter.to_string(), tracker as char);
        next_sf.push_str(addition.as_str());
    }

    fn helper(n: i32, sf: String) -> String {
        if n == 0 {
            return sf;
        }
        let sf = sf.as_bytes();
        let mut tracker = sf[0];
        let mut next_sf = String::from("");
        let mut counter = 1;
        for i in 1..sf.len() {
            if sf[i] == tracker {
                counter += 1;
            }else {
                write_to_new_sf(&mut next_sf, tracker, &counter);
                tracker = sf[i];
                counter = 1
            }
        }
        write_to_new_sf(&mut next_sf, tracker, &counter);
        return helper(n - 1, next_sf);
    }

    let answer = helper(n - 1, String::from("1"));
    answer
}
