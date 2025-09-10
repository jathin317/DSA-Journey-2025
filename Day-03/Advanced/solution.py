class Solution(object):
    @staticmethod
    def can_communicate(person1, person2, languages):
        for lang1 in languages[person1 - 1]:
            for lang2 in languages[person2 - 1]:
                if lang1 == lang2:
                    return True
        return False

    def minimumTeachings(self, n, languages, friendships):
        """
        :type n: int
        :type languages: List[List[int]]
        :type friendships: List[List[int]]
        :rtype: int
        """
        problem_people = set()
        for u, v in friendships:
            if not self.can_communicate(u, v, languages):
                problem_people.add(u)
                problem_people.add(v)

        teach = float("inf")

        for lang in range(1, n + 1):
            count = 0
            for user in problem_people:
                if lang not in languages[user - 1]:
                    count += 1
            teach = min(teach, count)

        return teach