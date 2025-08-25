class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_box = {}
        for letter in magazine:
            magazine_box[letter] = magazine_box.get(letter, 0) + 1

        for letter in ransomNote:
            if magazine_box.get(letter, 0) == 0:
                return False
            magazine_box[letter] -= 1

        return True