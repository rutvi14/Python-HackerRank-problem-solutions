from operator import itemgetter


def person_lister(f):
    def inner(people):
        # complete the function
        # sorted_person = sorted(people, key=itemgetter(2), reverse=False)
        # formatted_person = [f(person) for person in sorted_person]
        # return formatted_person passed all test cases except 3
        return map(f, sorted(people, key=lambda x: int(x[2])))

    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


if __name__ == "__main__":
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep="\n")
