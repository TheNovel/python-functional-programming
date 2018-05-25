import functools


def meanAge(records):
    correctRecords = [r for r in records if 'age' in r.keys()]

    ageRecs = len(correctRecords)
    ageTotal = functools.reduce(
        lambda prev, curr: prev + curr,
        [r['age'] for r in correctRecords],
        0
    )

    if ageRecs:
        return ageTotal / ageRecs
